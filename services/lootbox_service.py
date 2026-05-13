import logging
import random
from database.db import get_connection
from database.user_repo import update_balance, get_user_full
from config import LOOTBOX_PRICES, LOOTBOX_REWARDS
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)

RARITY_EMOJI = {
    "common": "📦",
    "rare": "🎁",
    "epic": "💎",
    "legendary": "👑",
}


async def buy_lootbox(user_id: int, rarity: str, lang: str) -> dict:
    price = LOOTBOX_PRICES.get(rarity)
    if not price:
        return {"ok": False, "text": t("lootbox_invalid_rarity", lang)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < price:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    await update_balance(user_id, -price)

    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO lootbox_inventory (user_id, lootbox_type, quantity) VALUES (?, ?, 1) "
            "ON CONFLICT(id) DO UPDATE SET quantity = quantity + 1",
            (user_id, rarity),
        )
        await conn.commit()
    finally:
        await conn.close()

    emoji = RARITY_EMOJI.get(rarity, "📦")
    return {"ok": True, "text": t("lootbox_bought", lang, emoji=emoji, rarity=rarity.upper(), price=format_money(price, lang))}


async def open_lootbox(user_id: int, rarity: str, lang: str) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT quantity FROM lootbox_inventory WHERE user_id = ? AND lootbox_type = ?",
            (user_id, rarity),
        ) as cur:
            row = await cur.fetchone()
            if not row or row[0] <= 0:
                return {"ok": False, "text": t("lootbox_none", lang, rarity=rarity.upper())}

        await conn.execute(
            "UPDATE lootbox_inventory SET quantity = quantity - 1 WHERE user_id = ? AND lootbox_type = ?",
            (user_id, rarity),
        )
        await conn.execute(
            "DELETE FROM lootbox_inventory WHERE user_id = ? AND lootbox_type = ? AND quantity <= 0",
            (user_id, rarity),
        )
        await conn.commit()
    finally:
        await conn.close()

    rewards_pool = LOOTBOX_REWARDS.get(rarity, {"money": (50, 200)})
    reward_type = random.choice(list(rewards_pool.keys()))
    reward_range = rewards_pool[reward_type]
    value = random.randint(reward_range[0], reward_range[1]) if reward_range[0] != reward_range[1] else reward_range[0]

    result_text = ""
    if reward_type == "money":
        await update_balance(user_id, value)
        result_text = t("lootbox_money", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper(), amount=format_money(value, lang))
    elif reward_type == "debt_bomb":
        from database.user_repo import update_debt
        await update_debt(user_id, value)
        result_text = t("lootbox_debt_bomb", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper(), amount=format_money(value, lang))
    elif reward_type == "shield":
        from datetime import datetime, timedelta
        conn2 = await get_connection()
        try:
            expires = datetime.now() + timedelta(hours=24)
            await conn2.execute(
                "INSERT INTO active_shields (user_id, shield_type, expires_at) VALUES (?, 'anti_trap', ?)",
                (user_id, expires.strftime("%Y-%m-%d %H:%M:%S")),
            )
            await conn2.commit()
        finally:
            await conn2.close()
        result_text = t("lootbox_shield", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper())
    elif reward_type == "chaos_buff":
        result_text = t("lootbox_chaos_buff", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper())
    elif reward_type == "curse":
        penalty = random.randint(100, 500)
        await update_balance(user_id, -penalty)
        result_text = t("lootbox_curse", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper(), penalty=format_money(penalty, lang))
    elif reward_type == "title_unlock":
        result_text = t("lootbox_title", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper())
    else:
        result_text = t("lootbox_nothing", lang, emoji=RARITY_EMOJI.get(rarity, "📦"), rarity=rarity.upper())

    conn3 = await get_connection()
    try:
        await conn3.execute(
            "INSERT INTO lootbox_rewards (user_id, reward_type, reward_value, rarity) VALUES (?, ?, ?, ?)",
            (user_id, reward_type, value, rarity),
        )
        await conn3.commit()
    finally:
        await conn3.close()

    return {"ok": True, "text": result_text}


async def get_lootbox_inventory(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT lootbox_type, quantity FROM lootbox_inventory WHERE user_id = ? AND quantity > 0",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()

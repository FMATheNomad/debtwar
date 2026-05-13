import logging
from datetime import datetime, timedelta
from database.db import get_connection
from database.user_repo import get_user_full, update_balance
from config import MARKET_ITEMS
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)


async def get_market_items() -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM market_items ORDER BY price ASC"
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def buy_item(user_id: int, item_id: str, lang: str) -> dict:
    items = {k: v for k, v in MARKET_ITEMS.items()}
    item = items.get(item_id)
    if not item:
        return {"ok": False, "text": t("market_item_not_found", lang)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < item["price"]:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    await update_balance(user_id, -item["price"])

    conn = await get_connection()
    try:
        if item["type"] == "consumable":
            await conn.execute(
                "INSERT INTO user_items (user_id, item_id, quantity) VALUES (?, ?, 1) "
                "ON CONFLICT(id) DO UPDATE SET quantity = quantity + 1",
                (user_id, item_id),
            )
        elif item["type"] == "shield":
            expires_at = datetime.now() + timedelta(hours=item.get("duration_hours", 24))
            await conn.execute(
                "INSERT INTO active_shields (user_id, shield_type, expires_at, durability) VALUES (?, ?, ?, 1)",
                (user_id, item["effect"], expires_at.strftime("%Y-%m-%d %H:%M:%S")),
            )
        else:
            await conn.execute(
                "INSERT INTO user_items (user_id, item_id, quantity) VALUES (?, ?, 1) "
                "ON CONFLICT(id) DO UPDATE SET quantity = quantity + 1",
                (user_id, item_id),
            )
        await conn.commit()
    finally:
        await conn.close()

    return {"ok": True, "text": t("market_bought", lang, name=item["name"], price=format_money(item["price"], lang))}


async def get_user_items(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT ui.item_id, ui.quantity, mi.name, mi.description, mi.item_type "
            "FROM user_items ui JOIN market_items mi ON ui.item_id = mi.id "
            "WHERE ui.user_id = ? AND ui.quantity > 0",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_active_shields(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT * FROM active_shields
               WHERE user_id = ? AND expires_at > datetime('now', 'localtime')
               ORDER BY expires_at DESC""",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def has_active_shield(user_id: int, shield_effect: str) -> bool:
    shields = await get_active_shields(user_id)
    return any(s["shield_type"] == shield_effect for s in shields)

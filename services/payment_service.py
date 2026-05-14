import logging
from datetime import datetime, timedelta
from database.db import get_connection
from database.user_repo import update_balance
from utils.formatter import format_money

logger = logging.getLogger(__name__)

PRODUCTS = {
    "starter_pack": {
        "id": "starter_pack",
        "title": "Starter Pack",
        "description": "500 coins + Basic Shield 24h + Common Lootbox\nSekali beli, langsung kaya!",
        "price_cents": 50,
        "label": "$0.50",
        "type": "one_time",
    },
    "season_pass": {
        "id": "season_pass",
        "title": "Season Pass",
        "description": "Daily reward 2x + Title eksklusif + 1 Rare Lootbox/minggu\nBerlaku 30 hari.",
        "price_cents": 150,
        "label": "$1.50",
        "type": "subscription",
        "duration_days": 30,
    },
    "gems_100": {
        "id": "gems_100",
        "title": "100 Gems",
        "description": "Gems adalah koin premium! Buat lootbox legendary, ganti title, reset cooldown.",
        "price_cents": 50,
        "label": "$0.50",
        "type": "gems",
        "gems": 100,
    },
    "gems_300": {
        "id": "gems_300",
        "title": "300 Gems (+30 bonus)",
        "description": "Dapat 330 Gems! Hemat 10%.",
        "price_cents": 150,
        "label": "$1.50",
        "type": "gems",
        "gems": 330,
    },
    "gems_1000": {
        "id": "gems_1000",
        "title": "1000 Gems (+200 bonus)",
        "description": "Dapat 1200 Gems! Hemat 20%.",
        "price_cents": 400,
        "label": "$4.00",
        "type": "gems",
        "gems": 1200,
    },
}


async def has_active_season_pass(user_id: int) -> bool:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT expires_at FROM purchases WHERE user_id = ? AND product_id = 'season_pass' AND (expires_at IS NULL OR expires_at > datetime('now', 'localtime')) ORDER BY purchased_at DESC LIMIT 1",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            return row is not None
    finally:
        await conn.close()


async def get_gems(user_id: int) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT balance FROM user_gems WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0
    finally:
        await conn.close()


async def add_gems(user_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO user_gems (user_id, balance) VALUES (?, ?) ON CONFLICT(user_id) DO UPDATE SET balance = balance + ?",
            (user_id, amount, amount),
        )
        await conn.commit()
    finally:
        await conn.close()


async def record_purchase(user_id: int, product_id: str, charge_id: str, stars: int):
    product = PRODUCTS.get(product_id)
    if not product:
        return
    conn = await get_connection()
    try:
        expires_at = None
        if product["type"] == "subscription":
            expires_at = (datetime.now() + timedelta(days=product.get("duration_days", 30))).strftime("%Y-%m-%d %H:%M:%S")
        await conn.execute(
            "INSERT INTO purchases (user_id, product_id, telegram_charge_id, amount_stars, expires_at) VALUES (?, ?, ?, ?, ?)",
            (user_id, product_id, charge_id, stars, expires_at),
        )
        await conn.commit()

        if product_id == "starter_pack":
            await update_balance(user_id, 500)
        elif product["type"] == "gems":
            await add_gems(user_id, product.get("gems", 0))
    finally:
        await conn.close()

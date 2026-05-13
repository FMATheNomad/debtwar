import logging
import random
import asyncio
from datetime import datetime
from database.db import get_connection
from database.user_repo import get_user_full, update_balance, update_debt, set_user_field
from config import WORLD_EVENT_CHANCE, EVENT_CRISIS_MULTIPLIER, EVENT_BOOM_MULTIPLIER, EVENT_GIFT_AMOUNT
from services.drama_service import generate_world_drama, record_drama
from utils.translator import t

logger = logging.getLogger(__name__)

WORLD_EVENTS = [
    {
        "id": "debt_crisis",
        "title_id": "event_title_debt_crisis",
        "desc_id": "event_desc_debt_crisis",
        "multiplier": 1.5,
        "duration_minutes": 60,
    },
    {
        "id": "tax_season",
        "title_id": "event_title_tax_season",
        "desc_id": "event_desc_tax_season",
        "multiplier": 0.8,
        "duration_minutes": 120,
    },
    {
        "id": "gov_audit",
        "title_id": "event_title_gov_audit",
        "desc_id": "event_desc_gov_audit",
        "multiplier": 0.5,
        "duration_minutes": 90,
    },
    {
        "id": "inflation",
        "title_id": "event_title_inflation",
        "desc_id": "event_desc_inflation",
        "multiplier": 2.0,
        "duration_minutes": 45,
    },
    {
        "id": "crypto_crash",
        "title_id": "event_title_crypto_crash",
        "desc_id": "event_desc_crypto_crash",
        "multiplier": 0.3,
        "duration_minutes": 30,
    },
    {
        "id": "stimulus",
        "title_id": "event_title_stimulus",
        "desc_id": "event_desc_stimulus",
        "multiplier": 0.0,
        "duration_minutes": 60,
    },
]


async def trigger_random_event() -> dict:
    if random.random() >= WORLD_EVENT_CHANCE:
        return None

    event = random.choice(WORLD_EVENTS)
    now = datetime.now()
    from datetime import timedelta
    ended_at = now + timedelta(minutes=event["duration_minutes"])

    conn = await get_connection()
    try:
        await conn.execute(
            """INSERT INTO world_events (event_type, title, description, multiplier, started_at, ended_at, is_active)
               VALUES (?, ?, ?, ?, ?, ?, 1)""",
            (event["id"], event["title_id"], event["desc_id"], event["multiplier"],
             now.strftime("%Y-%m-%d %H:%M:%S"), ended_at.strftime("%Y-%m-%d %H:%M:%S")),
        )
        await conn.commit()
    finally:
        await conn.close()

    effect_pct = {
        "debt_crisis": 10, "tax_season": 5, "gov_audit": 5,
        "inflation": 10, "crypto_crash": 10, "stimulus": 0,
    }.get(event["id"], 0)
    drama_text = await generate_world_drama(event["id"], effect_pct, EVENT_GIFT_AMOUNT)
    logger.info(f"World event triggered: {event['id']}")

    return {
        "event": event,
        "started_at": now,
        "ended_at": ended_at,
        "drama": drama_text,
    }


async def apply_event_effects(event_type: str, multiplier: float):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, balance, debt FROM users WHERE id IS NOT NULL"
        ) as cur:
            users = await cur.fetchall()

        for u in users:
            if event_type == "stimulus":
                bonus = random.randint(50, 200)
                await update_balance(u["id"], bonus)
            elif event_type == "debt_crisis":
                increase = int(u["debt"] * 0.1 * multiplier)
                if increase > 0:
                    await update_debt(u["id"], increase)
            elif event_type == "tax_season":
                tax = int(u["balance"] * 0.05)
                if tax > 0:
                    await update_balance(u["id"], -tax)
            elif event_type == "crypto_crash":
                loss = int(u["balance"] * 0.1)
                if loss > 0:
                    await update_balance(u["id"], -loss)

        await conn.commit()
    finally:
        await conn.close()


async def get_active_event():
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM world_events WHERE is_active = 1 AND ended_at > datetime('now', 'localtime') ORDER BY started_at DESC LIMIT 1"
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def deactivate_expired_events():
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE world_events SET is_active = 0 WHERE ended_at <= datetime('now', 'localtime') AND is_active = 1"
        )
        await conn.commit()
    finally:
        await conn.close()

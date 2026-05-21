import logging
import random
from datetime import datetime
from database.db import get_connection
from utils.translator import t

logger = logging.getLogger(__name__)


async def record_drama(text: str):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO drama_log (drama_text) VALUES (?)", (text,)
        )
        await conn.commit()
    finally:
        await conn.close()


async def generate_drama(username: str, count: int = 1, bounty: int = 0, lang: str = "id") -> str:
    idx = random.randint(0, 11)
    text = t(f"drama_template_{idx}", lang, user=username, count=count, bounty=bounty)
    await record_drama(text)
    return text


async def generate_world_drama(event_type: str, percent: int = 0, amount: int = 0, lang: str = "id") -> str:
    text = t(f"drama_event_{event_type}", lang, percent=percent, amount=amount)
    await record_drama(text)
    return text


async def get_recent_drama(limit: int = 5) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT drama_text, created_at FROM drama_log ORDER BY created_at DESC LIMIT ?",
            (limit,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()

import logging
from datetime import datetime
from database.db import get_connection
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def get_world_news(lang: str = "id") -> dict:
    active_event = None
    recent_drama = []
    prev_events = []

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM world_events WHERE is_active = 1 AND ended_at > datetime('now', 'localtime') ORDER BY started_at DESC LIMIT 1"
        ) as cur:
            row = await cur.fetchone()
            if row:
                row = dict(row)
                ended = datetime.strptime(row["ended_at"], "%Y-%m-%d %H:%M:%S")
                remaining = int((ended - datetime.now()).total_seconds())
                active_event = {
                    "title": row["title"],
                    "description": row["description"],
                    "remaining": remaining,
                    "multiplier": row["multiplier"],
                }

        async with conn.execute(
            "SELECT * FROM world_events WHERE is_active = 0 ORDER BY started_at DESC LIMIT 5"
        ) as cur:
            rows = await cur.fetchall()
            prev_events = [dict(r) for r in rows]

        async with conn.execute(
            "SELECT drama_text, created_at FROM drama_log ORDER BY created_at DESC LIMIT 5"
        ) as cur:
            rows = await cur.fetchall()
            recent_drama = [dict(r) for r in rows]

    finally:
        await conn.close()

    return {
        "active_event": active_event,
        "recent_drama": recent_drama,
        "prev_events": prev_events,
    }

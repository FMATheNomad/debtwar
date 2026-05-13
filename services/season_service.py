import logging
from datetime import datetime, timedelta
from database.db import get_connection
from config import SEASON_DURATION_DAYS, SEASON_XP_PER_LEND, SEASON_XP_PER_COLLECT, SEASON_XP_PER_TRAP

logger = logging.getLogger(__name__)


async def get_or_create_active_season() -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM seasons WHERE is_active = 1 AND (ended_at IS NULL OR ended_at > datetime('now', 'localtime')) ORDER BY started_at DESC LIMIT 1"
        ) as cur:
            row = await cur.fetchone()
            if row:
                return dict(row)

        import random
        season_names = [
            "Rise of Debt",
            "Chaos Protocol",
            "Mafia Empire",
            "Crypto Winter",
            "Shadow Economy",
            "Debt Revolution",
            "Scammer Paradise",
            "Banker's Gambit",
        ]
        name = random.choice(season_names)
        now = datetime.now()
        ended = now + timedelta(days=SEASON_DURATION_DAYS)

        await conn.execute(
            "INSERT INTO seasons (name, started_at, ended_at, is_active) VALUES (?, ?, ?, 1)",
            (name, now.strftime("%Y-%m-%d %H:%M:%S"), ended.strftime("%Y-%m-%d %H:%M:%S")),
        )
        await conn.commit()

        async with conn.execute(
            "SELECT * FROM seasons WHERE is_active = 1 ORDER BY started_at DESC LIMIT 1"
        ) as cur:
            row = await cur.fetchone()
            return dict(row)
    finally:
        await conn.close()


async def add_season_xp(user_id: int, action: str):
    season = await get_or_create_active_season()
    if not season:
        return

    xp_map = {
        "lend": SEASON_XP_PER_LEND,
        "collect": SEASON_XP_PER_COLLECT,
        "trap": SEASON_XP_PER_TRAP,
    }
    xp = xp_map.get(action, 5)

    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO season_leaderboard (season_id, user_id, score) VALUES (?, ?, ?) "
            "ON CONFLICT(season_id, user_id) DO UPDATE SET score = score + ?",
            (season["id"], user_id, xp, xp),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_season_leaderboard(season_id: int = None, limit: int = 10) -> list:
    conn = await get_connection()
    try:
        if not season_id:
            season = await get_or_create_active_season()
            season_id = season["id"]

        async with conn.execute(
            """SELECT sl.user_id, u.username, sl.score
               FROM season_leaderboard sl JOIN users u ON sl.user_id = u.id
               WHERE sl.season_id = ?
               ORDER BY sl.score DESC LIMIT ?""",
            (season_id, limit),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()

import logging
from database.db import get_connection
from config import WANTED_CHAOS_THRESHOLD, WANTED_BOUNTY_PER_CHAOS, WANTED_TARGET_MULTIPLIER

logger = logging.getLogger(__name__)


async def update_wanted_status(user_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT (traps_set + total_lent/100 + total_collected/100) as chaos_score
               FROM users WHERE id = ?""",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if not row:
                return
            chaos = row[0] or 0

        if chaos >= WANTED_CHAOS_THRESHOLD:
            bounty = chaos * WANTED_BOUNTY_PER_CHAOS
            level = min(chaos // 20 + 1, 10)
            await conn.execute(
                """INSERT INTO wanted_list (user_id, bounty, wanted_level, total_crimes)
                   VALUES (?, ?, ?, 1)
                   ON CONFLICT(user_id) DO UPDATE SET
                   bounty = ?, wanted_level = ?, total_crimes = total_crimes + 1,
                   updated_at = datetime('now', 'localtime')""",
                (user_id, bounty, level, bounty, level),
            )
        else:
            await conn.execute(
                "DELETE FROM wanted_list WHERE user_id = ?", (user_id,)
            )
        await conn.commit()
    finally:
        await conn.close()


async def get_wanted_list(limit: int = 10) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT w.user_id, u.username, w.bounty, w.wanted_level, w.total_crimes,
                      (u.traps_set + u.total_lent/100 + u.total_collected/100) as chaos_score
               FROM wanted_list w JOIN users u ON w.user_id = u.id
               ORDER BY w.bounty DESC LIMIT ?""",
            (limit,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def is_wanted(user_id: int) -> bool:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT 1 FROM wanted_list WHERE user_id = ?", (user_id,)
        ) as cur:
            return await cur.fetchone() is not None
    finally:
        await conn.close()


async def get_wanted_multiplier(user_id: int) -> float:
    if await is_wanted(user_id):
        return WANTED_TARGET_MULTIPLIER
    return 1.0

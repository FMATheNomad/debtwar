import logging
from database.db import get_connection
from config import TITLES
from services.credit_service import get_credit_score

logger = logging.getLogger(__name__)


async def get_user_credit_and_chaos(user_id: int) -> tuple:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT credit_score,
                      (traps_set + total_lent/100 + total_collected/100) as chaos_score
               FROM users WHERE id = ?""",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                return row[0], row[1] or 0
            return 500, 0
    finally:
        await conn.close()


async def get_current_title(user_id: int) -> str:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT title_id FROM user_titles WHERE user_id = ? AND is_active = 1",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                return row[0]
        async with conn.execute(
            "SELECT title_id FROM user_titles WHERE user_id = ? ORDER BY unlocked_at DESC LIMIT 1",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                return row[0]
        return "debt_peon"
    finally:
        await conn.close()


async def get_title_name(title_id: str) -> str:
    data = TITLES.get(title_id)
    return data["name"] if data else title_id


async def update_title(user_id: int) -> str:
    credit, chaos = await get_user_credit_and_chaos(user_id)
    best_title = "debt_peon"
    for tid, tdata in sorted(TITLES.items(), key=lambda x: (x[1]["min_credit"], x[1]["min_chaos"])):
        if credit >= tdata["min_credit"] and chaos >= tdata["min_chaos"]:
            best_title = tid

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT title_id FROM user_titles WHERE user_id = ? AND title_id = ?",
            (user_id, best_title),
        ) as cur:
            exists = await cur.fetchone()

        if not exists:
            await conn.execute(
                "INSERT OR IGNORE INTO user_titles (user_id, title_id, is_active) VALUES (?, ?, 1)",
                (user_id, best_title),
            )
        else:
            await conn.execute(
                "UPDATE user_titles SET is_active = 1 WHERE user_id = ? AND title_id = ?",
                (user_id, best_title),
            )

        await conn.execute(
            "UPDATE user_titles SET is_active = 0 WHERE user_id = ? AND title_id != ?",
            (user_id, best_title),
        )
        await conn.commit()
    finally:
        await conn.close()

    return best_title


async def get_all_unlocked_titles(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT title_id FROM user_titles WHERE user_id = ? ORDER BY unlocked_at DESC",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [row[0] for row in rows]
    finally:
        await conn.close()

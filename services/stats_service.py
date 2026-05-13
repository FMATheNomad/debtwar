import logging
from datetime import datetime
from database.db import get_connection

logger = logging.getLogger(__name__)


async def record_stat(user_id: int, stat_type: str, stat_value: int = 1):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO stats_history (user_id, stat_type, stat_value) VALUES (?, ?, ?)",
            (user_id, stat_type, stat_value),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_stats(user_id: int, stat_type: str = None, limit: int = 50) -> list:
    conn = await get_connection()
    try:
        if stat_type:
            query = "SELECT stat_type, stat_value, recorded_at FROM stats_history WHERE user_id = ? AND stat_type = ? ORDER BY recorded_at DESC LIMIT ?"
            params = (user_id, stat_type, limit)
        else:
            query = "SELECT stat_type, stat_value, recorded_at FROM stats_history WHERE user_id = ? ORDER BY recorded_at DESC LIMIT ?"
            params = (user_id, limit)
        async with conn.execute(query, params) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_stat_summary(user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT stat_type, SUM(stat_value) as total
               FROM stats_history WHERE user_id = ?
               GROUP BY stat_type ORDER BY total DESC""",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return {row["stat_type"]: row["total"] for row in rows}
    finally:
        await conn.close()


async def get_peak_balance(user_id: int) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT MAX(stat_value) FROM stats_history WHERE user_id = ? AND stat_type = 'balance_peak'",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            return row[0] or 0
    finally:
        await conn.close()


async def record_balance_peak(user_id: int, balance: int):
    peak = await get_peak_balance(user_id)
    if balance > peak:
        await record_stat(user_id, "balance_peak", balance)

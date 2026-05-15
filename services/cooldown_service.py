import time
import logging
from database.db import get_connection
from config import COOLDOWNS

logger = logging.getLogger(__name__)


async def check_cooldown(user_id: int, command: str) -> int:
    now = time.time()
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT expires_at FROM cooldowns WHERE user_id = ? AND command = ?",
            (user_id, command),
        ) as cur:
            row = await cur.fetchone()

        if row:
            expires_at = row[0]
            remaining = expires_at - int(now)
            if remaining > 0:
                return remaining
            await conn.execute(
                "DELETE FROM cooldowns WHERE user_id = ? AND command = ?",
                (user_id, command),
            )
            await conn.commit()

        cd_time = COOLDOWNS.get(command, 0)
        if cd_time > 0:
            expires_at = int(now) + cd_time
            await conn.execute(
                "INSERT OR REPLACE INTO cooldowns (user_id, command, expires_at) VALUES (?, ?, ?)",
                (user_id, command, expires_at),
            )
            await conn.commit()
        return 0
    finally:
        await conn.close()


async def is_on_cooldown(user_id: int, command: str) -> bool:
    return await check_cooldown(user_id, command) > 0


async def get_remaining(user_id: int, command: str) -> int:
    return await check_cooldown(user_id, command)


async def clear_cooldown(user_id: int, command: str = None):
    conn = await get_connection()
    try:
        if command:
            await conn.execute(
                "DELETE FROM cooldowns WHERE user_id = ? AND command = ?",
                (user_id, command),
            )
        else:
            await conn.execute(
                "DELETE FROM cooldowns WHERE user_id = ?",
                (user_id,),
            )
        await conn.commit()
    finally:
        await conn.close()


def get_all_cooldowns(user_id: int) -> dict:
    return {}

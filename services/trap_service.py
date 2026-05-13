import logging
import random
from database.db import get_connection
from database.user_repo import get_user_full
from services.credit_service import get_credit_tier

logger = logging.getLogger(__name__)


async def get_available_traps(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, name, success_rate, min_damage, max_damage, cooldown_seconds, cost FROM trap_types"
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def get_trap_type(trap_id: str):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM trap_types WHERE id = ?", (trap_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def calculate_advanced_trap(trap_data: dict, trapper_id: int) -> dict:
    tier = await get_credit_tier(trapper_id)
    success_rate = min(trap_data["success_rate"] * tier["multipliers"]["trap_success"], 0.95)
    success = random.random() < success_rate
    damage = random.randint(trap_data["min_damage"], trap_data["max_damage"]) if success else 0

    return {
        "success": success,
        "damage": damage,
        "trap_name": trap_data["name"],
        "trap_id": trap_data["id"],
    }

import logging
from config import CREDIT_SCORE_DEFAULT, CREDIT_SCORE_MIN, CREDIT_SCORE_MAX
from database.db import get_connection

logger = logging.getLogger(__name__)


async def get_credit_score(user_id: int) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT credit_score FROM users WHERE id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else CREDIT_SCORE_DEFAULT
    finally:
        await conn.close()


async def modify_credit_score(user_id: int, delta: int) -> int:
    conn = await get_connection()
    try:
        await conn.execute(
            """UPDATE users SET credit_score = GREATEST(?, LEAST(?, credit_score + ?))
               WHERE id = ?""",
            (CREDIT_SCORE_MIN, CREDIT_SCORE_MAX, delta, user_id),
        )
        await conn.commit()
        async with conn.execute(
            "SELECT credit_score FROM users WHERE id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else CREDIT_SCORE_DEFAULT
    finally:
        await conn.close()


async def add_repay_history(user_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET total_repaid = total_repaid + ? WHERE id = ?",
            (amount, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def add_default_history(user_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET total_defaulted = total_defaulted + ? WHERE id = ?",
            (amount, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_credit_tier(user_id: int) -> dict:
    score = await get_credit_score(user_id)
    if score >= 900:
        return {"tier": "SS", "label": "Legendary", "multipliers": {"interest": 0.5, "trap_success": 1.2, "spy_success": 1.1}}
    elif score >= 750:
        return {"tier": "S", "label": "Elite", "multipliers": {"interest": 0.7, "trap_success": 1.1, "spy_success": 1.05}}
    elif score >= 600:
        return {"tier": "A", "label": "Trusted", "multipliers": {"interest": 0.9, "trap_success": 1.0, "spy_success": 1.0}}
    elif score >= 400:
        return {"tier": "B", "label": "Average", "multipliers": {"interest": 1.0, "trap_success": 1.0, "spy_success": 1.0}}
    elif score >= 200:
        return {"tier": "C", "label": "Risky", "multipliers": {"interest": 1.2, "trap_success": 0.9, "spy_success": 0.95}}
    else:
        return {"tier": "D", "label": "Defaulted", "multipliers": {"interest": 1.5, "trap_success": 0.8, "spy_success": 0.9}}

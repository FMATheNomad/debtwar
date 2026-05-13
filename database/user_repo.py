import logging
import re
from datetime import date
from database.db import get_connection

logger = logging.getLogger(__name__)


async def get_user(user_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, username, balance, debt, language FROM users WHERE id = ?",
            (user_id,),
        ) as cur:
            return await cur.fetchone()
    finally:
        await conn.close()


async def get_user_full(user_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT id, username, balance, debt, language,
               total_lent, total_collected, traps_set, traps_successful,
               daily_streak, last_daily, bankrupt_count, is_bankrupt,
               bankruptcy_date, total_daily_claimed
               FROM users WHERE id = ?""",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                return dict(row)
            return None
    finally:
        await conn.close()


async def get_user_by_username(username: str):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, username, balance, debt, language FROM users WHERE username = ?",
            (username,),
        ) as cur:
            return await cur.fetchone()
    finally:
        await conn.close()


async def get_or_create_by_username(username: str) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, username, balance, debt, language, total_lent, total_collected, traps_set, traps_successful, daily_streak, last_daily, bankrupt_count, is_bankrupt, bankruptcy_date, total_daily_claimed FROM users WHERE username = ?",
            (username,),
        ) as cur:
            row = await cur.fetchone()

        if row:
            return dict(row) | {"is_new": False}

        import random, time
        ghost_id = -random.randint(1_000_000, 99_999_999)
        await conn.execute(
            """INSERT INTO users (id, username, balance, debt, language, is_ghost)
               VALUES (?, ?, 1000, 0, 'id', 1) ON CONFLICT(id) DO NOTHING""",
            (ghost_id, username),
        )
        await conn.commit()

        async with conn.execute(
            "SELECT id, username, balance, debt, language, total_lent, total_collected, traps_set, traps_successful, daily_streak, last_daily, bankrupt_count, is_bankrupt, bankruptcy_date, total_daily_claimed FROM users WHERE username = ?",
            (username,),
        ) as cur:
            row = await cur.fetchone()

        if not row:
            return {"id": 0, "username": username, "balance": 1000, "debt": 0, "language": "id",
                    "total_lent": 0, "total_collected": 0, "traps_set": 0, "traps_successful": 0,
                    "daily_streak": 0, "last_daily": None, "bankrupt_count": 0, "is_bankrupt": 0,
                    "bankruptcy_date": None, "total_daily_claimed": 0, "is_ghost": 1, "is_new": True}

        return dict(row) | {"is_new": True}
    finally:
        await conn.close()


async def register_user(user_id: int, username: str, language: str = "id") -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT id, balance, debt, language, total_lent, total_collected,
               traps_set, traps_successful, daily_streak, last_daily,
               bankrupt_count, is_bankrupt, bankruptcy_date, total_daily_claimed
                FROM users WHERE username = ? AND (id < 0 OR id != ?)""",
            (username, user_id),
        ) as cur:
            ghost = await cur.fetchone()

        if ghost:
            ghost_data = dict(ghost)
            await conn.execute("DELETE FROM users WHERE username = ? AND is_ghost = 1", (username,))
            await conn.execute(
                """INSERT OR REPLACE INTO users
                   (id, username, balance, debt, language, total_lent, total_collected,
                    traps_set, traps_successful, daily_streak, last_daily,
                    bankrupt_count, is_bankrupt, bankruptcy_date, total_daily_claimed, is_ghost)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)""",
                (
                    user_id, username,
                    ghost_data["balance"], ghost_data["debt"], language,
                    ghost_data["total_lent"], ghost_data["total_collected"],
                    ghost_data["traps_set"], ghost_data["traps_successful"],
                    ghost_data["daily_streak"], ghost_data["last_daily"],
                    ghost_data["bankrupt_count"], ghost_data["is_bankrupt"],
                    ghost_data["bankruptcy_date"], ghost_data["total_daily_claimed"],
                ),
            )
            await conn.commit()
            ghost_data["language"] = language
            ghost_data["is_ghost"] = True
            return ghost_data
        else:
            await conn.execute(
                "INSERT OR IGNORE INTO users (id, username, balance, debt, language) VALUES (?, ?, ?, 0, ?)",
                (user_id, username, 1000, language),
            )
            await conn.execute(
                "UPDATE users SET username = ?, language = ? WHERE id = ? AND (username != ? OR language != ?)",
                (username, language, user_id, username, language),
            )
            async with conn.execute(
                "SELECT display_name FROM users WHERE id = ?", (user_id,)
            ) as cur:
                row = await cur.fetchone()
                if row and not row[0]:
                    await conn.execute(
                        "UPDATE users SET needs_name = 1 WHERE id = ?",
                        (user_id,),
                    )
            await conn.commit()

            async with conn.execute(
                "SELECT balance, debt FROM users WHERE id = ?", (user_id,)
            ) as cur:
                row = await cur.fetchone()
            return {"balance": row[0], "debt": row[1], "is_ghost": False}
    finally:
        await conn.close()


async def update_balance(user_id: int, delta: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET balance = MAX(0, balance + ?) WHERE id = ?",
            (delta, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def set_balance(user_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET balance = ? WHERE id = ?",
            (amount, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def update_debt(user_id: int, delta: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET debt = MAX(0, debt + ?) WHERE id = ?",
            (delta, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def update_debt_by_username(username: str, delta: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET debt = MAX(0, debt + ?) WHERE username = ?",
            (delta, username),
        )
        await conn.commit()
    finally:
        await conn.close()


async def add_transaction(from_id: int, to_user: str, tx_type: str, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO transactions (from_id, to_user, type, amount) VALUES (?, ?, ?, ?)",
            (from_id, to_user, tx_type, amount),
        )
        await conn.commit()
    finally:
        await conn.close()


async def update_user_stat(user_id: int, field: str, delta: int = 1):
    allowed = {
        "total_lent", "total_collected", "traps_set",
        "traps_successful", "daily_streak", "bankrupt_count",
        "total_daily_claimed",
    }
    if field not in allowed:
        return
    conn = await get_connection()
    try:
        await conn.execute(
            f"UPDATE users SET {field} = {field} + ? WHERE id = ?",
            (delta, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def set_user_field(user_id: int, field: str, value):
    conn = await get_connection()
    try:
        await conn.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (value, user_id))
        await conn.commit()
    finally:
        await conn.close()


async def get_leaderboard(category: str, limit: int = 10):
    conn = await get_connection()
    try:
        if category == "richest":
            query = "SELECT username, MAX(display_name) as display_name, MAX(balance) as balance FROM users WHERE id IS NOT NULL AND username IS NOT NULL GROUP BY username ORDER BY balance DESC LIMIT ?"
        elif category == "debt":
            query = "SELECT username, MAX(display_name) as display_name, MAX(debt) as debt FROM users WHERE id IS NOT NULL AND username IS NOT NULL GROUP BY username ORDER BY debt DESC LIMIT ?"
        elif category == "chaos":
            query = """SELECT username, MAX(display_name) as display_name,
                       MAX(traps_set + total_lent/100 + total_collected/100) as chaos_score
                       FROM users WHERE id IS NOT NULL AND username IS NOT NULL GROUP BY username ORDER BY chaos_score DESC LIMIT ?"""
        else:
            return []
        async with conn.execute(query, (limit,)) as cur:
            rows = await cur.fetchall()
            result = []
            for row in rows:
                d = dict(row)
                if re.match(r'^.+\_\d+$', d.get("username", "")):
                    continue
                result.append(d)
            return result
    finally:
        await conn.close()


async def get_all_debtors():
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, username, debt, balance, language FROM users WHERE debt > 0 AND id IS NOT NULL"
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def check_daily_limit(user_id: int, limit_type: str, amount: int) -> bool:
    today = str(date.today())
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT total_lent, total_transfer FROM daily_limits WHERE user_id = ? AND date = ?",
            (user_id, today),
        ) as cur:
            row = await cur.fetchone()

        current = dict(row) if row else {"total_lent": 0, "total_transfer": 0}

        if limit_type == "lend":
            return current["total_lent"] + amount <= 5000
        elif limit_type == "transfer":
            return current["total_transfer"] + amount <= 3000
        return True
    finally:
        await conn.close()


async def add_daily_limit(user_id: int, limit_type: str, amount: int):
    today = str(date.today())
    conn = await get_connection()
    try:
        if limit_type == "lend":
            await conn.execute(
                """INSERT INTO daily_limits (user_id, date, total_lent)
                   VALUES (?, ?, ?)
                   ON CONFLICT(user_id, date) DO UPDATE SET total_lent = total_lent + ?""",
                (user_id, today, amount, amount),
            )
        elif limit_type == "transfer":
            await conn.execute(
                """INSERT INTO daily_limits (user_id, date, total_transfer)
                   VALUES (?, ?, ?)
                   ON CONFLICT(user_id, date) DO UPDATE SET total_transfer = total_transfer + ?""",
                (user_id, today, amount, amount),
            )
        await conn.commit()
    finally:
        await conn.close()


async def unlock_achievement(user_id: int, ach_id: str) -> bool:
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT OR IGNORE INTO achievements (user_id, ach_id) VALUES (?, ?)",
            (user_id, ach_id),
        )
        await conn.commit()
        async with conn.execute(
            "SELECT changes()"
        ) as cur:
            return (await cur.fetchone())[0] > 0
    finally:
        await conn.close()


async def get_user_achievements(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT ach_id FROM achievements WHERE user_id = ? ORDER BY unlocked DESC",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [row[0] for row in rows]
    finally:
        await conn.close()


async def get_achievement_count_by_username(username: str) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT COUNT(*) FROM achievements a JOIN users u ON a.user_id = u.id WHERE u.username = ?",
            (username,),
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0
    finally:
        await conn.close()


async def get_leaderboard_chaos_detail(limit: int = 10) -> list:
    conn = await get_connection()
    try:
        query = """SELECT username,
                   MAX(balance) as balance, MAX(debt) as debt,
                   MAX(total_lent) as total_lent, MAX(total_collected) as total_collected,
                   MAX(traps_set) as traps_set, MAX(traps_successful) as traps_successful,
                   MAX(traps_set + total_lent/100 + total_collected/100) as chaos_score
                   FROM users WHERE id IS NOT NULL AND username IS NOT NULL
                   GROUP BY username ORDER BY chaos_score DESC LIMIT ?"""
        async with conn.execute(query, (limit,)) as cur:
            rows = await cur.fetchall()
            result = []
            for row in rows:
                d = dict(row)
                if re.match(r'^.+\_\d+$', d.get("username", "")):
                    continue
                d["achievements"] = await get_achievement_count_by_username(d["username"])
                d["titles"] = await get_title_count_by_username(d["username"])
                d["active_title"] = await get_active_title_by_username(d["username"])
                result.append(d)
            return result
    finally:
        await conn.close()


async def get_title_count_by_username(username: str) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT COUNT(*) FROM user_titles ut JOIN users u ON ut.user_id = u.id WHERE u.username = ?",
            (username,),
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else 0
    finally:
        await conn.close()


async def get_active_title_by_username(username: str) -> str:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT t.name FROM user_titles ut
               JOIN users u ON ut.user_id = u.id
               JOIN titles t ON ut.title_id = t.id
               WHERE u.username = ? AND ut.is_active = 1 LIMIT 1""",
            (username,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                return row[0]
        async with conn.execute(
            """SELECT t.name FROM user_titles ut
               JOIN users u ON ut.user_id = u.id
               JOIN titles t ON ut.title_id = t.id
               WHERE u.username = ? ORDER BY ut.unlocked_at DESC LIMIT 1""",
            (username,),
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else None
    finally:
        await conn.close()


async def add_ghost_notification(target_user: str, from_name: str, action_type: str, amount: int = 0, detail: str = ""):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO ghost_notifications (target_user, from_name, action_type, amount, detail) VALUES (?, ?, ?, ?, ?)",
            (target_user, from_name, action_type, amount, detail),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_ghost_notifications(username: str) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT from_name, action_type, amount, detail, timestamp FROM ghost_notifications WHERE target_user = ? ORDER BY timestamp ASC",
            (username,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def clear_ghost_notifications(username: str):
    conn = await get_connection()
    try:
        await conn.execute("DELETE FROM ghost_notifications WHERE target_user = ?", (username,))
        await conn.commit()
    finally:
        await conn.close()


async def get_display_name(user_id: int, fallback: str = "Player") -> str:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT display_name, username FROM users WHERE id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            if row and row[0]:
                return row[0]
            if row and row[1]:
                return row[1]
            return fallback
    finally:
        await conn.close()


async def set_display_name(user_id: int, name: str):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE users SET display_name = ? WHERE id = ?", (name, user_id)
        )
        await conn.commit()
    finally:
        await conn.close()


async def link_ghost_by_username(username: str, user_id: int) -> bool:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id FROM users WHERE username = ? AND is_ghost = 1",
            (username,),
        ) as cur:
            row = await cur.fetchone()
        if row:
            await conn.execute(
                "UPDATE users SET id = ?, is_ghost = 0 WHERE username = ? AND is_ghost = 1",
                (user_id, username),
            )
            await conn.commit()
            logger.info(f"Linked ghost @{username} to user_id {user_id}")
            return True
        return False
    finally:
        await conn.close()
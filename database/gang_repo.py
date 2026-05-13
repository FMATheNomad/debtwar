import logging
from database.db import get_connection
from config import GANG_MAX_MEMBERS

logger = logging.getLogger(__name__)


async def create_gang(name: str, owner_id: int) -> dict:
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO gangs (name, owner_id) VALUES (?, ?)",
            (name, owner_id),
        )
        await conn.commit()
        async with conn.execute(
            "SELECT id FROM gangs WHERE name = ?", (name,)
        ) as cur:
            row = await cur.fetchone()
            gang_id = row[0]
        await conn.execute(
            "INSERT INTO gang_members (gang_id, user_id, role) VALUES (?, ?, 'owner')",
            (gang_id, owner_id),
        )
        await conn.commit()
        return {"ok": True, "gang_id": gang_id}
    except Exception as e:
        if "UNIQUE" in str(e):
            return {"ok": False, "error": "name_exists"}
        return {"ok": False, "error": str(e)}
    finally:
        await conn.close()


async def get_gang_by_user(user_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT g.id, g.name, g.owner_id, g.reputation, g.vault_balance, g.member_count, gm.role
               FROM gangs g JOIN gang_members gm ON g.id = gm.gang_id
               WHERE gm.user_id = ?""",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def get_gang_by_id(gang_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM gangs WHERE id = ?", (gang_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def get_gang_by_name(name: str):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM gangs WHERE name = ?", (name,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def get_gang_members(gang_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT u.id, u.username, u.balance, u.debt, gm.role, gm.joined_at
               FROM gang_members gm JOIN users u ON gm.user_id = u.id
               WHERE gm.gang_id = ? ORDER BY gm.joined_at ASC""",
            (gang_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def join_gang(gang_id: int, user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT member_count FROM gangs WHERE id = ?", (gang_id,)
        ) as cur:
            row = await cur.fetchone()
            if row and row[0] >= GANG_MAX_MEMBERS:
                return {"ok": False, "error": "full"}

        await conn.execute(
            "INSERT OR IGNORE INTO gang_members (gang_id, user_id, role) VALUES (?, ?, 'member')",
            (gang_id, user_id),
        )
        await conn.execute(
            "UPDATE gangs SET member_count = member_count + 1 WHERE id = ?",
            (gang_id,),
        )
        await conn.commit()
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        await conn.close()


async def leave_gang(gang_id: int, user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT role FROM gang_members WHERE gang_id = ? AND user_id = ?",
            (gang_id, user_id),
        ) as cur:
            row = await cur.fetchone()
            if not row:
                return {"ok": False, "error": "not_member"}
            if row[0] == "owner":
                member_count = await get_member_count(gang_id)
                if member_count > 1:
                    new_owner = await get_next_member(gang_id, user_id)
                    if new_owner:
                        await conn.execute(
                            "UPDATE gang_members SET role = 'owner' WHERE gang_id = ? AND user_id = ?",
                            (gang_id, new_owner),
                        )
                        await conn.execute(
                            "UPDATE gangs SET owner_id = ? WHERE id = ?",
                            (new_owner, gang_id),
                        )
                    else:
                        return {"ok": False, "error": "no_successor"}
                else:
                    await conn.execute("DELETE FROM gang_members WHERE gang_id = ?", (gang_id,))
                    await conn.execute("DELETE FROM gangs WHERE id = ?", (gang_id,))
                    await conn.commit()
                    return {"ok": True, "gang_deleted": True}

        await conn.execute(
            "DELETE FROM gang_members WHERE gang_id = ? AND user_id = ?",
            (gang_id, user_id),
        )
        await conn.execute(
            "UPDATE gangs SET member_count = MAX(0, member_count - 1) WHERE id = ?",
            (gang_id,),
        )
        await conn.commit()
        return {"ok": True}
    finally:
        await conn.close()


async def get_member_count(gang_id: int) -> int:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT COUNT(*) FROM gang_members WHERE gang_id = ?", (gang_id,)
        ) as cur:
            row = await cur.fetchone()
            return row[0]
    finally:
        await conn.close()


async def get_next_member(gang_id: int, exclude_user_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT user_id FROM gang_members WHERE gang_id = ? AND user_id != ? ORDER BY joined_at ASC LIMIT 1",
            (gang_id, exclude_user_id),
        ) as cur:
            row = await cur.fetchone()
            return row[0] if row else None
    finally:
        await conn.close()


async def add_to_vault(gang_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE gangs SET vault_balance = vault_balance + ? WHERE id = ?",
            (amount, gang_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def remove_from_vault(gang_id: int, amount: int) -> bool:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT vault_balance FROM gangs WHERE id = ?", (gang_id,)
        ) as cur:
            row = await cur.fetchone()
            if not row or row[0] < amount:
                return False
        await conn.execute(
            "UPDATE gangs SET vault_balance = vault_balance - ? WHERE id = ?",
            (amount, gang_id),
        )
        await conn.commit()
        return True
    finally:
        await conn.close()


async def add_gang_reputation(gang_id: int, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE gangs SET reputation = reputation + ? WHERE id = ?",
            (amount, gang_id),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_gang_leaderboard(limit: int = 10) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT name, reputation, vault_balance, member_count
               FROM gangs ORDER BY reputation DESC LIMIT ?""",
            (limit,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def declare_gang_war(attacker_gang_id: int, defender_gang_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id FROM gang_wars WHERE (attacker_gang_id = ? AND defender_gang_id = ?) AND status IN ('declared', 'active')",
            (attacker_gang_id, defender_gang_id),
        ) as cur:
            existing = await cur.fetchone()
            if existing:
                return {"ok": False, "error": "war_exists"}

        await conn.execute(
            "INSERT INTO gang_wars (attacker_gang_id, defender_gang_id, status) VALUES (?, ?, 'declared')",
            (attacker_gang_id, defender_gang_id),
        )
        await conn.commit()
        return {"ok": True}
    finally:
        await conn.close()


async def get_gang_war(gang_war_id: int):
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM gang_wars WHERE id = ?", (gang_war_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else None
    finally:
        await conn.close()


async def get_active_wars_for_gang(gang_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM gang_wars WHERE (attacker_gang_id = ? OR defender_gang_id = ?) AND status IN ('declared', 'active')",
            (gang_id, gang_id),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def end_gang_war(gang_war_id: int, winner_id: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE gang_wars SET status = 'ended', winner_id = ?, ended_at = datetime('now', 'localtime') WHERE id = ?",
            (winner_id, gang_war_id),
        )
        await conn.commit()
    finally:
        await conn.close()

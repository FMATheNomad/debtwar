import logging
import random
from database.db import get_connection
from database.user_repo import get_user_full, update_balance, get_user_by_username
from config import COURT_LAWYER_COST, COURT_CORRUPTION_CHANCE, COURT_MAX_FINE
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)


async def file_case(plaintiff_id: int, defendant_name: str, charge: str, lang: str) -> dict:
    defendant = await get_user_by_username(defendant_name)
    if not defendant:
        return {"ok": False, "text": t("target_not_found", lang, username=defendant_name)}
    if defendant[0] == plaintiff_id:
        return {"ok": False, "text": t("court_sue_self", lang)}

    plaintiff = await get_user_full(plaintiff_id)
    if not plaintiff or plaintiff["balance"] < COURT_LAWYER_COST:
        return {"ok": False, "text": t("court_need_fee", lang, fee=format_money(COURT_LAWYER_COST, lang))}

    await update_balance(plaintiff_id, -COURT_LAWYER_COST)

    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO court_cases (plaintiff_id, defendant_id, charge) VALUES (?, ?, ?)",
            (plaintiff_id, defendant[0], charge),
        )
        await conn.commit()
        async with conn.execute("SELECT last_insert_rowid()") as cur:
            case_id = (await cur.fetchone())[0]
    finally:
        await conn.close()

    return {
        "ok": True,
        "text": t("court_case_filed", lang, case_id=case_id, defendant=defendant_name, charge=charge),
        "case_id": case_id,
    }


async def vote_case(voter_id: int, case_id: int, vote: str, lang: str) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM court_cases WHERE id = ? AND status = 'pending'", (case_id,)
        ) as cur:
            case = await cur.fetchone()
            if not case:
                return {"ok": False, "text": t("court_case_not_found", lang)}

        await conn.execute(
            "INSERT OR IGNORE INTO court_votes (case_id, voter_id, vote) VALUES (?, ?, ?)",
            (case_id, voter_id, vote),
        )
        await conn.commit()
    finally:
        await conn.close()

    return {"ok": True, "text": t("court_vote_recorded", lang, vote=vote.upper())}


async def resolve_case(case_id: int, lang: str = "en") -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM court_cases WHERE id = ? AND status = 'pending'", (case_id,)
        ) as cur:
            case = await cur.fetchone()
            if not case:
                return None

        async with conn.execute(
            "SELECT vote, COUNT(*) as cnt FROM court_votes WHERE case_id = ? GROUP BY vote",
            (case_id,),
        ) as cur:
            votes = await cur.fetchall()
            vote_dict = {v["vote"]: v["cnt"] for v in votes}
            guilty = vote_dict.get("guilty", 0)
            innocent = vote_dict.get("innocent", 0)

        corrupted = random.random() < COURT_CORRUPTION_CHANCE
        if corrupted:
            guilty += 1

        if guilty > innocent:
            verdict = "guilty"
            fine = min(guilty * 100, COURT_MAX_FINE)
            await update_balance(case["defendant_id"], -fine)
            await update_balance(case["plaintiff_id"], fine)
            result_text = t("court_verdict_guilty", lang, fine=format_money(fine, lang))
        else:
            verdict = "innocent"
            result_text = t("court_verdict_innocent", lang)

        await conn.execute(
            "UPDATE court_cases SET status = 'verdict', verdict = ? WHERE id = ?",
            (verdict, case_id),
        )
        await conn.commit()
    finally:
        await conn.close()

    return {"verdict": verdict, "text": result_text, "corrupted": corrupted, "guilty": guilty, "innocent": innocent}


async def resolve_pending_cases() -> int:
    conn = await get_connection()
    resolved = 0
    try:
        async with conn.execute(
            "SELECT id FROM court_cases WHERE status = 'pending' AND created_at < datetime('now', '-1 hour', 'localtime')"
        ) as cur:
            rows = await cur.fetchall()
        for row in rows:
            try:
                await resolve_case(row["id"])
                resolved += 1
            except Exception:
                pass
    finally:
        await conn.close()
    return resolved


async def get_pending_cases() -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT c.*, u.username as defendant_name FROM court_cases c JOIN users u ON c.defendant_id = u.id WHERE c.status = 'pending'"
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()

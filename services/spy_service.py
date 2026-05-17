import logging
import random
from database.db import get_connection
from database.user_repo import get_user_full, update_balance, add_contact
from services.credit_service import get_credit_tier
from config import SPY_SUCCESS_RATE, SPY_DETECTION_RATE, SPY_FAIL_FINE
from utils.translator import t
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def execute_spy(spy_id: int, target_name: str, lang: str) -> dict:
    spy_data = await get_user_full(spy_id)
    if not spy_data:
        return {"ok": False, "text": t("not_registered", lang)}

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT id, username, balance, debt, language, (traps_set + total_lent/100 + total_collected/100) as chaos_score FROM users WHERE username = ?",
            (target_name,),
        ) as cur:
            target = await cur.fetchone()
    finally:
        await conn.close()

    if not target:
        return {"ok": False, "text": t("target_not_found", lang, username=target_name)}

    tier = await get_credit_tier(spy_id)
    success_rate = min(SPY_SUCCESS_RATE * tier["multipliers"]["spy_success"], 0.95)
    detection_rate = SPY_DETECTION_RATE

    rolled = random.random()

    if rolled < success_rate:
        target_dict = dict(target)
        est_balance = target_dict.get("balance", 0)
        est_debt = target_dict.get("debt", 0)
        chaos = target_dict.get("chaos_score", 0)
        last_active = "Tidak diketahui"

        text = (
            f"🕵️ *Hasil Spy*\n\n"
            f"🎯 Target: @{target_name}\n"
            f"💰 Estimasi Saldo: ~{format_money(est_balance, lang)}\n"
            f"💳 Estimasi Utang: ~{format_money(est_debt, lang)}\n"
            f"💀 Chaos Score: {chaos}\n"
            f"📅 Last Active: {last_active}\n"
        )

        await log_spy(spy_id, target["id"], True, False)
        try:
            await add_contact(spy_id, target["id"])
        except Exception:
            pass
        return {"ok": True, "text": text}

    else:
        fine = SPY_FAIL_FINE
        await update_balance(spy_id, -fine)
        detected = random.random() < detection_rate
        await log_spy(spy_id, target["id"], False, detected)

        fail_text = t("spy_failed", lang, fine=format_money(fine, lang))
        if detected:
            fail_text += "\n\n🚨 *Kamu terdeteksi!* Target mendapat notifikasi!"

        return {"ok": False, "text": fail_text}


async def log_spy(spy_id: int, target_id: int, success: bool, detected: bool):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO spy_logs (spy_id, target_id, success, detected) VALUES (?, ?, ?, ?)",
            (spy_id, target_id, int(success), int(detected)),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_spy_stats(user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT COUNT(*) as total, SUM(success) as successes FROM spy_logs WHERE spy_id = ?",
            (user_id,),
        ) as cur:
            row = await cur.fetchone()
            if row:
                total = row[0] or 0
                successes = row[1] or 0
                return {"total": total, "successes": successes, "failures": total - successes}
            return {"total": 0, "successes": 0, "failures": 0}
    finally:
        await conn.close()

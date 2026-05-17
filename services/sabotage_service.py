import logging
import random
from database.user_repo import get_user_full, update_balance, get_user_by_username, set_user_field, add_contact
from services.credit_service import get_credit_tier
from config import SABOTAGE_SUCCESS_RATE, SABOTAGE_FAIL_FINE, SABOTAGE_STEAL_MIN, SABOTAGE_STEAL_MAX, SABOTAGE_FREEZE_SECONDS
from utils.translator import t
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def execute_sabotage(attacker_id: int, target_name: str, sabo_type: str, lang: str, cost: int = 0) -> dict:
    attacker = await get_user_full(attacker_id)
    if not attacker:
        return {"ok": False, "text": t("not_registered", lang)}

    target_row = await get_user_by_username(target_name)
    if not target_row:
        return {"ok": False, "text": t("target_not_found", lang, username=target_name)}

    target_id = target_row[0]
    if target_id == attacker_id:
        return {"ok": False, "text": t("self_sabotage", lang)}

    target = await get_user_full(target_id)
    tier = await get_credit_tier(attacker_id)
    success_rate = min(SABOTAGE_SUCCESS_RATE * tier["multipliers"]["spy_success"], 0.85)

    if cost > 0:
        await update_balance(attacker_id, -cost)

    if random.random() >= success_rate:
        return {"ok": False, "text": t("sabotage_failed", lang, fine=format_money(cost, lang))}

    result_text = ""
    if sabo_type == "freeze":
        await set_user_field(target_id, "is_bankrupt", 1)
        from datetime import datetime, timedelta
        freeze_until = datetime.now() + timedelta(seconds=SABOTAGE_FREEZE_SECONDS)
        await set_user_field(target_id, "bankruptcy_date", freeze_until.strftime("%Y-%m-%d %H:%M:%S"))
        result_text = t("sabotage_freeze", lang, target=target_name, duration="1 jam")

    elif sabo_type == "steal":
        steal_amount = random.randint(SABOTAGE_STEAL_MIN, min(SABOTAGE_STEAL_MAX, target["balance"]))
        if steal_amount > 0:
            await update_balance(target_id, -steal_amount)
            await update_balance(attacker_id, steal_amount)
            result_text = t("sabotage_steal", lang, target=target_name, amount=format_money(steal_amount, lang))
        else:
            result_text = t("sabotage_steal_empty", lang, target=target_name)

    elif sabo_type == "block_daily":
        from datetime import datetime, timedelta
        fake_claim = (datetime.now() - timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")
        await set_user_field(target_id, "last_daily", fake_claim)
        result_text = t("sabotage_block_daily", lang, target=target_name)

    else:
        return {"ok": False, "text": t("sabotage_unknown_type", lang)}

    try:
        await add_contact(attacker_id, target_id)
    except Exception:
        pass
    await log_sabotage(attacker_id, target_id, sabo_type, True)
    return {"ok": True, "text": result_text}


async def log_sabotage(attacker_id: int, target_id: int, sabo_type: str, success: bool, amount: int = 0):
    from database.db import get_connection
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO sabotage_logs (attacker_id, target_id, sabotage_type, success, amount) VALUES (?, ?, ?, ?, ?)",
            (attacker_id, target_id, sabo_type, int(success), amount),
        )
        await conn.commit()
    finally:
        await conn.close()

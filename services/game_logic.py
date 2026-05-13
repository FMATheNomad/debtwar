import logging
import random
from config import MAX_DEBT
from utils.translator import t
from utils.formatter import format_money
from services.economy import (
    calculate_trap, apply_trap_consequences,
    apply_utang, apply_nagih, apply_transfer,
    check_bankruptcy, check_bankruptcy_status,
)
from database.user_repo import (
    get_user, get_user_full, get_or_create_by_username,
    update_balance, update_debt, update_debt_by_username,
    check_daily_limit, add_daily_limit, add_transaction,
    add_ghost_notification,
)
from services.cooldown_service import check_cooldown
from services.notification import send_notification

logger = logging.getLogger(__name__)

UTANG_CHAOS_KEYS = [f"utang_chaos_{i}" for i in range(10)]
NAGIH_SUCCESS_KEYS = [f"nagih_success_{i}" for i in range(5)]
NAGIH_FAIL_KEYS = [f"nagih_fail_{i}" for i in range(5)]
JEBAK_SUCCESS_KEYS = [f"jebak_success_{i}" for i in range(5)]
JEBAK_FAIL_KEYS = [f"jebak_fail_{i}" for i in range(5)]


async def execute_utang(lender_id: int, lender_name: str, target_name: str, amount: int, lang: str, context=None) -> dict:
    lender_row = await get_user(lender_id)
    if not lender_row:
        return {"ok": False, "text": t("not_registered", lang)}

    if lender_row[2] < amount:
        balance_fmt = format_money(lender_row[2], lang)
        return {"ok": False, "text": t("insufficient_balance", lang, balance=balance_fmt)}

    if not (await check_daily_limit(lender_id, "lend", amount)):
        limit_fmt = format_money(5000, lang)
        return {"ok": False, "text": t("anti_abuse_daily_lend_limit", lang, limit=limit_fmt)}

    target = await get_or_create_by_username(target_name)
    if target["debt"] + amount > MAX_DEBT:
        debt_fmt = format_money(target["debt"], lang)
        max_debt_fmt = format_money(MAX_DEBT, lang)
        return {
            "ok": False,
            "text": t("debt_full", lang, username=target_name, debt=debt_fmt, max_debt=max_debt_fmt),
        }

    ach_msgs = await apply_utang(lender_id, target_name, amount, lang)
    await add_daily_limit(lender_id, "lend", amount)

    if target.get("is_ghost", 0) == 1:
        await add_ghost_notification(target_name, lender_name, "utang", amount)

    money_fmt = format_money(amount, lang)
    chaos_key = random.choice(UTANG_CHAOS_KEYS)
    msg = t(chaos_key, lang, lender=lender_name, debtor=f"@{target_name}", amount=money_fmt)

    target_is_ghost = target.get("is_ghost", 0) == 1
    notif_result = await send_notification(
        target_id=target["id"],
        target_lang=target.get("language", lang),
        text=t("notify_debt", target.get("language", lang), lender=lender_name, amount=money_fmt),
        lang=lang,
        username=target_name,
        context=context,
        is_ghost=target_is_ghost,
    )

    if notif_result:
        msg += f"\n\n{notif_result}"

    if ach_msgs:
        msg += "\n\n" + "\n".join(ach_msgs)

    return {"ok": True, "text": msg}


async def execute_nagih(lender_id: int, lender_name: str, target_name: str, lang: str, context=None) -> dict:
    target = await get_or_create_by_username(target_name)

    if target["debt"] <= 0:
        chaos_key = random.choice(NAGIH_FAIL_KEYS)
        msg = t(chaos_key, lang, lender=lender_name, debtor=f"@{target_name}")
        return {"ok": False, "text": msg}

    amount = target["debt"]
    money_fmt = format_money(amount, lang)

    ach_msgs = await apply_nagih(lender_id, target_name, amount, lang)

    target_is_ghost = target.get("is_ghost", 0) == 1
    notif_result = await send_notification(
        target_id=target["id"],
        target_lang=target.get("language", lang),
        text=t("notify_collect", target.get("language", lang), lender=lender_name, amount=money_fmt),
        lang=lang,
        username=target_name,
        context=context,
        is_ghost=target_is_ghost,
    )

    chaos_key = random.choice(NAGIH_SUCCESS_KEYS)
    msg = t(chaos_key, lang, lender=lender_name, debtor=f"@{target_name}", amount=money_fmt)

    if notif_result:
        msg += f"\n\n{notif_result}"
    if ach_msgs:
        msg += "\n\n" + "\n".join(ach_msgs)

    return {"ok": True, "text": msg}


async def execute_jebak(trapper_id: int, trapper_name: str, target_name: str, lang: str, context=None) -> dict:
    target = await get_or_create_by_username(target_name)

    result = calculate_trap()
    money_fmt = format_money(result["amount"], lang)
    reward_fmt = format_money(result["reward"], lang)
    penalty_fmt = format_money(result["penalty"], lang)

    if result["success"]:
        if target["debt"] + result["amount"] > MAX_DEBT:
            debt_fmt = format_money(target["debt"], lang)
            max_debt_fmt = format_money(MAX_DEBT, lang)
            return {
                "ok": False,
                "text": t("debt_full_trap", lang, username=target_name, debt=debt_fmt, max_debt=max_debt_fmt),
            }

        consequences = await apply_trap_consequences(trapper_id, target_name, result, lang)

        if target.get("is_ghost", 0) == 1:
            await add_ghost_notification(target_name, trapper_name, "jebak", result["amount"])

        target_is_ghost = target.get("is_ghost", 0) == 1
        notif_result = await send_notification(
            target_id=target["id"],
            target_lang=target.get("language", lang),
            text=t("notify_trap", target.get("language", lang), trapper=trapper_name, amount=money_fmt),
            lang=lang,
            username=target_name,
            context=context,
            is_ghost=target_is_ghost,
        )

        chaos_key = random.choice(JEBAK_SUCCESS_KEYS)
        msg = t(chaos_key, lang, trapper=trapper_name, target=f"@{target_name}", amount=money_fmt, reward=reward_fmt)

        if notif_result:
            msg += f"\n\n{notif_result}"
        if consequences.get("ach_msgs"):
            msg += "\n\n" + "\n".join(consequences["ach_msgs"])
    else:
        consequences = await apply_trap_consequences(trapper_id, target_name, result, lang)

        notif_result = await send_notification(
            target_id=target["id"],
            target_lang=target.get("language", lang),
            text=t("notify_trap_fail", target.get("language", lang), trapper=trapper_name),
            lang=lang,
            username=target_name,
            context=context,
            is_ghost=target.get("is_ghost", 0) == 1,
        )

        chaos_key = random.choice(JEBAK_FAIL_KEYS)
        msg = t(chaos_key, lang, trapper=trapper_name, target=f"@{target_name}")
        msg += f" {t('trap_penalty', lang, penalty=penalty_fmt)}"

        if notif_result:
            msg += f"\n\n{notif_result}"

    return {"ok": True, "text": msg}


async def execute_transfer(sender_id: int, sender_name: str, target_name: str, amount: int, lang: str, context=None) -> dict:
    sender_row = await get_user(sender_id)
    if not sender_row:
        return {"ok": False, "text": t("not_registered", lang)}

    if sender_row[2] < amount:
        balance_fmt = format_money(sender_row[2], lang)
        return {"ok": False, "text": t("insufficient_balance", lang, balance=balance_fmt)}

    if not (await check_daily_limit(sender_id, "transfer", amount)):
        limit_fmt = format_money(3000, lang)
        return {"ok": False, "text": t("anti_abuse_daily_transfer_limit", lang, limit=limit_fmt)}

    target = await get_or_create_by_username(target_name)

    await update_balance(sender_id, -amount)
    await update_debt_by_username(target_name, -amount)
    await add_transaction(sender_id, target_name, "transfer", amount)
    await add_daily_limit(sender_id, "transfer", amount)

    money_fmt = format_money(amount, lang)

    notif_result = await send_notification(
        target_id=target["id"],
        target_lang=target.get("language", lang),
        text=t("notify_transfer", target.get("language", lang), sender=sender_name, amount=money_fmt),
        lang=lang,
        username=target_name,
        context=context,
        is_ghost=target.get("is_ghost", 0) == 1,
    )

    msg = t("transfer_success", lang, amount=money_fmt, target=target_name)
    if notif_result:
        msg += f"\n\n{notif_result}"

    return {"ok": True, "text": msg}
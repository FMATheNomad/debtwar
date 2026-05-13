import logging
from config import GANG_CREATE_COST, GANG_TAX_RATE, GANG_REPUTATION_WIN_BONUS
from database.gang_repo import (
    create_gang, get_gang_by_user, get_gang_by_name, get_gang_members,
    join_gang, leave_gang, add_to_vault, remove_from_vault,
    add_gang_reputation, get_gang_leaderboard, get_gang_by_id,
    declare_gang_war, get_active_wars_for_gang, end_gang_war,
)
from database.user_repo import update_balance, get_user_full
from utils.translator import t
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def handle_create_gang(user_id: int, name: str, lang: str) -> dict:
    existing = await get_gang_by_user(user_id)
    if existing:
        return {"ok": False, "text": t("gang_already_in", lang)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < GANG_CREATE_COST:
        cost = format_money(GANG_CREATE_COST, lang)
        return {"ok": False, "text": t("gang_insufficient_funds", lang, cost=cost)}

    name_check = await get_gang_by_name(name)
    if name_check:
        return {"ok": False, "text": t("gang_name_exists", lang)}

    result = await create_gang(name, user_id)
    if not result["ok"]:
        return {"ok": False, "text": t("gang_create_failed", lang)}

    await update_balance(user_id, -GANG_CREATE_COST)
    return {"ok": True, "text": t("gang_created", lang, name=name, cost=format_money(GANG_CREATE_COST, lang))}


async def handle_join_gang(user_id: int, gang_name: str, lang: str) -> dict:
    existing = await get_gang_by_user(user_id)
    if existing:
        return {"ok": False, "text": t("gang_already_in", lang)}

    gang = await get_gang_by_name(gang_name)
    if not gang:
        return {"ok": False, "text": t("gang_not_found", lang)}

    result = await join_gang(gang["id"], user_id)
    if not result["ok"]:
        if result.get("error") == "full":
            return {"ok": False, "text": t("gang_full", lang)}
        return {"ok": False, "text": t("gang_join_failed", lang)}

    return {"ok": True, "text": t("gang_joined", lang, name=gang["name"])}


async def handle_leave_gang(user_id: int, lang: str) -> dict:
    gang = await get_gang_by_user(user_id)
    if not gang:
        return {"ok": False, "text": t("gang_not_in", lang)}

    result = await leave_gang(gang["id"], user_id)
    if result.get("gang_deleted"):
        return {"ok": True, "text": t("gang_left_disbanded", lang, name=gang["name"])}

    return {"ok": True, "text": t("gang_left", lang, name=gang["name"])}


async def handle_gang_info(user_id: int, lang: str) -> dict:
    gang = await get_gang_by_user(user_id)
    if not gang:
        return {"ok": False, "text": t("gang_not_in", lang)}

    members = await get_gang_members(gang["id"])
    member_list = "\n".join(
        f"{'👑' if m['role'] == 'owner' else '💼' if m['role'] == 'co_owner' else '🔹'} @{m['username']} ({m['role']})"
        for m in members
    )

    text = (
        f"🏴 *{gang['name']}*\n"
        f"👑 Owner: `{gang['owner_id']}`\n"
        f"⭐ Reputation: {gang['reputation']}\n"
        f"🏦 Vault: {gang['vault_balance']}\n"
        f"👥 Members: {gang['member_count']}/{20}\n\n"
        f"*Anggota:*\n{member_list}"
    )

    return {"ok": True, "text": text}


async def handle_gang_vault_deposit(user_id: int, amount: int, lang: str) -> dict:
    gang = await get_gang_by_user(user_id)
    if not gang:
        return {"ok": False, "text": t("gang_not_in", lang)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < amount:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user["balance"] if user else 0, lang))}

    await update_balance(user_id, -amount)
    await add_to_vault(gang["id"], amount)

    return {"ok": True, "text": t("gang_vault_deposited", lang, amount=format_money(amount, lang), name=gang["name"])}


async def handle_gang_vault_withdraw(user_id: int, amount: int, lang: str) -> dict:
    gang = await get_gang_by_user(user_id)
    if not gang:
        return {"ok": False, "text": t("gang_not_in", lang)}

    if gang["role"] not in ("owner", "co_owner"):
        return {"ok": False, "text": t("gang_owner_only", lang)}

    success = await remove_from_vault(gang["id"], amount)
    if not success:
        return {"ok": False, "text": t("gang_vault_insufficient", lang)}

    await update_balance(user_id, amount)
    return {"ok": True, "text": t("gang_vault_withdrawn", lang, amount=format_money(amount, lang), name=gang["name"])}


async def handle_gang_leaderboard(lang: str) -> str:
    rows = await get_gang_leaderboard()
    if not rows:
        return t("gang_lb_empty", lang)

    text = f"🏴 *{t('gang_lb_title', lang)}*\n\n"
    for i, g in enumerate(rows, 1):
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
        text += f"{medal} *{g['name']}* — ⭐{g['reputation']} | 👥{g['member_count']} | 🏦{g['vault_balance']}\n"

    return text


async def apply_gang_tax(user_id: int, transaction_amount: int):
    gang = await get_gang_by_user(user_id)
    if not gang:
        return
    tax = int(transaction_amount * GANG_TAX_RATE)
    if tax > 0:
        await add_to_vault(gang["id"], tax)


async def handle_gang_war_declare(user_id: int, target_gang_name: str, lang: str) -> dict:
    gang = await get_gang_by_user(user_id)
    if not gang:
        return {"ok": False, "text": t("gang_not_in", lang)}
    if gang["role"] not in ("owner", "co_owner"):
        return {"ok": False, "text": t("gang_owner_only", lang)}

    target = await get_gang_by_name(target_gang_name)
    if not target:
        return {"ok": False, "text": t("gang_not_found", lang)}
    if target["id"] == gang["id"]:
        return {"ok": False, "text": t("gang_war_self", lang)}

    result = await declare_gang_war(gang["id"], target["id"])
    if not result["ok"]:
        return {"ok": False, "text": t("gang_war_exists", lang)}

    return {"ok": True, "text": t("gang_war_declared", lang, attacker=gang["name"], defender=target["name"])}

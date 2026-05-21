import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user, get_user_full, update_balance, update_debt_by_username, add_transaction
from services.cooldown_service import check_cooldown
from services.trap_service import get_available_traps, get_trap_type, calculate_advanced_trap
from services.credit_service import modify_credit_score
from config import CREDIT_TRAP_FAIL_PENALTY
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_trap_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    traps = await get_available_traps(user.id)
    trap_list = ""
    for t_info in traps:
        trap_list += t("traps_list_item", lang,
            name=t_info['name'],
            rate=int(t_info['success_rate']*100),
            min=t_info['min_damage'],
            max=t_info['max_damage'],
            cd=t_info['cooldown_seconds'],
            cost=t_info['cost'],
        ) + "\n\n"
    text = t("traps_list_title", lang, trap_list=trap_list.strip())

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_trap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if len(context.args) < 2:
        await cmd_trap_list(update, context)
        return

    trap_id = context.args[0].lower()
    target_name = parse_mention(context.args[1])

    remaining = await check_cooldown(user.id, f"trap_{trap_id}")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s untuk trap ini.")
        return

    trap_data = await get_trap_type(trap_id)
    if not trap_data:
        await update.message.reply_text(t("trap_unknown", lang))
        return

    if target_name.lower() == uname.lower():
        await update.message.reply_text(t("self_jebak", lang))
        return

    user_data = await get_user_full(user.id)
    if not user_data or user_data["balance"] < trap_data["cost"]:
        await update.message.reply_text(t("insufficient_balance", lang, balance=format_money(user_data.get("balance", 0) if user_data else 0, lang)))
        return

    await update_balance(user.id, -trap_data["cost"])

    result = await calculate_advanced_trap(trap_data, user.id)
    if result["success"]:
        await update_debt_by_username(target_name, result["damage"])
        await add_transaction(user.id, target_name, f"trap_{trap_id}", result["damage"])

        reward = int(result["damage"] * 0.2)
        await update_balance(user.id, reward)

        text = t("traps_success", lang,
            name=result['trap_name'],
            target=target_name,
            damage=format_money(result['damage'], lang),
            reward=format_money(reward, lang),
        )
    else:
        await modify_credit_score(user.id, -CREDIT_TRAP_FAIL_PENALTY)
        text = t("traps_fail", lang, name=result['trap_name'], target=target_name)

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

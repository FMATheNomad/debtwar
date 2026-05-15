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
    text = "🪤 *Advanced Traps*\n\n"
    for t_info in traps:
        text += (
            f"• *{t_info['name']}*\n"
            f"  Rate: {int(t_info['success_rate']*100)}% | DMG: {t_info['min_damage']}-{t_info['max_damage']}\n"
            f"  CD: {t_info['cooldown_seconds']}s | Cost: {t_info['cost']}\n\n"
        )
    text += "Gunakan: /trap <nama> @username\nContoh: /trap phishing @fariz"

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

        text = (
            f"🪤 *{result['trap_name']} BERHASIL!*\n\n"
            f"🎯 Target: @{target_name}\n"
            f"💥 Damage: +{format_money(result['damage'], lang)} debt\n"
            f"💰 Reward: +{format_money(reward, lang)}"
        )
    else:
        await modify_credit_score(user.id, -CREDIT_TRAP_FAIL_PENALTY)
        text = f"❌ *{result['trap_name']} GAGAL!*\n\nJebakan tidak mempan ke @{target_name}."

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

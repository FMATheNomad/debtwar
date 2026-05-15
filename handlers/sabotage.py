import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user
from services.cooldown_service import check_cooldown
from services.sabotage_service import execute_sabotage
from config import SABOTAGE_COST
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_sabotage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    remaining = await check_cooldown(user.id, "sabotage")
    if remaining > 0:
        await update.message.reply_text(f"⏳ {t('wait', lang)} {remaining} {t('seconds', lang)} sabotage cooldown.")
        return

    if len(context.args) < 2:
        await update.message.reply_text(
            f"💣 *Sabotage System*\n\n"
            f"Gunakan: /sabotage <type> @username\n\n"
            f"Tipe:\n"
            f"• `freeze` — Freeze balance target (1 jam)\n"
            f"• `steal` — Curi uang target\n"
            f"• `block_daily` — Block daily reward target\n\n"
            f"Biaya: {format_money(SABOTAGE_COST, lang)}",
            parse_mode="Markdown",
            reply_markup=back_to_main_keyboard(lang),
        )
        return

    sabo_type = context.args[0].lower()
    target_name = parse_mention(context.args[1])

    if sabo_type not in ("freeze", "steal", "block_daily"):
        await update.message.reply_text(t("sabotage_unknown_type", lang))
        return

    if target_name.lower() == uname.lower():
        await update.message.reply_text(t("self_sabotage", lang))
        return

    from database.user_repo import get_user_full, update_balance
    attacker = await get_user_full(user.id)
    cost = SABOTAGE_COST
    if not attacker or attacker["balance"] < cost:
        await update.message.reply_text(t("insufficient_balance", lang, balance=format_money(attacker.get("balance", 0) if attacker else 0, lang)))
        return

    result = await execute_sabotage(user.id, target_name, sabo_type, lang, cost=cost)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

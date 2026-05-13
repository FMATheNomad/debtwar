import logging

from telegram import Update
from telegram.ext import ContextTypes

from database.user_repo import register_user
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention
from utils.keyboards import back_to_main_keyboard
from services.cooldown_service import check_cooldown
from services.game_logic import execute_utang
from anti_abuse.abuse_service import check_rate_limit, check_bankruptcy_block

logger = logging.getLogger(__name__)


async def cmd_utang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lender = update.effective_user
    lender_uname = get_username_or_fallback(lender)
    lang = "id" if getattr(lender, "language_code", "").startswith("id") else "en"

    await register_user(lender.id, lender_uname, lang)

    remaining = check_cooldown(lender.id, "utang")
    if remaining > 0:
        await update.message.reply_text(
            f"⏳ {t('wait', lang)} {remaining} {t('seconds', lang)} {t('before_using', lang)}"
        )
        return

    if not check_rate_limit(lender.id):
        await update.message.reply_text(t("anti_abuse_too_fast", lang))
        return

    blocked, msg = await check_bankruptcy_block(lender.id, lang)
    if blocked:
        await update.message.reply_text(msg)
        return

    if len(context.args) < 2:
        await update.message.reply_text(t("invalid_format_utang", lang))
        return

    target_name = parse_mention(context.args[0])
    try:
        amount = int(context.args[1])
    except ValueError:
        await update.message.reply_text(t("amount_must_be_number", lang))
        return

    if amount <= 0:
        await update.message.reply_text(t("amount_positive", lang))
        return

    if target_name.lower() == lender_uname.lower():
        await update.message.reply_text(t("self_utang", lang))
        return

    result = await execute_utang(lender.id, lender.first_name, target_name, amount, lang, context)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
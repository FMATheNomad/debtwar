import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import bank_menu_keyboard, back_to_main_keyboard
from database.user_repo import register_user
from services.bank_service import get_bank_info, bank_deposit, bank_withdraw

logger = logging.getLogger(__name__)


async def cmd_bank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        text = await get_bank_info(user.id, lang)
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=bank_menu_keyboard(lang))
        return

    action = context.args[0].lower()
    if action in ("deposit", "withdraw") and len(context.args) >= 2:
        try:
            amount = int(context.args[1])
        except ValueError:
            await update.message.reply_text(t("amount_must_be_number", lang))
            return

        if action == "deposit":
            result = await bank_deposit(user.id, amount, lang)
        else:
            result = await bank_withdraw(user.id, amount, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
    else:
        await update.message.reply_text(t("bank_usage", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def bank_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await query.answer()

    text = await get_bank_info(user.id, lang)
    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=bank_menu_keyboard(lang))

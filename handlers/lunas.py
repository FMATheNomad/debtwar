import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.markdown import safe
from utils.helpers import get_username_or_fallback, parse_mention
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user, get_user_full, update_balance, update_debt, get_user_by_username
from database.db import get_connection
from services.credit_service import modify_credit_score, add_repay_history
from config import CREDIT_REPAY_BONUS
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_lunas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    user_data = await get_user_full(user.id)
    if not user_data:
        await update.message.reply_text(t("not_registered", lang))
        return

    debt = user_data["debt"]
    balance = user_data["balance"]

    if debt <= 0:
        await update.message.reply_text(t("lunas_no_debt", lang))
        return

    amount = debt
    target_name = None

    if context.args:
        first = context.args[0]
        if first.startswith("@"):
            target_name = parse_mention(first)
        else:
            try:
                amount = int(first)
            except ValueError:
                await update.message.reply_text(t("lunas_amount_not_number", lang))
                return
            if len(context.args) >= 2 and context.args[1].startswith("@"):
                target_name = parse_mention(context.args[1])

    if amount <= 0:
        await update.message.reply_text(t("lunas_min_amount", lang))
        return
    if amount > debt:
        amount = debt
    if balance < amount:
        await update.message.reply_text(
            t("lunas_insufficient", lang, balance=format_money(balance, lang), amount=format_money(amount, lang)),
            reply_markup=back_to_main_keyboard(lang),
        )
        return

    await update_balance(user.id, -amount)
    await update_debt(user.id, -amount)
    await modify_credit_score(user.id, CREDIT_REPAY_BONUS)
    await add_repay_history(user.id, amount)

    paid_to = "NPC (sistem)"
    if target_name:
        target_row = await get_user_by_username(target_name)
        if target_row:
            await update_balance(target_row[0], amount)
            paid_to = f"@{safe(target_name)}"
        else:
            target_name = None

    remaining = debt - amount
    text = t("lunas_success", lang, amount=format_money(amount, lang), paid_to=paid_to, remaining=format_money(remaining, lang), bonus=CREDIT_REPAY_BONUS)
    if target_name:
        text += t("lunas_paid_to_player", lang, target=safe(target_name))
    else:
        text += t("lunas_paid_to_system", lang)

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

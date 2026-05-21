import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import casino_menu_keyboard, back_to_main_keyboard
from utils.disclaimer import casino_disclaimer
from database.user_repo import register_user
from services.cooldown_service import check_cooldown
from services.casino_service import play_slots, play_blackjack, play_roulette, get_casino_stats

logger = logging.getLogger(__name__)


async def cmd_casino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        stats = await get_casino_stats(user.id)
        text = t("casino_help", lang, total_bet=stats['total_bet'], total_won=stats['total_won'], total_lost=stats['total_lost']) + casino_disclaimer(lang)
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=casino_menu_keyboard(lang))
        return

    await update.message.reply_text(t("casino_usage", lang), parse_mode="Markdown", reply_markup=casino_menu_keyboard(lang))


async def cmd_slots(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    remaining = await check_cooldown(user.id, "slots")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s")
        return

    if not context.args:
        await update.message.reply_text(t("casino_slots_usage", lang))
        return

    try:
        bet = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t("amount_must_be_number", lang))
        return

    result = await play_slots(user.id, bet, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_blackjack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    remaining = await check_cooldown(user.id, "blackjack")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s")
        return

    if not context.args:
        await update.message.reply_text(t("casino_bj_usage", lang))
        return

    try:
        bet = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t("amount_must_be_number", lang))
        return

    result = await play_blackjack(user.id, bet, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_roulette(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    remaining = await check_cooldown(user.id, "roulette")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s")
        return

    if len(context.args) < 2:
        await update.message.reply_text(t("casino_roulette_usage", lang))
        return

    try:
        bet = int(context.args[0])
    except ValueError:
        await update.message.reply_text(t("amount_must_be_number", lang))
        return

    choice = context.args[1].lower()
    result = await play_roulette(user.id, bet, choice, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

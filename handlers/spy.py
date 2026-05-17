import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention, resolve_target
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user
from services.cooldown_service import check_cooldown
from services.spy_service import execute_spy, get_spy_stats
from config import SPY_COST
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_spy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    remaining = await check_cooldown(user.id, "spy")
    if remaining > 0:
        await update.message.reply_text(f"⏳ {t('wait', lang)} {remaining} {t('seconds', lang)} spy cooldown.")
        return

    target_name = None
    reply = update.message.reply_to_message
    if not context.args and not reply:
        stats = await get_spy_stats(user.id)
        await update.message.reply_text(
            f"🕵️ *Spy System*\n\n"
            f"Gunakan: /spy @username\n"
            f"Atau reply pesan target + /spy\n"
            f"Biaya: {format_money(SPY_COST, lang)}\n\n"
            f"📊 Spy Stats: {stats['total']} total | {stats['successes']} sukses | {stats['failures']} gagal",
            parse_mode="Markdown",
            reply_markup=back_to_main_keyboard(lang),
        )
        return

    if reply and reply.from_user and not reply.from_user.is_bot:
        tuser = reply.from_user
        if tuser.id == user.id:
            await update.message.reply_text(t("self_spy", lang))
            return
        target_name = get_username_or_fallback(tuser)
        await register_user(tuser.id, target_name, lang)
    elif context.args:
        target_name = parse_mention(context.args[0])
        if target_name.lower() == uname.lower():
            await update.message.reply_text(t("self_spy", lang))
            return
    else:
        return

    from database.user_repo import get_user_full
    spy_data = await get_user_full(user.id)
    if not spy_data or spy_data["balance"] < SPY_COST:
        await update.message.reply_text(t("insufficient_balance", lang, balance=format_money(spy_data.get("balance", 0) if spy_data else 0, lang)))
        return

    from database.user_repo import update_balance
    await update_balance(user.id, -SPY_COST)

    result = await execute_spy(user.id, target_name, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

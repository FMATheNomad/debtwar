import logging

from telegram import Update
from telegram.ext import ContextTypes

from database.user_repo import register_user
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention, resolve_target
from utils.keyboards import back_to_main_keyboard
from services.cooldown_service import check_cooldown
from services.game_logic import execute_jebak
from anti_abuse.abuse_service import check_rate_limit, check_bankruptcy_block

logger = logging.getLogger(__name__)


async def cmd_jebak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trapper = update.effective_user
    trapper_uname = get_username_or_fallback(trapper)
    lang = "id" if getattr(trapper, "language_code", "").startswith("id") else "en"

    await register_user(trapper.id, trapper_uname, lang)

    remaining = await check_cooldown(trapper.id, "jebak")
    if remaining > 0:
        await update.message.reply_text(
            f"⏳ {t('wait', lang)} {remaining} {t('seconds', lang)} {t('before_using', lang)}"
        )
        return

    if not check_rate_limit(trapper.id):
        await update.message.reply_text(t("anti_abuse_too_fast", lang))
        return

    blocked, msg = await check_bankruptcy_block(trapper.id, lang)
    if blocked:
        await update.message.reply_text(msg)
        return

    reply = update.message.reply_to_message
    target_name = None
    if reply and reply.from_user and not reply.from_user.is_bot:
        tuser = reply.from_user
        if tuser.id == trapper.id:
            await update.message.reply_text(t("self_jebak", lang))
            return
        target_name = get_username_or_fallback(tuser)
        await register_user(tuser.id, target_name, lang)
    elif context.args:
        target_name = parse_mention(context.args[0])
        if target_name.lower() == trapper_uname.lower():
            await update.message.reply_text(t("self_jebak", lang))
            return
    else:
        await update.message.reply_text(
            "Reply pesan target atau ketik:\n`/jebak @username`",
            parse_mode="Markdown",
        )
        return

    result = await execute_jebak(trapper.id, trapper.first_name, target_name, lang, context)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
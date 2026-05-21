import logging
import re
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user, set_display_name, get_user_full
from database.db import get_connection

logger = logging.getLogger(__name__)


async def cmd_setname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        full = await get_user_full(user.id)
        needs_name = full.get("needs_name", 0) if full else 1
        if needs_name:
            await update.message.reply_text(
                t("setname_welcome", lang),
                parse_mode="Markdown",
            )
        else:
            await update.message.reply_text(
                t("setname_usage", lang),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )
        return

    name = " ".join(context.args).strip()[:20]
    if not re.match(r"^[\w\s]+$", name):
        await update.message.reply_text(
            t("setname_invalid_chars", lang),
            reply_markup=back_to_main_keyboard(lang),
        )
        return

    await set_display_name(user.id, name)
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT needs_name FROM users WHERE id = ?", (user.id,)
        ) as cur:
            row = await cur.fetchone()
            was_new = row and row[0] == 1

        await conn.execute(
            "UPDATE users SET needs_name = 0 WHERE id = ?", (user.id,)
        )
        await conn.commit()
    finally:
        await conn.close()

    text = t("setname_success", lang, name=name)
    if was_new:
        text += t("setname_ready", lang)

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_to_main_keyboard(lang),
    )

import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.keyboards import back_to_main_keyboard
from services.drama_service import get_recent_drama

logger = logging.getLogger(__name__)


async def drama_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await query.answer()

    dramas = await get_recent_drama(10)
    if not dramas:
        text = f"📰 *{t('drama_title', lang)}*\n\n{t('drama_empty', lang)}"
    else:
        text = f"📰 *{t('drama_title', lang)}*\n\n"
        for d in dramas:
            ts = d.get("created_at", "???")
            text += f"📌 {d['drama_text']}\n— _{ts}_\n\n"

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

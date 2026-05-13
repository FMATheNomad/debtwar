import logging

from telegram import Update
from telegram.ext import ContextTypes

from database.user_repo import register_user
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard
from services.economy import apply_daily_reward

logger = logging.getLogger(__name__)


async def cmd_daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    await register_user(user.id, uname, lang)

    result = await apply_daily_reward(user.id, lang)
    text = result.get("message", "")

    ach_msgs = result.get("ach_msgs", [])
    if ach_msgs:
        text += "\n\n" + "\n".join(ach_msgs)

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
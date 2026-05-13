import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.keyboards import back_to_main_keyboard
from services.wanted_service import get_wanted_list, is_wanted

logger = logging.getLogger(__name__)


async def wanted_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await query.answer()

    rows = await get_wanted_list(10)
    if not rows:
        text = f"🚨 *{t('wanted_title', lang)}*\n\n{t('wanted_empty', lang)}"
    else:
        text = f"🚨 *{t('wanted_title', lang)}*\n\n"
        for i, row in enumerate(rows, 1):
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            text += t("wanted_entry", lang,
                       medal=medal,
                       name=row["username"],
                       level=row["wanted_level"],
                       bounty=row["bounty"],
                       crimes=row["total_crimes"]) + "\n"

    user_wanted = await is_wanted(user.id)
    if user_wanted:
        text += f"\n{t('wanted_you_are_wanted', lang)}"

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

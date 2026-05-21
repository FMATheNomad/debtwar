import logging

from telegram import Update
from telegram.ext import ContextTypes

from utils.translator import t
from utils.keyboards import faq_menu_keyboard, back_to_main_keyboard
from handlers.menu import _push_nav

logger = logging.getLogger(__name__)


async def cmd_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    text = (
        t("faq_title", lang)
        + t("faq_commands", lang)
        + t("faq_economy", lang)
        + t("faq_tips", lang)
    )

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def faq_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data

    sections = {
        "faq_show": "faq_title",
        "faq_howtoplay": "faq_howtoplay",
        "faq_commands": "faq_commands",
        "faq_economy": "faq_economy",
        "faq_tips": "faq_tips",
        "faq_tagging": "faq_tagging",
    }

    key = sections.get(data, "faq_title")
    if key == "faq_title":
        text = (
            t("faq_title", lang)
            + t("faq_commands", lang)
            + t("faq_economy", lang)
            + t("faq_tips", lang)
        )
    else:
        _push_nav(context, "faq_show")
        text = t(key, lang)

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=faq_menu_keyboard(lang))
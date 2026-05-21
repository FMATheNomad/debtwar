from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.translator import t


def confirm_keyboard(action_id: str, lang: str = "id") -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("confirm_yes", lang), callback_data=f"cfm_{action_id}"),
            InlineKeyboardButton(t("confirm_cancel", lang), callback_data=f"cfm_cancel_{action_id}"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

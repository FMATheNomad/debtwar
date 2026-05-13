from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def confirm_keyboard(action_id: str, lang: str = "id") -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("✅ Ya", callback_data=f"cfm_{action_id}"),
            InlineKeyboardButton("❌ Batal", callback_data=f"cfm_cancel_{action_id}"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

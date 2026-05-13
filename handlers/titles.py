import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils.translator import t
from utils.keyboards import back_to_main_keyboard
from services.title_service import get_current_title, get_title_name, get_all_unlocked_titles
from database.db import get_connection
from config import TITLES

logger = logging.getLogger(__name__)


async def titles_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data

    if data == "titles_show":
        current_id = await get_current_title(user.id)
        current_name = await get_title_name(current_id)
        unlocked = await get_all_unlocked_titles(user.id)
        unlocked_set = set(unlocked)

        text = f"👑 *Title / Rank*\n\n"
        text += f"🎯 Title Aktif: *{current_name}*\n\n"
        text += f"🏅 *Semua Title:*\n"

        for tid, tdata in TITLES.items():
            unlocked_symbol = "✅" if tid in unlocked_set else "🔒"
            active_mark = " 👈 AKTIF" if tid == current_id else ""
            text += f"{unlocked_symbol} {tdata['name']}{active_mark}\n"

        text += "\nKlik title yang sudah di-unlock untuk mengaktifkannya."

        buttons = []
        row = []
        for i, (tid, tdata) in enumerate(TITLES.items()):
            if tid in unlocked_set and tid != current_id:
                row.append(InlineKeyboardButton(tdata['name'], callback_data=f"title_select_{tid}"))
                if len(row) >= 2:
                    buttons.append(row)
                    row = []
        if row:
            buttons.append(row)
        buttons.append([InlineKeyboardButton("🔙 Kembali", callback_data="menu_main")])

        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

    elif data.startswith("title_select_"):
        title_id = data.replace("title_select_", "")
        title_name = await get_title_name(title_id)
        conn = await get_connection()
        try:
            await conn.execute(
                "UPDATE user_titles SET is_active = 0 WHERE user_id = ?", (user.id,)
            )
            await conn.execute(
                "UPDATE user_titles SET is_active = 1 WHERE user_id = ? AND title_id = ?",
                (user.id, title_id),
            )
            await conn.commit()
        finally:
            await conn.close()

        await query.edit_message_text(
            f"✅ Title aktif diubah ke: *{title_name}*",
            parse_mode="Markdown",
            reply_markup=back_to_main_keyboard(lang),
        )

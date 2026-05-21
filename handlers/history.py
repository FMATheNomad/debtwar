import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.translator import t
from utils.formatter import format_money
from database.db import get_connection
from database.user_repo import get_user

logger = logging.getLogger(__name__)

TYPE_TRANSLATION_KEYS = {
    "utang": "history_type_utang", "nagih": "history_type_nagih",
    "jebak_success": "history_type_jebak_success", "jebak_fail": "history_type_jebak_fail",
    "transfer": "history_type_transfer", "interest": "history_type_interest",
    "interest_profit": "history_type_interest_profit", "daily": "history_type_daily",
    "lootbox": "history_type_lootbox", "bank_deposit": "history_type_bank_deposit",
    "bank_withdraw": "history_type_bank_withdraw", "trap": "history_type_trap",
    "spy": "history_type_spy", "sabotage": "history_type_sabotage",
    "system": "history_type_system", "invest_buy": "history_type_invest_buy",
    "invest_sell": "history_type_invest_sell",
}


async def history_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    limit = 15
    offset = 0
    if data.startswith("history_more_"):
        offset = int(data.replace("history_more_", ""))

    user_row = await get_user(user.id)
    current_balance = user_row[2] if user_row else 0

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT type, amount, to_user, timestamp FROM transactions WHERE from_id = ? ORDER BY timestamp DESC LIMIT ? OFFSET ?",
            (user.id, limit + 1, offset),
        ) as cur:
            rows = await cur.fetchall()
    finally:
        await conn.close()

    has_more = len(rows) > limit
    rows = rows[:limit]

    text = t("history_header", lang, balance=format_money(current_balance, lang)) + "\n\n"
    if not rows:
        text += t("history_empty", lang)
    else:
        for r in rows:
            label = t(TYPE_TRANSLATION_KEYS.get(r["type"], r["type"]), lang)
            amt = format_money(r["amount"], lang)
            to = f" → @{r['to_user']}" if r["to_user"] and r["type"] not in ("interest", "daily", "system") else ""
            ts = r["timestamp"][:16] if r["timestamp"] else ""
            text += f"• {label}: {amt}{to}\n  _{ts}_\n"

    buttons = []
    if has_more:
        buttons.append([InlineKeyboardButton(t("history_more_btn", lang), callback_data=f"history_more_{offset + limit}")])
    buttons.append([InlineKeyboardButton(t("menu_btn_back", lang), callback_data="_back")])

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

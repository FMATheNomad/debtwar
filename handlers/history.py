import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.translator import t
from utils.formatter import format_money
from database.db import get_connection
from database.user_repo import get_user

logger = logging.getLogger(__name__)

TYPE_LABEL = {
    "utang": "Pinjamkan", "nagih": "Tagihan", "jebak_success": "Jebakan Berhasil",
    "jebak_fail": "Jebakan Gagal", "transfer": "Transfer", "interest": "Bunga",
    "interest_profit": "Bunga Masuk", "daily": "Daily Reward", "lootbox": "Lootbox",
    "bank_deposit": "Deposit Bank", "bank_withdraw": "Tarik Bank",
    "trap": "Trap", "spy": "Spy", "sabotage": "Sabotase", "system": "Sistem",
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

    text = (
        f"📜 *Riwayat Transaksi*\n"
        f"💰 Saldo: *{format_money(current_balance, lang)}*\n\n"
    )
    if not rows:
        text += "Belum ada transaksi."
    else:
        for r in rows:
            label = TYPE_LABEL.get(r["type"], r["type"])
            amt = format_money(r["amount"], lang)
            to = f" → @{r['to_user']}" if r["to_user"] and r["type"] not in ("interest", "daily", "system") else ""
            ts = r["timestamp"][:16] if r["timestamp"] else ""
            text += f"• {label}: {amt}{to}\n  _{ts}_\n"

    buttons = []
    if has_more:
        buttons.append([InlineKeyboardButton("⬇️ Lainnya", callback_data=f"history_more_{offset + limit}")])
    buttons.append([InlineKeyboardButton("🔙 Kembali", callback_data="menu_main")])

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

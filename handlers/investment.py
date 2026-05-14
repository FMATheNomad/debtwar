import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard
from utils.formatter import format_money
from database.user_repo import register_user
from services.investment_service import (
    get_all_prices, get_instruments_by_type, get_portfolio,
    buy_instrument, sell_instrument, INSTRUMENT_LABELS,
)

logger = logging.getLogger(__name__)


async def investment_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    itype_map = {"invest_stock": "stock", "invest_mf": "mutual_fund", "invest_bond": "bond"}
    label_map = {"invest_stock": "Saham", "invest_mf": "Reksadana", "invest_bond": "Obligasi"}

    if data == "invest_show":
        types = [
            ("Saham AS & ID", "invest_stock"),
            ("Reksadana", "invest_mf"),
            ("Obligasi", "invest_bond"),
            ("Portfolio Saya", "invest_portfolio"),
        ]
        buttons = [[InlineKeyboardButton(n, callback_data=c)] for n, c in types]
        buttons.append([InlineKeyboardButton("🔙 Kembali", callback_data="menu_main")])
        await query.edit_message_text(
            "💹 *Pasar Investasi*\n\n"
            "Pilih instrumen investasi:\n"
            "• Harga saham & reksadana berubah tiap jam\n"
            "• Obligasi return tetap\n"
            "• Terpengaruh oleh World Events!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    elif data in itype_map:
        itype = itype_map[data]
        instruments = await get_instruments_by_type(itype)
        text = f"💹 *{label_map[data]}*\n\n"
        for i in instruments:
            pct = ((i["current_price"] - i["previous_price"]) / i["previous_price"]) * 100 if i["previous_price"] else 0
            arrow = "🟢" if pct >= 0 else "🔴"
            text += f"{arrow} *{i['instrument_name']}*\n"
            text += f"   Harga: Rp{i['current_price']:,.0f} ({pct:+.2f}%)\n"
            text += f"   `/investbuy {i['instrument_type']} {i['instrument_id']} <jumlah>`\n\n"

        buttons = [[InlineKeyboardButton("🔙 Kembali", callback_data="invest_show")]]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

    elif data == "invest_portfolio":
        portfolio = await get_portfolio(user.id)
        if not portfolio:
            text = "📂 *Portfolio Kamu*\n\nKosong. Beli instrumen dulu ya!"
        else:
            text = "📂 *Portfolio Kamu*\n\n"
            total_value = 0
            total_cost = 0
            for p in portfolio:
                value = int(p["shares"] * p["current_price"])
                total_value += value
                total_cost += p["total_invested"]
                pct = ((p["current_price"] - (p["total_invested"] / p["shares"] if p["shares"] else 0)) / (p["total_invested"] / p["shares"] if p["shares"] else 1)) * 100
                arrow = "🟢" if value >= p["total_invested"] else "🔴"
                text += f"{arrow} *{p['instrument_name']}*\n"
                text += f"   Nilai: Rp{value:,} | Modal: Rp{p['total_invested']:,}\n"
                text += f"   `/investsell {p['instrument_type']} {p['instrument_id']}`\n\n"

            total_pnl = total_value - total_cost
            text += f"━━━━━━━━━━━\nTotal: Rp{total_value:,} ({'+' if total_pnl >= 0 else ''}Rp{total_pnl:,})"

        buttons = [[InlineKeyboardButton("🔙 Kembali", callback_data="invest_show")]]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))


async def cmd_invest_buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    if len(context.args) < 3:
        await update.message.reply_text("Gunakan: /investbuy <type> <id> <jumlah>\nContoh: /investbuy stock TECH 5000")
        return

    itype = context.args[0].lower()
    iid = context.args[1].upper()
    try:
        amount = int(context.args[2])
    except ValueError:
        await update.message.reply_text("Jumlah harus angka.")
        return

    if amount <= 0:
        await update.message.reply_text("Jumlah minimal 1.")
        return

    result = await buy_instrument(user.id, itype, iid, amount, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_invest_sell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    if len(context.args) < 2:
        await update.message.reply_text("Gunakan: /investsell <type> <id>\nContoh: /investsell stock TECH")
        return

    itype = context.args[0].lower()
    iid = context.args[1].upper()

    result = await sell_instrument(user.id, itype, iid, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

import os
import logging
from uuid import uuid4
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user
from services.payment_service import PRODUCTS, get_gems, add_gems, record_purchase, has_active_season_pass

logger = logging.getLogger(__name__)

DOKU_MERCHANT = os.getenv("DOKU_MERCHANT")
DOKU_SECRET = os.getenv("DOKU_SECRET")


async def cmd_shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    gems = await get_gems(user.id)
    has_sp = await has_active_season_pass(user.id)
    sp_status = t("shop_sp_active", lang) if has_sp else t("shop_sp_inactive", lang)

    text = t("shop_header", lang, gems=gems, sp_status=sp_status)

    buttons = []
    for pid, p in PRODUCTS.items():
        name = p["title"]
        price = p.get("label", f"${p['price_cents']/100:.2f}")
        if pid == "season_pass" and has_sp:
            name += " ✅"
        buttons.append([InlineKeyboardButton(f"{name} — {price}", callback_data=f"shop_{pid}")])

    buttons.append([InlineKeyboardButton("💎 Pakai Gems", callback_data="shop_gems_use")])
    buttons.append([InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main")])

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))


async def shop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    if data == "shop_gems_use":
        gems = await get_gems(user.id)
        text = t("shop_gems_info", lang, gems=gems)
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return

    product = PRODUCTS.get(data.replace("shop_", ""))
    if not product:
        return

    invoice_id = f"DW-{user.id}-{uuid4().hex[:8].upper()}"
    amount = product["price_cents"]
    context.user_data["pending_payment"] = {
        "invoice_id": invoice_id,
        "product_id": product["id"],
        "user_id": user.id,
    }

    text = t("shop_invoice", lang, id=invoice_id, product=product['title'], total=product.get('label', f'${amount/100:.2f}')) + "\n\n"

    if DOKU_MERCHANT and DOKU_SECRET:
        text += (
            "💳 *Cara Bayar via Doku:*\n"
            "1. Transfer ke VA berikut:\n"
            f"   *Bank BCA / Mandiri / BNI*\n"
            f"   *No Virtual Account: {invoice_id}*\n"
            "2. Konfirmasi dengan kirim /pay\n"
            f"3. Atau klik link berikut:\n"
        )
        buttons = [
            [InlineKeyboardButton("💳 Bayar via Doku", url=f"https://journal.doku.com/checkout?invoice={invoice_id}")],
            [InlineKeyboardButton("✅ Saya sudah bayar", callback_data="pay_confirm")],
            [InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main")],
        ]
    else:
        text += t("shop_payment_unavailable", lang)
        buttons = [[InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main")]]

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

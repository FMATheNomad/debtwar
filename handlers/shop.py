import os
import logging
from uuid import uuid4
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice
from telegram.ext import ContextTypes, PreCheckoutQueryHandler
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard
from database.user_repo import register_user
from services.payment_service import PRODUCTS, get_gems, add_gems, record_purchase, has_active_season_pass

logger = logging.getLogger(__name__)


PAYMENT_TOKEN = os.getenv("PAYMENT_TOKEN")


async def cmd_shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, get_username_or_fallback(user), lang)

    gems = await get_gems(user.id)
    has_sp = await has_active_season_pass(user.id)
    sp_status = "✅ Aktif" if has_sp else "❌ Belum"

    text = (
        f"🏪 *Debt War Shop*\n\n"
        f"💎 Gems kamu: *{gems}*\n"
        f"🎟️ Season Pass: {sp_status}\n\n"
        f"Pilih produk di bawah:\n"
    )

    buttons = []
    for pid, p in PRODUCTS.items():
        name = p["title"]
        price = p.get("label", f"${p['price_cents']/100:.2f}")
        if pid == "season_pass" and has_sp:
            name += " ✅"
        buttons.append([InlineKeyboardButton(f"{name} — {price}", callback_data=f"shop_{pid}")])

    buttons.append([InlineKeyboardButton("💎 Pakai Gems", callback_data="shop_gems_use")])
    buttons.append([InlineKeyboardButton("🔙 Kembali", callback_data="menu_main")])

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))


async def shop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    if data == "shop_gems_use":
        gems = await get_gems(user.id)
        text = (
            f"💎 *Pakai Gems*\n\n"
            f"Kamu punya *{gems} Gems*.\n\n"
            f"Gems bisa dipake buat:\n"
            f"• Legendary Lootbox — 100 Gems\n"
            f"• Instant Cooldown — 20 Gems\n"
            f"• Ganti Title — 50 Gems\n"
            f"• Season XP Boost (24h) — 40 Gems\n\n"
            f"Fitur ini akan datang segera!"
        )
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return

    product = PRODUCTS.get(data.replace("shop_", ""))
    if not product:
        return

    await query.edit_message_text(f"⏳ Memproses pembelian {product['title']}...")

    prices = [LabeledPrice(product["title"], product["price_cents"])]
    try:
        await context.bot.send_invoice(
            chat_id=user.id,
            title=product["title"],
            description=product["description"],
            payload=f"debtwar_{product['id']}_{user.id}",
            provider_token=PAYMENT_TOKEN or None,
            currency="USD",
            prices=prices,
        )
    except Exception as e:
        logger.warning(f"Stars payment error: {e}")
        await query.edit_message_text(
            "❌ Pembayaran Telegram Stars belum diaktifkan.\n\n"
            "Owner bot harus setting dulu di @BotFather:\n"
            "1. /mybots → pilih bot → Payments\n"
            "2. Enable Telegram Stars\n"
            "3. Coba lagi setelah selesai.",
            reply_markup=back_to_main_keyboard(lang),
        )


async def pre_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    if query.invoice_payload.startswith("debtwar_"):
        await query.answer(ok=True)
    else:
        await query.answer(ok=False, error_message="Invalid product")


async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    payment = update.effective_message.successful_payment
    payload = payment.invoice_payload
    parts = payload.split("_")
    if len(parts) >= 3:
        product_id = parts[1]
        charge_id = payment.telegram_payment_charge_id
        stars = payment.total_amount // 100
        await record_purchase(user.id, product_id, charge_id, stars)
        product = PRODUCTS.get(product_id)
        name = product["title"] if product else product_id
        text = f"✅ *Pembelian Berhasil!*\n\n{name} sudah aktif!"
        if product_id == "starter_pack":
            text += "\n💰 +500 coins! Cek saldo kamu."
        elif product.get("type") == "gems":
            text += f"\n💎 +{product.get('gems', 0)} Gems!"
        await update.effective_message.reply_text(text, parse_mode="Markdown")

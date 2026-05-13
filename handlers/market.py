import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import market_menu_keyboard, back_to_main_keyboard
from database.user_repo import register_user
from services.market_service import get_market_items, buy_item, get_user_items, get_active_shields

logger = logging.getLogger(__name__)


async def cmd_market(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    items = await get_market_items()
    text = "🏪 *Market / Shop*\n\n"
    for item in items:
        text += f"• *{item['name']}* — {item['price']}💰\n  `{item['id']}`\n"

    text += "\nGunakan: /buy <item_id>\nContoh: /buy shield_basic"

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=market_menu_keyboard(lang))


async def cmd_buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        await update.message.reply_text("Gunakan: /buy <item_id>")
        return

    item_id = context.args[0].lower()
    result = await buy_item(user.id, item_id, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    items = await get_user_items(user.id)
    shields = await get_active_shields(user.id)

    text = "🎒 *Inventory*\n\n"

    if items:
        text += "*Items:*\n"
        for item in items:
            text += f"• {item['name']} x{item['quantity']}\n"
    else:
        text += "*Items:* (kosong)\n"

    if shields:
        text += "\n*Active Shields:*\n"
        for s in shields:
            text += f"• {s['shield_type']} (exp: {s['expires_at']})\n"
    else:
        text += "\n*Shields:* (tidak ada)\n"

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

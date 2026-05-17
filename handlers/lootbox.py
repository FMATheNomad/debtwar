import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import lootbox_menu_keyboard, back_to_main_keyboard
from utils.disclaimer import LOOTBOX_DISCLAIMER
from database.user_repo import register_user
from services.lootbox_service import buy_lootbox, open_lootbox, get_lootbox_inventory
from config import LOOTBOX_PRICES
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_lootbox(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        inv = await get_lootbox_inventory(user.id)
        text = "🎁 *Lootbox System*\n\n"
        text += "*Harga:*\n"
        for rarity, price in LOOTBOX_PRICES.items():
            text += f"• {rarity.upper()}: {format_money(price, lang)}💰\n"

        text += "\n*Inventory:*\n"
        if inv:
            for i in inv:
                text += f"• {i['lootbox_type'].upper()} x{i['quantity']}\n"
        else:
            text += "(kosong)\n"

        text += "\nGunakan:\n/lootbox buy <rarity>\n/lootbox open <rarity>"
        text += LOOTBOX_DISCLAIMER
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=lootbox_menu_keyboard(lang))
        return

    action = context.args[0].lower()
    if len(context.args) < 2:
        await update.message.reply_text("Gunakan: /lootbox buy/open <rarity>")
        return

    rarity = context.args[1].lower()
    if rarity not in LOOTBOX_PRICES:
        await update.message.reply_text(t("lootbox_invalid_rarity", lang))
        return

    if action == "buy":
        result = await buy_lootbox(user.id, rarity, lang)
    elif action == "open":
        result = await open_lootbox(user.id, rarity, lang)
    else:
        await update.message.reply_text("Gunakan: /lootbox buy <rarity> atau /lootbox open <rarity>")
        return

    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

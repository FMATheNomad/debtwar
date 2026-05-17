import logging
from telegram import Update
from telegram.ext import ContextTypes
from config import TOKEN
from database.user_repo import create_invite_code, get_invite_owner, add_connection, get_connections, get_user_by_id
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import back_to_main_keyboard

logger = logging.getLogger(__name__)


async def cmd_invite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    code = await create_invite_code(user.id)
    bot_username = (await context.bot.get_me()).username
    link = f"https://t.me/{bot_username}?start={code}"

    text = (
        f"🔗 *Invite Link*\n\n"
        f"Kirim link ini ke temenmu:\n`{link}`\n\n"
        f"Kalo dia join, kalian otomatis terhubung!"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    conns = await get_connections(user.id)
    if not conns:
        text = (
            f"📇 *Contacts*\n\n"
            f"Kamu belum punya koneksi.\n"
            f"Gunakan /invite buat ngajak temen!"
        )
    else:
        lines = ["📇 *Contacts*\n"]
        for c in conns[:20]:
            other = await get_user_by_id(c["other_id"])
            if other:
                name = other.get("display_name") or other.get("username") or f"User#{other['id']}"
                lines.append(f"• `{other['id']}` — {name}")
        text = "\n".join(lines)

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def cmd_player(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    if not context.args:
        await update.message.reply_text("Gunakan: `/player <user_id>`", parse_mode="Markdown")
        return

    try:
        pid = int(context.args[0])
    except ValueError:
        await update.message.reply_text("User ID harus angka.")
        return

    target = await get_user_by_id(pid)
    if not target:
        await update.message.reply_text("Player tidak ditemukan.")
        return

    from utils.formatter import format_money
    name = target.get("display_name") or target.get("username") or f"User#{target['id']}"
    text = (
        f"👤 *Player Info*\n\n"
        f"ID: `{target['id']}`\n"
        f"Nama: {name}\n"
        f"Balance: {format_money(target['balance'], lang)}\n"
        f"Utang: {format_money(target['debt'], lang)}"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

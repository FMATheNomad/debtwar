import logging

from telegram import Update
from telegram.ext import ContextTypes

from config import LOGO_FILE
from database.user_repo import register_user, get_ghost_notifications, clear_ghost_notifications
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import main_menu_keyboard
from utils.formatter import format_money

logger = logging.getLogger(__name__)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from database.user_repo import get_invite_owner, accept_contact

    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    if context.args:
        param = context.args[0]
        if param.startswith("inv_"):
            inv = await get_invite_owner(param)
            if inv and inv["owner_id"] != user.id:
                await accept_contact(inv["owner_id"], user.id)

    result = await register_user(user.id, uname, lang)
    balance = result["balance"]
    debt = result["debt"]
    is_ghost = result.get("is_ghost", False)
    is_new = not is_ghost and balance == 1000 and debt == 0

    money = format_money(balance, lang)

    extra = ""
    if is_ghost and debt > 0:
        debt_money = format_money(debt, lang)
        extra = t("welcome_ghost", lang, debt=debt_money)

    ghost_notifs = await get_ghost_notifications(uname)
    if ghost_notifs:
        extra += "\n\n\U0001f514 *Aktivitas saat kamu offline:*"
        for n in ghost_notifs:
            atype = n.get("action_type", "")
            aname = n.get("from_name", "???")
            aamt = format_money(n.get("amount", 0), lang)
            if atype == "utang":
                extra += t("ghost_action_lent", lang, name=aname, amount=aamt)
            elif atype == "jebak":
                extra += t("ghost_action_trap", lang, name=aname, amount=aamt)
            else:
                extra += f"\n\U0001f4ac @{aname} melakukan {atype} ({aamt})"
        extra += t("ghost_join_cta", lang)
        await clear_ghost_notifications(uname)

    balance_label = t("welcome_new_user", lang) if is_new else t("welcome_returning_user", lang)

    welcome_text = (
        f"\U0001f44b Selamat datang, {user.first_name}!\n\n"
        f"{balance_label}: *{money}*"
        f"{extra}"
    )

    try:
        with open(LOGO_FILE, "rb") as logo:
            await update.message.reply_photo(
                photo=logo,
                caption=welcome_text,
                parse_mode="Markdown",
            )
    except FileNotFoundError:
        logger.warning(f"Logo file not found: {LOGO_FILE}")
        await update.message.reply_text(welcome_text, parse_mode="Markdown")

    await update.message.reply_text(
        t("welcome_game_desc", lang),
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(lang),
    )
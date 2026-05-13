import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention
from utils.keyboards import court_menu_keyboard, back_to_main_keyboard
from database.user_repo import register_user
from services.court_service import file_case, vote_case, get_pending_cases, resolve_case

logger = logging.getLogger(__name__)


async def cmd_court(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        cases = await get_pending_cases()
        text = "🏛️ *Pengadilan Debt War*\n\n"
        if cases:
            text += "*Kasus Tertunda:*\n"
            for c in cases:
                text += f"#{c['id']} — {c['charge']} vs @{c['defendant_name']}\n"
        else:
            text += "Tidak ada kasus tertunda.\n"
        text += "\nGunakan:\n/sue @user <tuduhan>\n/vote <case_id> <guilty/innocent>"
        await update.message.reply_text(text, reply_markup=court_menu_keyboard(lang))
        return

    action = context.args[0].lower()

    if action == "sue" and len(context.args) >= 3:
        target = parse_mention(context.args[1])
        charge = " ".join(context.args[2:])
        result = await file_case(user.id, target, charge, lang)
        await update.message.reply_text(result["text"], reply_markup=back_to_main_keyboard(lang))

    elif action == "vote" and len(context.args) >= 3:
        try:
            case_id = int(context.args[1])
        except ValueError:
            await update.message.reply_text("Case ID harus angka.")
            return
        vote = context.args[2].lower()
        if vote not in ("guilty", "innocent"):
            await update.message.reply_text("Vote: guilty atau innocent")
            return
        result = await vote_case(user.id, case_id, vote, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    else:
        await update.message.reply_text(t("court_usage", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

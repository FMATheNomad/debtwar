import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import npc_menu_keyboard, back_to_main_keyboard
from database.user_repo import register_user
from services.cooldown_service import check_cooldown
from services.npc_service import get_npc_info, interact_npc, NPCS

logger = logging.getLogger(__name__)


async def cmd_npc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        text = "🤖 *NPC Hub*\n\n"
        actions = {
            "loan_shark": "`borrow` pinjem duit, `pay` bayar utang",
            "mafia_boss": "`mission` ambil misi",
            "scammer": "`phish` tipu balik",
            "collector": "`help_collect` tagih random debtor",
        }
        for nid, ndata in NPCS.items():
            text += f"• *{ndata['name']}* — `{nid}`\n  {ndata['desc']}\n  Aksi: {actions.get(nid, '')}\n\n"
        text += "Gunakan: /npc <id> <action>\nContoh: `/npc loan_shark borrow`"
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=npc_menu_keyboard(lang))
        return

    npc_id = context.args[0].lower()
    if npc_id not in NPCS:
        await update.message.reply_text("NPC tidak dikenal. Coba: loan_shark, mafia_boss, scammer, collector")
        return

    remaining = await check_cooldown(user.id, f"npc_{npc_id}")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s")
        return

    if len(context.args) < 2:
        info = await get_npc_info(npc_id, lang)
        await update.message.reply_text(f"{info}\n\nGunakan: /npc {npc_id} <action>", parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return

    action = context.args[1].lower()
    result = await interact_npc(user.id, npc_id, action, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

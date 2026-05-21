import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import npc_menu_keyboard, back_to_main_keyboard
from database.user_repo import register_user
from services.cooldown_service import check_cooldown
from services.npc_service import get_npc_info, interact_npc, NPCS
from anti_abuse.abuse_service import check_rate_limit, check_bankruptcy_block

logger = logging.getLogger(__name__)


async def cmd_npc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        text = t("npc_hub_title", lang) + "\n\n"
        actions = {
            "loan_shark": t("npc_hub_action_loan_shark", lang),
            "mafia_boss": t("npc_hub_action_mafia_boss", lang),
            "scammer": t("npc_hub_action_scammer", lang),
            "collector": t("npc_hub_action_collector", lang),
        }
        for nid, ndata in NPCS.items():
            nname = t(f"npc_{nid}_name", lang)
            ndesc = t(f"npc_{nid}_desc", lang)
            text += f"• *{nname}* — `{nid}`\n  {ndesc}\n  Aksi: {actions.get(nid, '')}\n\n"
        text += t("npc_hub_usage", lang)
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=npc_menu_keyboard(lang))
        return

    npc_id = context.args[0].lower()
    if npc_id not in NPCS:
        await update.message.reply_text(t("npc_not_found_list", lang))
        return

    remaining = await check_cooldown(user.id, f"npc_{npc_id}")
    if remaining > 0:
        await update.message.reply_text(f"⏳ Cooldown {remaining}s")
        return

    if not check_rate_limit(user.id):
        await update.message.reply_text(t("anti_abuse_too_fast", lang))
        return

    blocked, msg = await check_bankruptcy_block(user.id, lang)
    if blocked:
        await update.message.reply_text(msg)
        return

    if len(context.args) < 2:
        info = await get_npc_info(npc_id, lang)
        await update.message.reply_text(t("npc_info_usage", lang).format(info, npc_id), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return

    action = context.args[1].lower()
    result = await interact_npc(user.id, npc_id, action, lang)
    await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.keyboards import gang_menu_keyboard, back_to_main_keyboard
from services.gang_service import (
    handle_create_gang, handle_join_gang, handle_leave_gang,
    handle_gang_info, handle_gang_vault_deposit,
    handle_gang_vault_withdraw, handle_gang_leaderboard,
    handle_gang_war_declare,
)
from database.user_repo import register_user
from handlers.menu import _push_nav

logger = logging.getLogger(__name__)


async def cmd_gang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uname = get_username_or_fallback(user)
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    await register_user(user.id, uname, lang)

    if not context.args:
        from utils.keyboards import gang_menu_keyboard
        await update.message.reply_text(
            t("gang_menu_title", lang),
            parse_mode="Markdown",
            reply_markup=gang_menu_keyboard(lang),
        )
        return

    action = context.args[0].lower()

    if action == "create" and len(context.args) >= 2:
        name = " ".join(context.args[1:])[:30]
        result = await handle_create_gang(user.id, name, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    elif action == "join" and len(context.args) >= 2:
        name = " ".join(context.args[1:])
        result = await handle_join_gang(user.id, name, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    elif action == "leave":
        result = await handle_leave_gang(user.id, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    elif action == "info":
        result = await handle_gang_info(user.id, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    elif action == "vault" and len(context.args) >= 3:
        sub = context.args[1].lower()
        try:
            amount = int(context.args[2])
        except ValueError:
            await update.message.reply_text(t("amount_must_be_number", lang))
            return
        if sub == "deposit":
            result = await handle_gang_vault_deposit(user.id, amount, lang)
        elif sub == "withdraw":
            result = await handle_gang_vault_withdraw(user.id, amount, lang)
        else:
            await update.message.reply_text(t("gang_vault_usage", lang))
            return
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    elif action == "war" and len(context.args) >= 2:
        target = " ".join(context.args[1:])
        result = await handle_gang_war_declare(user.id, target, lang)
        await update.message.reply_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

    else:
        await update.message.reply_text(t("gang_help", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))


async def gang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    def push_gang_sub():
        _push_nav(context, "gang_menu")

    if data == "gang_info":
        push_gang_sub()
        result = await handle_gang_info(user.id, lang)
    elif data == "gang_leaderboard":
        push_gang_sub()
        text = await handle_gang_leaderboard(lang)
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return
    elif data == "gang_create":
        push_gang_sub()
        await query.edit_message_text(t("gang_prompt_create", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return
    elif data == "gang_join":
        push_gang_sub()
        await query.edit_message_text(t("gang_prompt_join", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
        return
    elif data == "gang_leave":
        push_gang_sub()
        result = await handle_leave_gang(user.id, lang)
    elif data == "gang_vault":
        push_gang_sub()
        result = await handle_gang_info(user.id, lang)
        if result["ok"]:
            result["text"] += t("gang_vault_hint", lang)
    elif data == "gang_menu":
        await query.edit_message_text(t("gang_menu_title", lang), parse_mode="Markdown", reply_markup=gang_menu_keyboard(lang))
        return
    else:
        await query.edit_message_text(t("gang_menu_title", lang), parse_mode="Markdown", reply_markup=gang_menu_keyboard(lang))
        return

    await query.edit_message_text(result.get("text", t("unknown_error", lang)), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

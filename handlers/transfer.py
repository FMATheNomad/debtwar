import logging
import time

from telegram import Update
from telegram.ext import ContextTypes

from database.user_repo import register_user, get_user, update_balance, update_debt_by_username, add_transaction, check_daily_limit, add_daily_limit
from utils.translator import t
from utils.helpers import get_username_or_fallback, parse_mention, resolve_target
from utils.formatter import format_money
from utils.keyboards import back_to_main_keyboard
from services.cooldown_service import check_cooldown
from services.notification import send_notification
from anti_abuse.abuse_service import check_rate_limit, check_bankruptcy_block
from database.user_repo import get_or_create_by_username
from utils.confirm import confirm_keyboard

logger = logging.getLogger(__name__)


async def cmd_transfer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sender = update.effective_user
    sender_uname = get_username_or_fallback(sender)
    lang = "id" if getattr(sender, "language_code", "").startswith("id") else "en"

    await register_user(sender.id, sender_uname, lang)

    remaining = await check_cooldown(sender.id, "transfer")
    if remaining > 0:
        await update.message.reply_text(
            f"⏳ {t('wait', lang)} {remaining} {t('seconds', lang)} {t('before_using', lang)}"
        )
        return

    if not check_rate_limit(sender.id):
        await update.message.reply_text(t("anti_abuse_too_fast", lang))
        return

    blocked, msg = await check_bankruptcy_block(sender.id, lang)
    if blocked:
        await update.message.reply_text(msg)
        return

    target_name = None
    amount = None
    reply = update.message.reply_to_message

    if reply and reply.from_user and not reply.from_user.is_bot:
        tuser = reply.from_user
        if tuser.id == sender.id:
            await update.message.reply_text(t("self_transfer", lang))
            return
        target_name = get_username_or_fallback(tuser)
        await register_user(tuser.id, target_name, lang)
        if context.args:
            try:
                amount = int(context.args[0])
            except ValueError:
                await update.message.reply_text(t("amount_must_be_number", lang))
                return
    elif len(context.args) >= 2:
        target_name = parse_mention(context.args[0])
        if target_name.lower() == sender_uname.lower():
            await update.message.reply_text(t("self_transfer", lang))
            return
        try:
            amount = int(context.args[1])
        except ValueError:
            await update.message.reply_text(t("amount_must_be_number", lang))
            return
    else:
        await update.message.reply_text(
            "Reply pesan target + jumlah, atau ketik:\n`/transfer @username <jumlah>`",
            parse_mode="Markdown",
        )
        return

    if amount <= 0:
        await update.message.reply_text(t("amount_positive", lang))
        return

    sender_row = await get_user(sender.id)
    if not sender_row:
        await update.message.reply_text(t("not_registered", lang))
        return

    if sender_row[2] < amount:
        balance_fmt = format_money(sender_row[2], lang)
        await update.message.reply_text(t("insufficient_balance", lang, balance=balance_fmt))
        return

    if not (await check_daily_limit(sender.id, "transfer", amount)):
        limit_fmt = format_money(3000, lang)
        await update.message.reply_text(t("anti_abuse_daily_transfer_limit", lang, limit=limit_fmt))
        return

    target = await get_or_create_by_username(target_name)
    money_fmt = format_money(amount, lang)

    if amount > 1000:
        confirm_id = f"transfer_{sender.id}_{int(time.time())}"
        context.user_data["pending_action"] = {
            "id": confirm_id,
            "from_id": sender.id,
            "to_id": target["id"],
            "to_name": target_name,
            "amount": amount,
            "amount_formatted": money_fmt,
        }
        await update.message.reply_text(
            f"⚠️ *Konfirmasi Transfer*\n\n"
            f"Transfer {money_fmt} ke @{target_name}?\n\n"
            f"Jumlah besar ({money_fmt}) perlu konfirmasi.",
            parse_mode="Markdown",
            reply_markup=confirm_keyboard(confirm_id, lang),
        )
        return

    await update_balance(sender.id, -amount)
    await update_debt_by_username(target_name, -amount)
    await add_transaction(sender.id, target_name, "transfer", amount)
    await add_daily_limit(sender.id, "transfer", amount)

    notif_result = await send_notification(
        target_id=target["id"],
        target_lang=target.get("language", lang),
        text=t("notify_transfer", target.get("language", lang), sender=sender_uname, amount=money_fmt),
        lang=lang,
        username=target_name,
        context=context,
    )

    msg = t("transfer_success", lang, amount=money_fmt, target=target_name)
    if notif_result:
        msg += f"\n\n{notif_result}"

    await update.message.reply_text(msg, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
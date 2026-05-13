import logging

from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from database.user_repo import get_user, get_user_full, get_user_achievements, get_display_name
from database.db import get_connection
from utils.translator import t
from utils.helpers import get_username_or_fallback
from utils.formatter import format_money
from utils.keyboards import profile_menu_keyboard
from services.title_service import get_current_title, get_title_name
from services.credit_service import get_credit_score
from services.stats_service import record_balance_peak
from config import ACHIEVEMENTS

logger = logging.getLogger(__name__)

ACH_EMOJI = {
    "first_trap": "\U0001f3c5",
    "first_collect": "\U0001f3c6",
    "debt_collector_1000": "\U0001f4b0",
    "debt_collector_5000": "\U0001f988",
    "big_lender_1000": "\U0001f4b8",
    "trap_master_10": "\U0001faa8",
    "bankrupt_once": "\U0001f480",
    "streak_7": "\U0001f525",
}


async def build_profile_text(user, lang: str):
    row = await get_user(user.id)
    if not row:
        return t("not_registered", lang), profile_menu_keyboard(lang)

    _, username, balance, debt, db_lang = row
    lang = db_lang if db_lang else lang

    full = await get_user_full(user.id)

    money_balance = format_money(balance, lang)
    money_debt = format_money(debt, lang)

    title_id = await get_current_title(user.id)
    title_name = await get_title_name(title_id)
    credit = await get_credit_score(user.id)
    await record_balance_peak(user.id, balance)
    display_name = await get_display_name(user.id, user.first_name or "Player")

    text = (
        f"{t('profile_title', lang)}\n\n"
        f"👑 `{title_name}`\n"
        f"💳 Credit: *{credit}*\n"
        f"📛 Nama: `{display_name}`\n"
        f"{t('profile_id', lang)} : `{user.id}`\n"
        f"📌 Tag: `@{username}`\n"
        f"{t('profile_balance', lang)}    : *{money_balance}*\n"
        f"{t('profile_debt', lang)}      : *{money_debt}*"
    )

    if full:
        text += f"\n\n\U0001f4ca *{t('profile_stats', lang)}*"
        text += f"\n{t('profile_total_lent', lang)}: {format_money(full.get('total_lent', 0), lang)}"
        text += f"\n{t('profile_total_collected', lang)}: {format_money(full.get('total_collected', 0), lang)}"
        text += f"\n{t('profile_traps_set', lang)}: {full.get('traps_set', 0)}"
        text += f"\n{t('profile_traps_successful', lang)}: {full.get('traps_successful', 0)}"
        text += f"\n{t('profile_daily_streak', lang)}: {full.get('daily_streak', 0)}\U0001f525"
        if full.get("bankrupt_count", 0) > 0:
            text += f"\n{t('profile_bankrupt_count', lang)}: {full.get('bankrupt_count', 0)}\U0001f480"

    conn = await get_connection()
    try:
        async with conn.execute(
            """SELECT to_user,
                      COALESCE(SUM(CASE WHEN type='utang' THEN amount ELSE 0 END), 0)
                      - COALESCE(SUM(CASE WHEN type='nagih' THEN amount ELSE 0 END), 0) as outstanding
               FROM transactions WHERE from_id = ? AND type IN ('utang','nagih')
               GROUP BY to_user HAVING outstanding > 0
               ORDER BY outstanding DESC LIMIT 3""",
            (user.id,),
        ) as cur:
            lent_to = await cur.fetchall()
        async with conn.execute(
            """SELECT from_id,
                      COALESCE(SUM(CASE WHEN type='utang' THEN amount ELSE 0 END), 0)
                      - COALESCE(SUM(CASE WHEN type='nagih' THEN amount ELSE 0 END), 0) as outstanding
               FROM transactions WHERE to_user = ? AND type IN ('utang','nagih')
               GROUP BY from_id HAVING outstanding > 0
               ORDER BY outstanding DESC LIMIT 3""",
            (username,),
        ) as cur:
            borrowed_from = await cur.fetchall()
    finally:
        await conn.close()

    if borrowed_from:
        text += "\n\n📌 *Diutangin oleh:*"
        for row in borrowed_from:
            text += f"\n🔹 `{row['from_id']}` — {format_money(row['outstanding'], lang)}"
    if lent_to:
        text += "\n\n📌 *Kamu ngutangin:*"
        for row in lent_to:
            text += f"\n🔹 `@{row['to_user']}` — {format_money(row['outstanding'], lang)}"

    ach_list = await get_user_achievements(user.id)
    if ach_list:
        text += f"\n\n\U0001f3c6 *{t('profile_achievements', lang)}*"
        for ach_id in ach_list:
            emoji = ACH_EMOJI.get(ach_id, "\U0001f3c5")
            ach_data = ACHIEVEMENTS.get(ach_id, {})
            ach_key = f"ach_{ach_data.get('key', ach_id)}"
            ach_name = t(ach_key, lang).split("\n")[0] if "\n" in t(ach_key, lang) else t(ach_key, lang)
            if ach_name.startswith("ach_"):
                ach_name = ach_id.replace("_", " ")
            text += f"\n{emoji} {ach_name}"

    return text, profile_menu_keyboard(lang)


async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    text, keyboard = await build_profile_text(user, lang)
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=keyboard)
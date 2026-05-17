import logging
import re as _re

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from utils.translator import t
from utils.markdown import safe
from utils.keyboards import leaderboard_menu_keyboard, back_to_main_keyboard
from database.user_repo import get_leaderboard, get_leaderboard_chaos_detail

logger = logging.getLogger(__name__)


import re


def _lb_name(row: dict) -> str:
    dn = row.get("display_name") or ""
    un = row.get("username") or ""
    if dn:
        return safe(dn)
    if un and not _re.search(r"_\d{5,}$", un):
        return f"@{safe(un)}"
    return "Player"


async def cmd_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    text = f"{t('leaderboard_title', lang)}\n\n"
    text += f"🔹 {t('leaderboard_richest', lang)}\n"
    rows = await get_leaderboard("richest", 5)
    if rows:
        for i, row in enumerate(rows, 1):
            m = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            text += f"{m} {_lb_name(row)} — {row['balance']}\n"
    else:
        text += f"{t('leaderboard_empty', lang)}\n"

    text += f"\n🔹 {t('leaderboard_debt', lang)}\n"
    rows = await get_leaderboard("debt", 5)
    if rows:
        for i, row in enumerate(rows, 1):
            m = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            text += f"{m} {_lb_name(row)} — {row['debt']}\n"
    else:
        text += f"{t('leaderboard_empty', lang)}\n"

    text += f"\n🔹 {t('leaderboard_chaos', lang)}\n"
    rows = await get_leaderboard("chaos", 5)
    if rows:
        for i, row in enumerate(rows, 1):
            m = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
            text += f"{m} {_lb_name(row)} — {row['chaos_score']}\n"
    else:
        text += f"{t('leaderboard_empty', lang)}\n"

    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=leaderboard_menu_keyboard(lang))


async def lb_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    data = query.data
    await query.answer()

    back_kb = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Kembali", callback_data="leaderboard_show")]])

    try:
        valid = {"lb_richest", "lb_debt", "lb_chaos", "lb_chaos_detail"}
        if data not in valid:
            await query.edit_message_text("Leaderboard gak ditemukan.", reply_markup=back_kb)
            return

        if data == "lb_chaos_detail":
            rows = await get_leaderboard_chaos_detail(10)
            lines = [t("leaderboard_chaos_detail_title", lang)]
            if not rows:
                lines.append(t("leaderboard_empty", lang))
            else:
                for i, row in enumerate(rows, 1):
                    medal = {1: "\U0001f947", 2: "\U0001f948", 3: "\U0001f949"}.get(i, f"{i}.")
                    name = _lb_name(row)
                    score = row.get("chaos_score", 0)
                    t_set = row.get("traps_set", 0)
                    t_ok = row.get("traps_successful", 0)
                    lent = row.get("total_lent", 0)
                    col = row.get("total_collected", 0)
                    ach = row.get("achievements", 0)
                    titles = row.get("titles", 0)
                    active_title = row.get("active_title", "")
                    title_str = f" 👑 {active_title}" if active_title else ""
                    lines.append(
                        f"{medal} {name}{title_str}\n"
                        f"   Score: {score} | Trap: {t_set}/{t_ok}\n"
                        f"   Lend: {lent} | Collect: {col} | Ach: {ach} | Titles: {titles}\n"
                    )
            await query.edit_message_text("".join(lines), parse_mode="Markdown", reply_markup=back_kb)
            return

        category = data.replace("lb_", "")
        rows = await get_leaderboard(category, 10)
        lines = []
        titles_map = {"richest": "leaderboard_richest", "debt": "leaderboard_debt", "chaos": "leaderboard_chaos"}
        title_key = titles_map.get(category, "")
        if title_key:
            lines.append(f"{t(title_key, lang)}")

        if not rows:
            lines.append(t("leaderboard_empty", lang))
        else:
            for i, row in enumerate(rows, 1):
                keys = list(row.keys())
                val_keys = [k for k in keys if k not in ("username", "display_name")]
                val = row.get(val_keys[0], 0) if val_keys else 0
                medal = {1: "\U0001f947", 2: "\U0001f948", 3: "\U0001f949"}.get(i, f"{i}.")
                lines.append(f"{medal} {_lb_name(row)} \u2014 {val}")

        await query.edit_message_text("\n".join(lines), parse_mode="Markdown", reply_markup=back_kb)

    except Exception as e:
        logger.error(f"LB callback error: {e}")
        await query.edit_message_text("⚠️ Error memuat leaderboard.", reply_markup=back_kb)
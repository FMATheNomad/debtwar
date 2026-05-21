import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.keyboards import back_to_main_keyboard
from database.user_repo import get_user_full
from services.stats_service import get_stat_summary, get_peak_balance, record_balance_peak
from services.title_service import get_current_title, get_title_name

logger = logging.getLogger(__name__)


async def stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    full = await get_user_full(user.id)
    if not full:
        await query.edit_message_text(t("not_registered", lang), reply_markup=back_to_main_keyboard(lang))
        return

    current_balance = full.get("balance", 0)
    await record_balance_peak(user.id, current_balance)
    peak = await get_peak_balance(user.id)
    title_id = await get_current_title(user.id)
    title_name = await get_title_name(title_id)

    traps_set = full.get("traps_set", 0)
    traps_ok = full.get("traps_successful", 0)
    trap_rate = f"{int(traps_ok / traps_set * 100)}%" if traps_set > 0 else "0%"
    chaos = traps_set + full.get("total_lent", 0) // 100 + full.get("total_collected", 0) // 100

    text = (
        f"{t('stats_title', lang)}\n\n"
        f"{t('stats_title_label', lang, title=title_name)}\n"
        f"{t('stats_chaos_score_label', lang, score=chaos)}\n\n"
        f"{t('stats_total_lent_label', lang, amount=full.get('total_lent', 0))}\n"
        f"{t('stats_total_collected_label', lang, amount=full.get('total_collected', 0))}\n"
        f"{t('stats_traps_label', lang, count=traps_set, rate=trap_rate)}\n"
        f"{t('stats_peak_balance_label', lang, amount=peak)}\n"
        f"{t('stats_bankruptcies_label', lang, count=full.get('bankrupt_count', 0))}\n"
        f"{t('stats_daily_claimed_label', lang, count=full.get('total_daily_claimed', 0))}\n"
        f"{t('stats_daily_streak_label', lang, days=full.get('daily_streak', 0))}\n"
    )

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

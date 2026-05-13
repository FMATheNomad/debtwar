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
        f"📊 *Statistik Pemain*\n\n"
        f"👑 Title: *{title_name}*\n"
        f"💀 Chaos Score: *{chaos}*\n\n"
        f"💰 Total Pinjaman: {full.get('total_lent', 0)}\n"
        f"💸 Total Tagihan: {full.get('total_collected', 0)}\n"
        f"🪤 Jebakan: {traps_set} ({trap_rate} sukses)\n"
        f"🏔️ Saldo Tertinggi: {peak}\n"
        f"💀 Bangkrut: {full.get('bankrupt_count', 0)}x\n"
        f"🎁 Daily Diklaim: {full.get('total_daily_claimed', 0)}x\n"
        f"🔥 Daily Streak: {full.get('daily_streak', 0)} hari\n"
    )

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

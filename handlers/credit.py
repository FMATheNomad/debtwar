import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.translator import t
from utils.keyboards import back_to_main_keyboard
from services.credit_service import get_credit_score, get_credit_tier
from database.user_repo import get_user_full

logger = logging.getLogger(__name__)


async def credit_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    score = await get_credit_score(user.id)
    tier = await get_credit_tier(user.id)
    full = await get_user_full(user.id)

    text = (
        f"💳 *Credit Score*\n\n"
        f"📊 Skor: *{score}/1000*\n"
        f"🏅 Tier: *{tier['tier']} ({tier['label']})*\n\n"
        f"🔹 Mod Bunga: {tier['multipliers']['interest']}x\n"
        f"🔹 Mod Jebakan: {tier['multipliers']['trap_success']}x\n"
        f"🔹 Mod Spy: {tier['multipliers']['spy_success']}x\n\n"
    )

    if full:
        text += (
            f"✅ Total Dibayar: {full.get('total_repaid', 0)}\n"
            f"❌ Total Gagal Bayar: {full.get('total_defaulted', 0)}\n"
        )

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

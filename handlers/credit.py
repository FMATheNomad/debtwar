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
        f"{t('credit_title', lang)}\n\n"
        f"{t('credit_skor_label', lang, score=score)}\n"
        f"{t('credit_tier_label', lang, tier=tier['tier'], label=tier['label'])}\n\n"
        f"{t('credit_mod_interest', lang, value=tier['multipliers']['interest'])}\n"
        f"{t('credit_mod_trap', lang, value=tier['multipliers']['trap_success'])}\n"
        f"{t('credit_mod_spy', lang, value=tier['multipliers']['spy_success'])}\n\n"
    )

    if full:
        text += (
            f"{t('credit_repaid_total', lang, amount=full.get('total_repaid', 0))}\n"
            f"{t('credit_defaulted_total', lang, amount=full.get('total_defaulted', 0))}\n"
        )

    await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

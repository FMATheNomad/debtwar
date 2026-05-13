import logging
from datetime import datetime
from database.db import get_connection
from database.user_repo import get_all_debtors, update_debt, update_balance, add_transaction, get_user_full
from config import INTEREST_RATE, INTEREST_MIN_AMOUNT
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)


async def get_lenders(debtor_username: str) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT from_id, SUM(amount) as total FROM transactions WHERE to_user = ? AND type = 'utang' GROUP BY from_id",
            (debtor_username,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()


async def process_interest_for_all():
    debtors = await get_all_debtors()
    now = datetime.now()
    processed = 0

    for debtor in debtors:
        user_id = debtor["id"]
        debt = debtor["debt"]
        lang = debtor.get("language", "en")
        username = debtor.get("username", "")

        user_data = await get_user_full(user_id)
        if not user_data:
            continue

        last_daily_str = user_data.get("last_daily")
        if not last_daily_str:
            continue

        try:
            last_daily = datetime.strptime(last_daily_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue

        hours_passed = (now - last_daily).total_seconds() / 3600
        if hours_passed < 24:
            continue

        days_passed = int(hours_passed / 24)
        interest = int(debt * INTEREST_RATE) * days_passed

        if interest < INTEREST_MIN_AMOUNT:
            continue

        await update_debt(user_id, interest)
        await add_transaction(user_id, "system", "interest", interest)

        lenders = await get_lenders(username)
        if lenders:
            total_lent = sum(l["total"] for l in lenders)
            for l in lenders:
                share = int(interest * l["total"] / total_lent) if total_lent > 0 else 0
                if share > 0:
                    await update_balance(l["from_id"], share)
                    await add_transaction(l["from_id"], username, "interest_profit", share)

        interest_fmt = format_money(interest, lang)
        msg = t("interest_notify", lang, percent="5%", amount=interest_fmt)

        try:
            from config import TOKEN
            from telegram import Bot
            bot = Bot(token=TOKEN)
            await bot.send_message(chat_id=user_id, text=msg, parse_mode="Markdown")
        except Exception:
            pass

        processed += 1

    if processed > 0:
        logger.info(f"Processed interest for {processed} users")
    return processed

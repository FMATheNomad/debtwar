import logging
from datetime import datetime, timedelta
from config import (
    MAX_DEBT, INITIAL_BALANCE, BANKRUPTCY_THRESHOLD,
    TRAP_DEBT_MIN, TRAP_DEBT_MAX, TRAP_SUCCESS_RATE, TRAP_REWARD_RATE,
    TRAP_COST_MIN, TRAP_COST_MAX,
    DAILY_REWARD_MIN, DAILY_REWARD_MAX, DAILY_STREAK_BONUS,
    INTEREST_RATE, INTEREST_MIN_AMOUNT,
    ACHIEVEMENTS,
)
from database.user_repo import (
    get_user_full, update_balance, set_balance, update_debt,
    update_debt_by_username, update_user_stat, set_user_field,
    add_transaction, unlock_achievement,
)
from utils.formatter import format_money
from utils.translator import t
from services.credit_service import modify_credit_score, add_default_history
from config import CREDIT_REPAY_BONUS, CREDIT_DEFAULT_PENALTY, CREDIT_BANKRUPTCY_PENALTY, CREDIT_TRAP_FAIL_PENALTY

logger = logging.getLogger(__name__)


def calculate_trap() -> dict:
    import random
    success = random.random() < TRAP_SUCCESS_RATE
    amount = random.randint(TRAP_DEBT_MIN, TRAP_DEBT_MAX)
    penalty = random.randint(TRAP_COST_MIN, TRAP_COST_MAX)
    reward = int(amount * TRAP_REWARD_RATE) if success else 0
    return {
        "success": success,
        "amount": amount,
        "penalty": penalty,
        "reward": reward,
    }


async def apply_trap_consequences(trapper_id: int, target_name: str, result: dict, lang: str):
    from utils.helpers import get_username_or_fallback
    from utils.translator import t
    from database.user_repo import get_user_by_username

    amount = result["amount"]
    penalty = result["penalty"]
    reward = result["reward"]
    success = result["success"]

    if success:
        await update_debt_by_username(target_name, amount)
        target_row = await get_user_by_username(target_name)
        if target_row:
            target_id = target_row[0]
            target_balance = target_row[2]
            actual_reward = min(reward, target_balance)
            if actual_reward > 0:
                await update_balance(target_id, -actual_reward)
                await update_balance(trapper_id, actual_reward)
        await update_user_stat(trapper_id, "traps_set")
        await update_user_stat(trapper_id, "traps_successful")
        await add_transaction(trapper_id, target_name, "jebak_success", amount)

        ach_unlocked = await unlock_achievement(trapper_id, "first_trap")
        ach_msgs = []
        if ach_unlocked:
            ach_msgs.append(t("ach_first_trap", lang))

        user_data = await get_user_full(trapper_id)
        if user_data and user_data.get("traps_successful", 0) >= 10:
            if await unlock_achievement(trapper_id, "trap_master_10"):
                ach_msgs.append(t("ach_trap_master", lang))

        return {"success": True, "ach_msgs": ach_msgs}
    else:
        await update_balance(trapper_id, -penalty)
        await update_user_stat(trapper_id, "traps_set")
        await add_transaction(trapper_id, target_name, "jebak_fail", penalty)
        await modify_credit_score(trapper_id, -CREDIT_TRAP_FAIL_PENALTY)
        return {"success": False}


async def apply_utang(lender_id: int, target_name: str, amount: int, lang: str):
    from utils.helpers import get_username_or_fallback

    await update_balance(lender_id, -amount)
    await update_debt_by_username(target_name, amount)
    await update_user_stat(lender_id, "total_lent", amount)
    await add_transaction(lender_id, target_name, "utang", amount)

    from services.stats_service import record_stat
    await record_stat(lender_id, "lent", amount)

    ach_msgs = []
    user_data = await get_user_full(lender_id)
    if user_data:
        total_lent = user_data.get("total_lent", 0)
        if total_lent >= 1000:
            if await unlock_achievement(lender_id, "big_lender_1000"):
                ach_msgs.append(t("ach_big_lender", lang))

    from services.title_service import update_title
    await update_title(lender_id)

    return ach_msgs


async def apply_nagih(lender_id: int, target_name: str, amount: int, lang: str):
    await update_debt_by_username(target_name, -amount)
    await update_balance(lender_id, amount)
    await update_user_stat(lender_id, "total_collected", amount)
    await add_transaction(lender_id, target_name, "nagih", amount)
    await modify_credit_score(lender_id, CREDIT_REPAY_BONUS)

    ach_msgs = []
    if await unlock_achievement(lender_id, "first_collect"):
        ach_msgs.append(t("ach_first_collect", lang))

    user_data = await get_user_full(lender_id)
    if user_data:
        total_collected = user_data.get("total_collected", 0)
        if total_collected >= 1000:
            if await unlock_achievement(lender_id, "debt_collector_1000"):
                ach_msgs.append(t("ach_debt_collector", lang))
        if total_collected >= 5000:
            if await unlock_achievement(lender_id, "debt_collector_5000"):
                ach_msgs.append(t("ach_debt_collector_5000", lang))

    from services.title_service import update_title
    await update_title(lender_id)

    return ach_msgs


async def apply_transfer(sender_id: int, target_name: str, amount: int, lang: str):
    await update_balance(sender_id, -amount)
    await update_debt_by_username(target_name, -amount)
    await add_transaction(sender_id, target_name, "transfer", amount)


async def apply_daily_reward(user_id: int, lang: str) -> dict:
    import random
    from datetime import date
    from utils.helpers import format_remaining_time
    from config import CREDIT_DAILY_ACTIVITY_BONUS

    user_data = await get_user_full(user_id)
    if not user_data:
        return {"success": False, "message": t("not_registered", lang)}

    now = datetime.now()
    last_daily_str = user_data.get("last_daily")

    if last_daily_str:
        try:
            last_daily = datetime.strptime(last_daily_str, "%Y-%m-%d %H:%M:%S")
            if (now - last_daily).total_seconds() < 86400:
                remaining = 86400 - (now - last_daily).total_seconds()
                return {
                    "success": False,
                    "message": t("daily_already_claimed", lang, time=format_remaining_time(int(remaining))),
                }
        except ValueError:
            pass

    streak = user_data.get("daily_streak", 0)
    if last_daily_str:
        try:
            last_date = datetime.strptime(last_daily_str, "%Y-%m-%d %H:%M:%S").date()
            if (date.today() - last_date).days > 1:
                streak = 0
        except ValueError:
            streak = 0

    new_streak = streak + 1
    base_reward = random.randint(DAILY_REWARD_MIN, DAILY_REWARD_MAX)
    bonus = min(new_streak * DAILY_STREAK_BONUS, 200)
    total_reward = base_reward + bonus

    await update_balance(user_id, total_reward)
    await set_user_field(user_id, "daily_streak", new_streak)
    await set_user_field(user_id, "last_daily", now.strftime("%Y-%m-%d %H:%M:%S"))
    await update_user_stat(user_id, "total_daily_claimed")
    await modify_credit_score(user_id, CREDIT_DAILY_ACTIVITY_BONUS)

    msg = t("daily_success", lang, amount=format_money(total_reward, lang), streak=new_streak)
    if bonus > 0 and new_streak > 1:
        msg += t("daily_streak_bonus", lang, bonus=format_money(bonus, lang))

    ach_msgs = []
    if new_streak >= 7:
        if await unlock_achievement(user_id, "streak_7"):
            ach_msgs.append(t("ach_streak_7", lang))

    return {"success": True, "message": msg, "ach_msgs": ach_msgs, "streak": new_streak}


async def check_and_apply_interest(user_id: int, lang: str) -> list:
    user_data = await get_user_full(user_id)
    if not user_data or user_data["debt"] <= 0:
        return []

    from datetime import datetime
    last_interest_str = user_data.get("last_daily")
    if not last_interest_str:
        return []

    try:
        last_interest = datetime.strptime(last_interest_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return []

    now = datetime.now()
    hours_passed = (now - last_interest).total_seconds() / 3600
    if hours_passed < 1:
        return []

    debt = user_data["debt"]
    interest = int(debt * INTEREST_RATE * (hours_passed / 24))
    if interest < INTEREST_MIN_AMOUNT:
        return []

    await update_debt(user_id, interest)
    await add_transaction(user_id, "system", "interest", interest)

    msg = t("interest_notify", lang, percent="5%", amount=format_money(interest, lang))
    return [msg]


async def check_bankruptcy(user_id: int, lang: str) -> bool:
    user_data = await get_user_full(user_id)
    if not user_data:
        return False

    if user_data["debt"] >= BANKRUPTCY_THRESHOLD:
        from datetime import timedelta
        await set_balance(user_id, 0)
        await set_user_field(user_id, "debt", 0)
        await update_user_stat(user_id, "bankrupt_count")
        await set_user_field(user_id, "is_bankrupt", 1)
        bankrupt_until = datetime.now() + timedelta(hours=24)
        await set_user_field(user_id, "bankruptcy_date", bankrupt_until.strftime("%Y-%m-%d %H:%M:%S"))
        await modify_credit_score(user_id, -CREDIT_BANKRUPTCY_PENALTY)
        await add_default_history(user_id, BANKRUPTCY_THRESHOLD)

        if await unlock_achievement(user_id, "bankrupt_once"):
            pass

        from services.title_service import update_title
        await update_title(user_id)

        return True
    return False


async def check_bankruptcy_status(user_id: int) -> tuple:
    user_data = await get_user_full(user_id)
    if not user_data or not user_data.get("is_bankrupt"):
        return False, None

    from datetime import datetime
    bankrupt_str = user_data.get("bankruptcy_date")
    if not bankrupt_str:
        return False, None

    try:
        bankrupt_until = datetime.strptime(bankrupt_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return False, None

    now = datetime.now()
    if now >= bankrupt_until:
        await set_user_field(user_id, "is_bankrupt", 0)
        await set_user_field(user_id, "bankruptcy_date", None)
        return False, None

    return True, bankrupt_until


async def get_chaos_message_key(prefix: str, count: int) -> str:
    return f"{prefix}_{random.randint(0, count - 1)}" if count > 0 else prefix


async def trigger_random_event(lang: str = "en") -> dict:
    """5% chance random economy event. Returns event dict or None."""
    import random
    if random.random() >= 0.05:
        return None

    from database.user_repo import get_all_debtors
    from config import EVENT_CRISIS_MULTIPLIER, EVENT_BOOM_MULTIPLIER, EVENT_GIFT_AMOUNT

    event_type = random.choice(["crisis", "boom", "gift"])

    if event_type == "crisis":
        debtors = await get_all_debtors()
        for d in debtors:
            increase = int(d["debt"] * EVENT_CRISIS_MULTIPLIER)
            if increase > 0:
                await update_debt(d["id"], increase)
        return {
            "type": "crisis",
            "message": t("event_crisis", lang, percent="10%"),
        }
    elif event_type == "boom":
        debtors = await get_all_debtors()
        for d in debtors:
            bonus = int(d["debt"] * EVENT_BOOM_MULTIPLIER)
            if bonus > 0:
                await update_balance(d["id"], bonus)
        return {
            "type": "boom",
            "message": t("event_boom", lang, percent="5%"),
        }
    else:
        return {
            "type": "gift",
            "message": t("event_gift", lang, amount=format_money(EVENT_GIFT_AMOUNT, lang)),
        }
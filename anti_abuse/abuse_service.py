import logging
from services.notification import send_notification

logger = logging.getLogger(__name__)

_transaction_tracker = {}


def check_rate_limit(user_id: int) -> bool:
    import time
    now = time.time()
    timestamps = _transaction_tracker.get(user_id, [])
    timestamps = [t for t in timestamps if now - t < 60]
    if len(timestamps) >= 5:
        return False
    timestamps.append(now)
    _transaction_tracker[user_id] = timestamps
    return True


async def check_bankruptcy_block(user_id: int, lang: str) -> tuple:
    from datetime import datetime
    from database.user_repo import get_user_full
    from config import BANKRUPTCY_COOLDOWN_HOURS

    user_data = await get_user_full(user_id)
    if not user_data:
        return False, None

    if user_data.get("is_bankrupt"):
        bankrupt_str = user_data.get("bankruptcy_date")
        if bankrupt_str:
            try:
                bankrupt_until = datetime.strptime(bankrupt_str, "%Y-%m-%d %H:%M:%S")
                from datetime import datetime
                now = datetime.now()
                if now < bankrupt_until:
                    from utils.helpers import format_remaining_time
                    remaining = int((bankrupt_until - now).total_seconds())
                    return True, t("anti_abuse_bankrupt", lang, date=format_remaining_time(remaining))
                else:
                    from database.user_repo import set_user_field
                    await set_user_field(user_id, "is_bankrupt", 0)
                    await set_user_field(user_id, "bankruptcy_date", None)
            except ValueError:
                pass

    return False, None
import time
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)

MAX_REQUESTS_PER_MINUTE = 40
_tracker = defaultdict(list)


def check_rate_limit(user_id: int) -> bool:
    now = time.time()
    timestamps = _tracker[user_id]
    timestamps[:] = [t for t in timestamps if now - t < 60]
    if len(timestamps) >= MAX_REQUESTS_PER_MINUTE:
        return False
    timestamps.append(now)
    return True


def get_remaining(user_id: int) -> int:
    now = time.time()
    timestamps = _tracker[user_id]
    timestamps[:] = [t for t in timestamps if now - t < 60]
    return max(0, MAX_REQUESTS_PER_MINUTE - len(timestamps))

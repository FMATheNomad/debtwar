import time
import logging
from config import COOLDOWNS

logger = logging.getLogger(__name__)

_cooldowns = {}


def check_cooldown(user_id: int, command: str) -> int:
    now = time.time()
    user_cd = _cooldowns.get(user_id, {})
    last_used = user_cd.get(command, 0)
    elapsed = now - last_used
    cd_time = COOLDOWNS.get(command, 0)
    remaining = cd_time - elapsed
    if remaining > 0:
        return int(remaining)
    user_cd[command] = now
    _cooldowns[user_id] = user_cd
    return 0


def is_on_cooldown(user_id: int, command: str) -> bool:
    return check_cooldown(user_id, command) > 0


def get_remaining(user_id: int, command: str) -> int:
    return check_cooldown(user_id, command)


def clear_cooldown(user_id: int, command: str = None):
    if command:
        if user_id in _cooldowns:
            _cooldowns[user_id].pop(command, None)
    else:
        _cooldowns.pop(user_id, None)


def get_all_cooldowns(user_id: int) -> dict:
    return _cooldowns.get(user_id, {})
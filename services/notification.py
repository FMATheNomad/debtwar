import logging
from utils.translator import t

logger = logging.getLogger(__name__)


async def send_notification(target_id: int, target_lang: str, text: str, lang: str, username: str = None, context=None, is_ghost: bool = False) -> str:
    if is_ghost:
        return t("notification_failed", lang)

    if target_id is None or target_id == 0:
        if username:
            try:
                from database.user_repo import get_user_by_username
                row = await get_user_by_username(username)
                if row and row[0] and row[0] > 0:
                    is_ghost_db = False
                    try:
                        from database.user_repo import get_user_full
                        full = await get_user_full(row[0])
                        if full:
                            is_ghost_db = full.get("is_ghost", 0) == 1
                    except Exception:
                        pass
                    if not is_ghost_db:
                        target_id = row[0]
            except Exception:
                pass

    if target_id is None or target_id == 0:
        return t("notification_failed", lang)

    if context is None:
        return ""

    try:
        await context.bot.send_message(chat_id=target_id, text=text, parse_mode="Markdown")
        return t("notification_sent", lang)
    except Exception as e:
        logger.warning(f"Failed to DM user {target_id} ({username}): {e}")
        return t("notification_failed", lang)
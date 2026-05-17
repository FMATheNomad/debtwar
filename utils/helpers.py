from telegram import Update


def parse_mention(text: str) -> str:
    return text.lstrip("@").strip()


def get_username_or_fallback(user) -> str:
    if user.username:
        return user.username
    name = user.first_name or "User"
    safe_name = "".join(c for c in name if c.isalnum() or c == "_")
    return f"{safe_name}_{user.id}"


def format_remaining_time(seconds: int) -> str:
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    else:
        return f"{seconds // 3600}h {(seconds % 3600) // 60}m"


async def resolve_target(update: Update, context, args_index: int = 0, allow_none: bool = False):
    from database.user_repo import get_user_full as _guf, register_user as _ru

    reply = update.message.reply_to_message
    if reply and reply.from_user and not reply.from_user.is_bot:
        target = reply.from_user
        target_id = target.id
        target_uname = get_username_or_fallback(target)
        source = "reply"
        await _ru(target_id, target_uname, "id")
        return target_id, target_uname, source

    if context.args and len(context.args) > args_index:
        raw = context.args[args_index]
        target_name = parse_mention(raw)
        target_row = None
        from database.user_repo import get_user_by_username as _gbu
        target_row = await _gbu(target_name)
        if target_row:
            return target_row[0], target_name, "mention"
        return 0, target_name, "mention"

    if allow_none:
        return None, None, None

    return 0, "", "none"
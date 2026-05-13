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
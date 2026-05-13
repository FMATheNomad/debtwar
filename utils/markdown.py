def safe(text) -> str:
    text = str(text) if not isinstance(text, str) else text
    text = text.replace("_", "\\_")
    text = text.replace("*", "\\*")
    text = text.replace("`", "\\`")
    text = text.replace("[", "\\[")
    return text

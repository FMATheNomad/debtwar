from config import CURRENCY_MAP


def curr_symbol(lang: str) -> str:
    return CURRENCY_MAP.get(lang, "$")


def format_money(amount: int, lang: str) -> str:
    sym = curr_symbol(lang)
    return f"{sym}{amount}"


def format_number(n: int) -> str:
    return f"{n:,}"


def format_percentage(rate: float) -> str:
    return f"{rate * 100:.0f}%"
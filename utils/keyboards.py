from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from utils.translator import t


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_profile", lang), callback_data="profile_show"),
            InlineKeyboardButton(t("menu_btn_daily", lang), callback_data="daily_claim"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_contacts", lang), callback_data="social_contacts"),
            InlineKeyboardButton(t("menu_btn_invite", lang), callback_data="social_invite"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_credit", lang), callback_data="credit_show"),
            InlineKeyboardButton(t("menu_btn_stats", lang), callback_data="stats_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_leaderboard", lang), callback_data="leaderboard_show"),
            InlineKeyboardButton(t("menu_btn_chaos", lang), callback_data="menu_chaos"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_bank", lang), callback_data="bank_info"),
            InlineKeyboardButton(t("menu_btn_history", lang), callback_data="history_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_invest", lang), callback_data="invest_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_social", lang), callback_data="social_menu"),
            InlineKeyboardButton(t("menu_btn_world_news", lang), callback_data="world_news_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_faq", lang), callback_data="faq_show"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def chaos_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_utang", lang), callback_data="action_utang"),
            InlineKeyboardButton(t("menu_btn_nagih", lang), callback_data="action_nagih"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_jebak", lang), callback_data="action_jebak"),
            InlineKeyboardButton(t("chaos_btn_traps", lang), callback_data="chaos_traps"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_transfer", lang), callback_data="action_transfer"),
        ],
        [
            InlineKeyboardButton(t("chaos_btn_spy", lang), callback_data="chaos_spy"),
            InlineKeyboardButton(t("chaos_btn_sabotage", lang), callback_data="chaos_sabo"),
        ],
        [
            InlineKeyboardButton(t("chaos_btn_casino", lang), callback_data="chaos_casino"),
            InlineKeyboardButton(t("chaos_btn_lootbox", lang), callback_data="chaos_lootbox"),
        ],
        [
            InlineKeyboardButton(t("chaos_btn_market", lang), callback_data="chaos_market"),
            InlineKeyboardButton(t("chaos_btn_lunas", lang), callback_data="chaos_lunas"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def leaderboard_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("leaderboard_richest", lang), callback_data="lb_richest"),
            InlineKeyboardButton(t("leaderboard_debt", lang), callback_data="lb_debt"),
        ],
        [
            InlineKeyboardButton(t("leaderboard_chaos", lang), callback_data="lb_chaos"),
            InlineKeyboardButton(t("leaderboard_chaos_detail", lang), callback_data="lb_chaos_detail"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def profile_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_credit", lang), callback_data="credit_show"),
            InlineKeyboardButton(t("menu_btn_stats", lang), callback_data="stats_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_titles", lang), callback_data="titles_show"),
            InlineKeyboardButton(t("profile_btn_achievements", lang), callback_data="achievements_show"),
        ],
        [
            InlineKeyboardButton(t("profile_btn_set_name", lang), callback_data="profile_settings"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_refresh", lang), callback_data="profile_show"),
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def faq_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("faq_btn_howtoplay", lang), callback_data="faq_howtoplay"),
            InlineKeyboardButton(t("faq_btn_commands", lang), callback_data="faq_commands"),
        ],
        [
            InlineKeyboardButton(t("faq_btn_economy", lang), callback_data="faq_economy"),
            InlineKeyboardButton(t("faq_btn_tips", lang), callback_data="faq_tips"),
        ],
        [
            InlineKeyboardButton(t("faq_btn_tagging", lang), callback_data="faq_tagging"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def back_to_main_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(t("menu_btn_back", lang), callback_data="_back")],
    ]
    return InlineKeyboardMarkup(keyboard)


def reply_main_menu(lang: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(t("menu_btn_profile", lang)),
            KeyboardButton(t("menu_btn_daily", lang)),
        ],
        [
            KeyboardButton(t("menu_btn_leaderboard", lang)),
            KeyboardButton(t("menu_btn_chaos", lang)),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def reply_chaos_menu(lang: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(t("menu_btn_utang", lang)),
            KeyboardButton(t("menu_btn_nagih", lang)),
        ],
        [
            KeyboardButton(t("menu_btn_jebak", lang)),
            KeyboardButton(t("menu_btn_transfer", lang)),
        ],
        [
            KeyboardButton(t("menu_btn_back", lang)),
        ],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def gang_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_profile", lang), callback_data="gang_info"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_leaderboard", lang), callback_data="gang_leaderboard"),
            InlineKeyboardButton(t("gang_btn_create", lang), callback_data="gang_create"),
        ],
        [
            InlineKeyboardButton(t("gang_btn_join", lang), callback_data="gang_join"),
            InlineKeyboardButton(t("gang_btn_leave", lang), callback_data="gang_leave"),
        ],
        [
            InlineKeyboardButton(t("gang_btn_vault", lang), callback_data="gang_vault"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def bank_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("bank_btn_deposit", lang), callback_data="bank_deposit"),
            InlineKeyboardButton(t("bank_btn_withdraw", lang), callback_data="bank_withdraw"),
        ],
        [
            InlineKeyboardButton(t("bank_btn_history", lang), callback_data="bank_history"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def casino_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("casino_btn_slots", lang), callback_data="casino_slots"),
            InlineKeyboardButton(t("casino_btn_blackjack", lang), callback_data="casino_bj"),
        ],
        [
            InlineKeyboardButton(t("casino_btn_roulette", lang), callback_data="casino_roulette"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def market_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("market_btn_shop", lang), callback_data="market_show"),
            InlineKeyboardButton(t("market_btn_inventory", lang), callback_data="inventory_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def lootbox_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("lootbox_btn_buy_common", lang), callback_data="lb_buy_common"),
            InlineKeyboardButton(t("lootbox_btn_buy_rare", lang), callback_data="lb_buy_rare"),
        ],
        [
            InlineKeyboardButton(t("lootbox_btn_buy_epic", lang), callback_data="lb_buy_epic"),
            InlineKeyboardButton(t("lootbox_btn_buy_legendary", lang), callback_data="lb_buy_leg"),
        ],
        [
            InlineKeyboardButton(t("lootbox_btn_open_common", lang), callback_data="lb_open_common"),
            InlineKeyboardButton(t("lootbox_btn_open_rare", lang), callback_data="lb_open_rare"),
        ],
        [
            InlineKeyboardButton(t("lootbox_btn_open_epic", lang), callback_data="lb_open_epic"),
            InlineKeyboardButton(t("lootbox_btn_open_legendary", lang), callback_data="lb_open_leg"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def trap_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("trap_btn_fake_investment", lang), callback_data="trap_fake_investment"),
            InlineKeyboardButton(t("trap_btn_phishing", lang), callback_data="trap_phishing"),
        ],
        [
            InlineKeyboardButton(t("trap_btn_tax_trap", lang), callback_data="trap_tax"),
            InlineKeyboardButton(t("trap_btn_pyramid", lang), callback_data="trap_pyramid"),
        ],
        [
            InlineKeyboardButton(t("trap_btn_mafia_extortion", lang), callback_data="trap_mafia_extortion"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def npc_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("npc_btn_loan_shark", lang), callback_data="npc_loan_shark"),
            InlineKeyboardButton(t("npc_btn_mafia_boss", lang), callback_data="npc_mafia_boss"),
        ],
        [
            InlineKeyboardButton(t("npc_btn_scammer", lang), callback_data="npc_scammer"),
            InlineKeyboardButton(t("npc_btn_collector", lang), callback_data="npc_collector"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def court_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("court_btn_file_case", lang), callback_data="court_sue"),
            InlineKeyboardButton(t("court_btn_vote", lang), callback_data="court_vote"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def social_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_gang", lang), callback_data="gang_menu"),
            InlineKeyboardButton(t("menu_btn_wanted", lang), callback_data="wanted_show"),
        ],
        [
            InlineKeyboardButton(t("social_btn_court", lang), callback_data="court_show"),
            InlineKeyboardButton(t("social_btn_npc", lang), callback_data="npc_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
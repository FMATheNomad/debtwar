from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from utils.translator import t


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(t("menu_btn_profile", lang), callback_data="profile_show"),
            InlineKeyboardButton(t("menu_btn_daily", lang), callback_data="daily_claim"),
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
            InlineKeyboardButton("🏦 Bank", callback_data="bank_info"),
            InlineKeyboardButton("📜 History", callback_data="history_show"),
        ],
        [
            InlineKeyboardButton("💹 Investasi", callback_data="invest_show"),
        ],
        [
            InlineKeyboardButton("🏴 Social", callback_data="social_menu"),
            InlineKeyboardButton("📰 World News", callback_data="world_news_show"),
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
            InlineKeyboardButton("🪤 Traps", callback_data="chaos_traps"),
        ],
        [
            InlineKeyboardButton("🔄 Transfer", callback_data="action_transfer"),
        ],
        [
            InlineKeyboardButton("🕵️ Spy", callback_data="chaos_spy"),
            InlineKeyboardButton("💣 Sabotage", callback_data="chaos_sabo"),
        ],
        [
            InlineKeyboardButton("🎰 Casino", callback_data="chaos_casino"),
            InlineKeyboardButton("🎁 Lootbox", callback_data="chaos_lootbox"),
        ],
        [
            InlineKeyboardButton("🏪 Market", callback_data="chaos_market"),
            InlineKeyboardButton("💳 Lunas", callback_data="chaos_lunas"),
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
            InlineKeyboardButton("👑 Titles", callback_data="titles_show"),
            InlineKeyboardButton("🏆 Achievements", callback_data="achievements_show"),
        ],
        [
            InlineKeyboardButton("⚙️ Set Name", callback_data="profile_settings"),
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
            InlineKeyboardButton(t("faq_btn_commands", lang), callback_data="faq_commands"),
            InlineKeyboardButton(t("faq_btn_economy", lang), callback_data="faq_economy"),
        ],
        [
            InlineKeyboardButton(t("faq_btn_tips", lang), callback_data="faq_tips"),
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
            InlineKeyboardButton("➕ Create", callback_data="gang_create"),
        ],
        [
            InlineKeyboardButton("🔗 Join", callback_data="gang_join"),
            InlineKeyboardButton("🚪 Leave", callback_data="gang_leave"),
        ],
        [
            InlineKeyboardButton("🏦 Vault", callback_data="gang_vault"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def bank_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🏦 Info", callback_data="bank_info"),
            InlineKeyboardButton("📥 Deposit", callback_data="bank_deposit"),
        ],
        [
            InlineKeyboardButton("📤 Withdraw", callback_data="bank_withdraw"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def casino_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎰 Slots", callback_data="casino_slots"),
            InlineKeyboardButton("🃏 Blackjack", callback_data="casino_bj"),
        ],
        [
            InlineKeyboardButton("🎱 Roulette", callback_data="casino_roulette"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def market_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🏪 Shop", callback_data="market_show"),
            InlineKeyboardButton("🎒 Inventory", callback_data="inventory_show"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def lootbox_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📦 Common (200)", callback_data="lb_buy_common"),
            InlineKeyboardButton("🎁 Rare (500)", callback_data="lb_buy_rare"),
        ],
        [
            InlineKeyboardButton("💎 Epic (1200)", callback_data="lb_buy_epic"),
            InlineKeyboardButton("👑 Legendary (3000)", callback_data="lb_buy_leg"),
        ],
        [
            InlineKeyboardButton("📂 Buka Common", callback_data="lb_open_common"),
            InlineKeyboardButton("📂 Buka Rare", callback_data="lb_open_rare"),
        ],
        [
            InlineKeyboardButton("📂 Buka Epic", callback_data="lb_open_epic"),
            InlineKeyboardButton("📂 Buka Legendary", callback_data="lb_open_leg"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def trap_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎣 Fake Investment", callback_data="trap_fake_investment"),
            InlineKeyboardButton("📧 Phishing", callback_data="trap_phishing"),
        ],
        [
            InlineKeyboardButton("🧾 Tax Trap", callback_data="trap_tax"),
            InlineKeyboardButton("🔺 Pyramid", callback_data="trap_pyramid"),
        ],
        [
            InlineKeyboardButton("💀 Mafia Extortion", callback_data="trap_mafia_extortion"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def npc_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🧛 Loan Shark", callback_data="npc_loan_shark"),
            InlineKeyboardButton("🕴️ Mafia Boss", callback_data="npc_mafia_boss"),
        ],
        [
            InlineKeyboardButton("🐍 Scammer", callback_data="npc_scammer"),
            InlineKeyboardButton("💪 Collector", callback_data="npc_collector"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def court_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("⚖️ File Case", callback_data="court_sue"),
            InlineKeyboardButton("🗳️ Vote", callback_data="court_vote"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def social_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    from utils.translator import t as _t
    keyboard = [
        [
            InlineKeyboardButton("🏴 Gang", callback_data="gang_menu"),
            InlineKeyboardButton("🚨 Wanted", callback_data="wanted_show"),
        ],
        [
            InlineKeyboardButton("🏛️ Court", callback_data="court_show"),
            InlineKeyboardButton("🤖 NPC", callback_data="npc_show"),
        ],
        [
            InlineKeyboardButton("🔗 Invite", callback_data="social_invite"),
            InlineKeyboardButton("📇 Contacts", callback_data="social_contacts"),
        ],
        [
            InlineKeyboardButton(t("menu_btn_back", lang), callback_data="menu_main"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
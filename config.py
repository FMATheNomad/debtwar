import os

# ─────────────────────────────────────────
# BOT TOKEN
# ─────────────────────────────────────────
TOKEN = os.getenv("DEBTWAR_TOKEN")
if not TOKEN:
    raise RuntimeError("DEBTWAR_TOKEN environment variable not set!")

# ─────────────────────────────────────────
# DATABASE
# ─────────────────────────────────────────
DB_FILE = "debtwar.db"

# ─────────────────────────────────────────
# ECONOMY LIMITS
# ─────────────────────────────────────────
INITIAL_BALANCE = 1000
MAX_DEBT = 5000
BANKRUPTCY_THRESHOLD = MAX_DEBT * 2  # 10000

# ─────────────────────────────────────────
# TRAP SYSTEM
# ─────────────────────────────────────────
TRAP_COST_MIN = 10
TRAP_COST_MAX = 50
TRAP_DEBT_MIN = 50
TRAP_DEBT_MAX = 300
TRAP_SUCCESS_RATE = 0.5
TRAP_REWARD_RATE = 0.20

# ─────────────────────────────────────────
# COOLDOWNS (seconds)
# ─────────────────────────────────────────
COOLDOWNS = {
    "utang": 10,
    "nagih": 5,
    "jebak": 15,
    "transfer": 10,
    "npc_loan_shark": 600,
    "npc_mafia_boss": 600,
    "npc_scammer": 300,
    "npc_collector": 600,
}

# ─────────────────────────────────────────
# DAILY REWARD
# ─────────────────────────────────────────
DAILY_REWARD_MIN = 50
DAILY_REWARD_MAX = 200
DAILY_STREAK_BONUS = 25
DAILY_COOLDOWN = 86400

# ─────────────────────────────────────────
# INTEREST SYSTEM
# ─────────────────────────────────────────
INTEREST_RATE = 0.05
INTEREST_MIN_AMOUNT = 10
INTEREST_CHECK_INTERVAL = 3600

# ─────────────────────────────────────────
# ANTI-ABUSE LIMITS
# ─────────────────────────────────────────
DAILY_LEND_LIMIT = MAX_DEBT * 2
DAILY_TARGET_LEND_LIMIT = MAX_DEBT
DAILY_TRANSFER_LIMIT = 3000
MAX_TRANSACTIONS_PER_MINUTE = 5
BANKRUPTCY_COOLDOWN_HOURS = 24

# ─────────────────────────────────────────
# RANDOM EVENT
# ─────────────────────────────────────────
EVENT_CHANCE = 0.05
EVENT_CRISIS_MULTIPLIER = 0.10
EVENT_BOOM_MULTIPLIER = 0.05
EVENT_GIFT_AMOUNT = 50

# ─────────────────────────────────────────
# ACHIEVEMENT THRESHOLDS
# ─────────────────────────────────────────
ACHIEVEMENTS = {
    "first_trap": {"id": "first_trap", "threshold": 1, "key": "first_trap"},
    "first_collect": {"id": "first_collect", "threshold": 1, "key": "first_collect"},
    "debt_collector_1000": {"id": "debt_collector_1000", "threshold": 1000, "key": "debt_collector"},
    "debt_collector_5000": {"id": "debt_collector_5000", "threshold": 5000, "key": "debt_collector_5000"},
    "big_lender_1000": {"id": "big_lender_1000", "threshold": 1000, "key": "big_lender"},
    "trap_master_10": {"id": "trap_master_10", "threshold": 10, "key": "trap_master"},
    "bankrupt_once": {"id": "bankrupt_once", "threshold": 1, "key": "bankrupt"},
    "streak_7": {"id": "streak_7", "threshold": 7, "key": "streak_7"},
}

# ─────────────────────────────────────────
# LEADERBOARD
# ─────────────────────────────────────────
LEADERBOARD_SIZE = 10

# ─────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────
ASSETS_DIR = "assets"
LOGO_FILE = "assets/logo.png"
LOGS_DIR = "logs"
LOG_FILE = "logs/bot.log"

# ─────────────────────────────────────────
# CURRENCY MAP
# ─────────────────────────────────────────
CURRENCY_MAP = {
    "id": "Rp",
    "en": "$",
    "en-gb": "\u00a3",
    "eu": "\u20ac",
    "jp": "\u00a5",
    "kr": "\u20a9",
    "ru": "\u20bd",
    "in": "\u20b9",
}

# ─────────────────────────────────────────
# LANGUAGE NAMES
# ─────────────────────────────────────────
SUPPORTED_LANGUAGES = {
    "id": "Indonesia",
    "en": "English",
}

# ─────────────────────────────────────────
# CREDIT SCORE
# ─────────────────────────────────────────
CREDIT_SCORE_DEFAULT = 500
CREDIT_SCORE_MIN = 0
CREDIT_SCORE_MAX = 1000
CREDIT_REPAY_BONUS = 10
CREDIT_DEFAULT_PENALTY = 25
CREDIT_BANKRUPTCY_PENALTY = 75
CREDIT_TRAP_FAIL_PENALTY = 5
CREDIT_DAILY_ACTIVITY_BONUS = 2
CREDIT_SPY_CAUGHT_PENALTY = 15

# ─────────────────────────────────────────
# TITLE / RANK SYSTEM
# ─────────────────────────────────────────
TITLES = {
    "debt_peon":       {"name": "Debt Peon",       "min_credit": 0,   "min_chaos": 0},
    "money_mule":      {"name": "Money Mule",      "min_credit": 200, "min_chaos": 0},
    "debt_goblin":     {"name": "Debt Goblin",     "min_credit": 400, "min_chaos": 5},
    "loan_shark":      {"name": "Loan Shark",      "min_credit": 600, "min_chaos": 15},
    "mafia_banker":    {"name": "Mafia Banker",    "min_credit": 750, "min_chaos": 30},
    "cert_scammer":    {"name": "Certified Scammer","min_credit": 0,  "min_chaos": 50},
    "chaos_agent":     {"name": "Chaos Agent",     "min_credit": 300, "min_chaos": 75},
    "king_of_chaos":   {"name": "King of Chaos",   "min_credit": 500, "min_chaos": 100},
    "debt_collector":  {"name": "Debt Collector",  "min_credit": 400, "min_chaos": 20},
    "shadow_mafia":    {"name": "Shadow Mafia",    "min_credit": 850, "min_chaos": 60},
}

# ─────────────────────────────────────────
# SPY SYSTEM
# ─────────────────────────────────────────
SPY_COST = 100
SPY_SUCCESS_RATE = 0.7
SPY_DETECTION_RATE = 0.15
SPY_FAIL_FINE = 50
SPY_COOLDOWN = 120

# ─────────────────────────────────────────
# SABOTAGE SYSTEM
# ─────────────────────────────────────────
SABOTAGE_COST = 150
SABOTAGE_SUCCESS_RATE = 0.55
SABOTAGE_FAIL_FINE = 80
SABOTAGE_FREEZE_SECONDS = 3600
SABOTAGE_STEAL_MIN = 20
SABOTAGE_STEAL_MAX = 100
SABOTAGE_COOLDOWN = 300

# ─────────────────────────────────────────
# GANG / MAFIA SYSTEM
# ─────────────────────────────────────────
GANG_CREATE_COST = 2000
GANG_MAX_MEMBERS = 20
GANG_TAX_RATE = 0.05
GANG_WAR_COOLDOWN_HOURS = 48
GANG_REPUTATION_WIN_BONUS = 50
GANG_REPUTATION_LOSS_PENALTY = 20

# ─────────────────────────────────────────
# BANK SYSTEM
# ─────────────────────────────────────────
BANK_INTEREST_RATE = 0.02
BANK_INTEREST_INTERVAL_HOURS = 24
BANK_INTEREST_MIN_AMOUNT = 5
BANK_WITHDRAW_FEE = 0.02
BANK_MAX_BALANCE = 50000

# ─────────────────────────────────────────
# CASINO / GAMBLING
# ─────────────────────────────────────────
CASINO_MIN_BET = 10
CASINO_MAX_BET = 500
CASINO_RTP = 0.85  # house edge 15%
CASINO_COOLDOWN = 10

# ─────────────────────────────────────────
# MARKET / SHOP
# ─────────────────────────────────────────
MARKET_ITEMS = {
    "shield_basic":      {"name": "Basic Shield",      "price": 300,  "type": "shield",         "duration_hours": 24,  "effect": "anti_trap"},
    "shield_advanced":   {"name": "Adv Shield",        "price": 800,  "type": "shield",         "duration_hours": 48,  "effect": "anti_trap_spy"},
    "debt_insurance":    {"name": "Debt Insurance",    "price": 500,  "type": "insurance",      "duration_hours": 24,  "effect": "bankruptcy_protection"},
    "trap_booster":      {"name": "Trap Booster",      "price": 400,  "type": "consumable",     "effect_value": 0.80,  "effect": "trap_success_rate"},
    "spy_tools":         {"name": "Spy Tools",         "price": 350,  "type": "consumable",     "effect_value": 0.90,  "effect": "spy_success_rate"},
    "protection_mafia":  {"name": "Mafia Protection",  "price": 1200, "type": "shield",         "duration_hours": 72,  "effect": "anti_sabotage"},
}

# ─────────────────────────────────────────
# LOOTBOX
# ─────────────────────────────────────────
LOOTBOX_PRICES = {
    "common":   200,
    "rare":     500,
    "epic":     1200,
    "legendary": 3000,
}

LOOTBOX_REWARDS = {
    "common":   {"money": (50, 200), "debt_bomb": (20, 80), "nothing": (0, 0)},
    "rare":     {"money": (200, 500), "debt_bomb": (80, 200), "shield": (1, 1)},
    "epic":     {"money": (500, 1500), "debt_bomb": (200, 500), "chaos_buff": (1, 1)},
    "legendary": {"money": (1500, 5000), "curse": (1, 1), "title_unlock": (1, 1)},
}

# ─────────────────────────────────────────
# WANTED SYSTEM
# ─────────────────────────────────────────
WANTED_CHAOS_THRESHOLD = 50
WANTED_BOUNTY_PER_CHAOS = 50
WANTED_TARGET_MULTIPLIER = 1.5

# ─────────────────────────────────────────
# WORLD EVENTS
# ─────────────────────────────────────────
WORLD_EVENT_INTERVAL_MIN = 3600
WORLD_EVENT_INTERVAL_MAX = 7200
WORLD_EVENT_CHANCE = 0.3

# ─────────────────────────────────────────
# NPC SYSTEM
# ─────────────────────────────────────────
NPC_COOLDOWN = 600
NPC_LOAN_SHARK_MAX = 3000
NPC_LOAN_SHARK_INTEREST = 0.10
NPC_MISSION_COST_MIN = 50
NPC_MISSION_COST_MAX = 200
NPC_MISSION_REWARD_MIN = 100
NPC_MISSION_REWARD_MAX = 500

# ─────────────────────────────────────────
# COURT SYSTEM
# ─────────────────────────────────────────
COURT_LAWYER_COST = 300
COURT_CORRUPTION_CHANCE = 0.15
COURT_MAX_FINE = 1000
COURT_VOTING_DURATION = 3600

# ─────────────────────────────────────────
# SEASON SYSTEM
# ─────────────────────────────────────────
SEASON_DURATION_DAYS = 30
SEASON_XP_PER_LEND = 10
SEASON_XP_PER_COLLECT = 15
SEASON_XP_PER_TRAP = 20
import aiosqlite
import logging
from config import DB_FILE

logger = logging.getLogger(__name__)


async def get_connection():
    conn = await aiosqlite.connect(DB_FILE)
    conn.row_factory = aiosqlite.Row
    await conn.execute("PRAGMA journal_mode=WAL")
    await conn.execute("PRAGMA foreign_keys=ON")
    return conn


async def init_db():
    conn = await get_connection()
    try:
        await conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id       INTEGER PRIMARY KEY,
                username TEXT,
                balance  INTEGER DEFAULT 1000,
                debt     INTEGER DEFAULT 0,
                language TEXT DEFAULT 'id'
            );

            CREATE TABLE IF NOT EXISTS transactions (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                from_id   INTEGER,
                to_user   TEXT,
                type      TEXT,
                amount    INTEGER,
                timestamp TEXT DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS daily_limits (
                user_id        INTEGER,
                date           TEXT,
                total_lent     INTEGER DEFAULT 0,
                total_transfer INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, date)
            );

            CREATE TABLE IF NOT EXISTS achievements (
                user_id   INTEGER,
                ach_id    TEXT,
                unlocked  TEXT DEFAULT (datetime('now', 'localtime')),
                PRIMARY KEY (user_id, ach_id)
            );

            CREATE TABLE IF NOT EXISTS ghost_notifications (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                target_user TEXT NOT NULL,
                from_name   TEXT,
                action_type TEXT,
                amount      INTEGER DEFAULT 0,
                detail      TEXT,
                timestamp   TEXT DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS gangs (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT UNIQUE,
                owner_id    INTEGER,
                reputation  INTEGER DEFAULT 0,
                vault_balance INTEGER DEFAULT 0,
                member_count INTEGER DEFAULT 1,
                created_at  TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (owner_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS gang_members (
                gang_id   INTEGER,
                user_id   INTEGER,
                role      TEXT DEFAULT 'member',
                joined_at TEXT DEFAULT (datetime('now', 'localtime')),
                PRIMARY KEY (gang_id, user_id),
                FOREIGN KEY (gang_id) REFERENCES gangs(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS gang_wars (
                id                INTEGER PRIMARY KEY AUTOINCREMENT,
                attacker_gang_id  INTEGER,
                defender_gang_id  INTEGER,
                status            TEXT DEFAULT 'declared',
                attacker_score    INTEGER DEFAULT 0,
                defender_score    INTEGER DEFAULT 0,
                winner_id         INTEGER,
                started_at        TEXT DEFAULT (datetime('now', 'localtime')),
                ended_at          TEXT,
                FOREIGN KEY (attacker_gang_id) REFERENCES gangs(id),
                FOREIGN KEY (defender_gang_id) REFERENCES gangs(id)
            );

            CREATE TABLE IF NOT EXISTS bank_accounts (
                user_id         INTEGER PRIMARY KEY,
                balance         INTEGER DEFAULT 0,
                last_interest   TEXT,
                total_deposited INTEGER DEFAULT 0,
                total_withdrawn INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS casino_stats (
                user_id       INTEGER PRIMARY KEY,
                total_bet     INTEGER DEFAULT 0,
                total_won     INTEGER DEFAULT 0,
                total_lost    INTEGER DEFAULT 0,
                slot_plays    INTEGER DEFAULT 0,
                blackjack_plays INTEGER DEFAULT 0,
                roulette_plays INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS titles (
                id              TEXT PRIMARY KEY,
                name            TEXT,
                description     TEXT,
                min_credit_score INTEGER DEFAULT 0,
                min_chaos       INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS user_titles (
                user_id    INTEGER,
                title_id   TEXT,
                unlocked_at TEXT DEFAULT (datetime('now', 'localtime')),
                is_active  INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, title_id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS stats_history (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER,
                stat_type  TEXT,
                stat_value INTEGER,
                recorded_at TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS wanted_list (
                user_id       INTEGER PRIMARY KEY,
                bounty        INTEGER DEFAULT 0,
                wanted_level  INTEGER DEFAULT 1,
                total_crimes  INTEGER DEFAULT 0,
                updated_at    TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS spy_logs (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                spy_id     INTEGER,
                target_id  INTEGER,
                success    INTEGER,
                detected   INTEGER DEFAULT 0,
                timestamp  TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (spy_id) REFERENCES users(id),
                FOREIGN KEY (target_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS sabotage_logs (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                attacker_id   INTEGER,
                target_id     INTEGER,
                sabotage_type TEXT,
                success       INTEGER,
                amount        INTEGER DEFAULT 0,
                timestamp     TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (attacker_id) REFERENCES users(id),
                FOREIGN KEY (target_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS market_items (
                id             TEXT PRIMARY KEY,
                name           TEXT,
                description    TEXT,
                price          INTEGER,
                item_type      TEXT,
                effect_value   REAL DEFAULT 0,
                duration_hours INTEGER DEFAULT 0,
                effect         TEXT
            );

            CREATE TABLE IF NOT EXISTS user_items (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER,
                item_id    TEXT,
                quantity   INTEGER DEFAULT 1,
                expires_at TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS active_shields (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER,
                shield_type TEXT,
                expires_at  TEXT,
                durability  INTEGER DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS seasons (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT,
                started_at TEXT,
                ended_at   TEXT,
                is_active  INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS season_leaderboard (
                season_id INTEGER,
                user_id   INTEGER,
                score     INTEGER DEFAULT 0,
                rank      INTEGER,
                PRIMARY KEY (season_id, user_id),
                FOREIGN KEY (season_id) REFERENCES seasons(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS court_cases (
                id             INTEGER PRIMARY KEY AUTOINCREMENT,
                plaintiff_id   INTEGER,
                defendant_id   INTEGER,
                charge         TEXT,
                status         TEXT DEFAULT 'pending',
                verdict        TEXT,
                fine_amount    INTEGER DEFAULT 0,
                created_at     TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (plaintiff_id) REFERENCES users(id),
                FOREIGN KEY (defendant_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS court_votes (
                case_id  INTEGER,
                voter_id INTEGER,
                vote     TEXT,
                PRIMARY KEY (case_id, voter_id),
                FOREIGN KEY (case_id) REFERENCES court_cases(id),
                FOREIGN KEY (voter_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS npc_interactions (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER,
                npc_type   TEXT,
                action     TEXT,
                reward     INTEGER DEFAULT 0,
                timestamp  TEXT DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS trap_types (
                id               TEXT PRIMARY KEY,
                name             TEXT,
                success_rate     REAL DEFAULT 0.3,
                min_damage       INTEGER DEFAULT 50,
                max_damage       INTEGER DEFAULT 200,
                cooldown_seconds INTEGER DEFAULT 300,
                min_level        INTEGER DEFAULT 1,
                cost             INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS drama_log (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                drama_text TEXT,
                created_at TEXT DEFAULT (datetime('now', 'localtime'))
            );

            CREATE TABLE IF NOT EXISTS world_events (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type  TEXT,
                title       TEXT,
                description TEXT,
                multiplier  REAL DEFAULT 1.0,
                started_at  TEXT,
                ended_at    TEXT,
                is_active   INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS lootbox_inventory (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id      INTEGER,
                lootbox_type TEXT,
                quantity     INTEGER DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );

            CREATE TABLE IF NOT EXISTS lootbox_rewards (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id      INTEGER,
                reward_type  TEXT,
                reward_value INTEGER DEFAULT 0,
                rarity       TEXT,
                opened_at    TEXT DEFAULT (datetime('now', 'localtime'))
            );
        """)
        await conn.commit()

        migrations = [
            "ALTER TABLE users ADD COLUMN total_lent INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN total_collected INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN traps_set INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN traps_successful INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN daily_streak INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN last_daily TEXT",
            "ALTER TABLE users ADD COLUMN bankrupt_count INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN is_bankrupt INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN bankruptcy_date TEXT",
            "ALTER TABLE users ADD COLUMN total_daily_claimed INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN is_ghost INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN credit_score INTEGER DEFAULT 500",
            "ALTER TABLE users ADD COLUMN total_repaid INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN total_defaulted INTEGER DEFAULT 0",
            "ALTER TABLE users ADD COLUMN display_name TEXT",
            "ALTER TABLE users ADD COLUMN needs_name INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN slot_wins INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN slot_losses INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN blackjack_wins INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN blackjack_losses INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN roulette_wins INTEGER DEFAULT 0",
            "ALTER TABLE casino_stats ADD COLUMN roulette_losses INTEGER DEFAULT 0",
        ]
        for migration in migrations:
            col_name = migration.split()[5]
            try:
                await conn.execute(migration)
                await conn.commit()
                logger.info(f"Migration: column '{col_name}' added")
            except Exception:
                pass

        await seed_default_data(conn)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database init error: {e}")
        raise
    finally:
        await conn.close()


async def seed_default_data(conn):
    from config import TITLES, MARKET_ITEMS
    for tid, tdata in TITLES.items():
        try:
            await conn.execute(
                "INSERT OR IGNORE INTO titles (id, name, min_credit_score, min_chaos) VALUES (?, ?, ?, ?)",
                (tid, tdata["name"], tdata["min_credit"], tdata["min_chaos"]),
            )
        except Exception:
            pass
    for mid, mdata in MARKET_ITEMS.items():
        try:
            await conn.execute(
                "INSERT OR IGNORE INTO market_items (id, name, price, item_type, effect_value, duration_hours, effect) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (mid, mdata["name"], mdata["price"], mdata["type"], mdata.get("effect_value", 0), mdata.get("duration_hours", 0), mdata.get("effect", "")),
            )
        except Exception:
            pass
    trap_seeds = [
        ("fake_investment", "Fake Investment", 0.35, 80, 300, 600, 1, 0),
        ("phishing_trap", "Phishing Trap", 0.40, 60, 200, 450, 2, 50),
        ("tax_trap", "Tax Trap", 0.30, 100, 400, 900, 3, 100),
        ("pyramid_scheme", "Pyramid Scheme", 0.25, 150, 500, 1200, 5, 200),
        ("mafia_extortion", "Mafia Extortion", 0.20, 200, 800, 1800, 7, 300),
    ]
    for ts in trap_seeds:
        try:
            await conn.execute(
                "INSERT OR IGNORE INTO trap_types (id, name, success_rate, min_damage, max_damage, cooldown_seconds, min_level, cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ts,
            )
        except Exception:
            pass
    await conn.commit()
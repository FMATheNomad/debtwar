import logging
import asyncio
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.request import HTTPXRequest

from config import TOKEN, LOG_FILE, LOGS_DIR
from database.db import init_db
from database.user_repo import link_ghost_by_username
from handlers.start import cmd_start
from handlers.profile import cmd_profile
from handlers.utang import cmd_utang
from handlers.nagih import cmd_nagih
from handlers.jebak import cmd_jebak
from handlers.transfer import cmd_transfer
from handlers.leaderboard import cmd_leaderboard
from handlers.daily import cmd_daily
from handlers.faq import cmd_faq
from handlers.menu import menu_callback
from handlers.gang import cmd_gang
from handlers.spy import cmd_spy
from handlers.sabotage import cmd_sabotage
from handlers.advanced_traps import cmd_trap, cmd_trap_list
from handlers.bank import cmd_bank
from handlers.casino import cmd_casino, cmd_slots, cmd_blackjack, cmd_roulette
from handlers.market import cmd_market, cmd_buy, cmd_inventory
from handlers.lootbox import cmd_lootbox
from handlers.npc import cmd_npc
from handlers.investment import cmd_invest_buy, cmd_invest_sell
from handlers.shop import cmd_shop, pre_checkout, successful_payment
from handlers.court import cmd_court
from handlers.lunas import cmd_lunas
from handlers.setname import cmd_setname
from utils.translator import t
from utils.keyboards import main_menu_keyboard, chaos_menu_keyboard
from services.interest_service import process_interest_for_all
from services.world_event_service import trigger_random_event, deactivate_expired_events
from services.bank_service import process_bank_interest
from services.rate_limiter import check_rate_limit as global_rl
from services.backup_service import schedule_backup
from services.investment_service import simulate_prices

os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


async def catch_all_updates(update, context):
    user = update.effective_user
    if user and user.username:
        try:
            await link_ghost_by_username(user.username, user.id)
        except Exception:
            pass


async def handle_message(update, context):
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"
    text = update.message.text.strip().lower()

    from database.db import get_connection as gcn
    conn = await gcn()
    try:
        async with conn.execute(
            "SELECT needs_name FROM users WHERE id = ?", (user.id,)
        ) as cur:
            row = await cur.fetchone()
            if row and row[0] == 1:
                await update.message.reply_text(
                    "👋 Kamu belum set nama display!\n"
                    "Ketik: `/setname <nama>`\n"
                    "Contoh: `/setname Fariz Ganteng`",
                    parse_mode="Markdown",
                )
                return
    finally:
        await conn.close()

    menu_map = {
        "profile": "profile_show",
        "daily": "daily_claim",
        "leaderboard": "leaderboard_show",
        "chaos menu": "menu_chaos",
        "chaos": "menu_chaos",
        "kembali": "menu_main",
        "back": "menu_main",
        "utang": None,
        "nagih": None,
        "jebak": None,
        "transfer": None,
        "lend": None,
        "collect": None,
        "trap": None,
        "bantuan": "faq_show",
        "help": "faq_show",
        "faq": "faq_show",
    }

    if text in menu_map:
        action = menu_map[text]
        if action is None:
            prompts = {
                "utang": "action_prompt_utang",
                "nagih": "action_prompt_nagih",
                "jebak": "action_prompt_jebak",
                "transfer": "action_prompt_transfer",
                "lend": "action_prompt_utang",
                "collect": "action_prompt_nagih",
                "trap": "action_prompt_jebak",
            }
            await update.message.reply_text(
                t(prompts.get(text, "action_prompt_utang"), lang),
                parse_mode="Markdown",
            )
        elif action == "menu_main":
            await update.message.reply_text(
                t("menu_main_title", lang),
                parse_mode="Markdown",
                reply_markup=main_menu_keyboard(lang),
            )
        elif action == "menu_chaos":
            await update.message.reply_text(
                t("menu_chaos_title", lang),
                parse_mode="Markdown",
                reply_markup=chaos_menu_keyboard(lang),
            )
        else:
            pass


async def on_startup(app):
    await init_db()
    logger.info("Database initialized")
    logger.info("Bot started — Debt War is live!")

    asyncio.create_task(schedule_interest(app))
    asyncio.create_task(schedule_world_events(app))
    asyncio.create_task(schedule_bank_interest(app))
    asyncio.create_task(schedule_backup())
    asyncio.create_task(schedule_investment_prices())


async def schedule_investment_prices():
    while True:
        await asyncio.sleep(3600)
        try:
            await simulate_prices()
        except Exception as e:
            logger.error(f"Investment price error: {e}")


async def schedule_interest(app):
    while True:
        await asyncio.sleep(3600)
        try:
            await process_interest_for_all()
        except Exception as e:
            logger.error(f"Interest processing error: {e}")


async def schedule_world_events(app):
    import random
    while True:
        await asyncio.sleep(random.randint(1800, 3600))
        try:
            await deactivate_expired_events()
            event = await trigger_random_event()
            if event:
                logger.info(f"World event active: {event['event']['id']}")
        except Exception as e:
            logger.error(f"World event error: {e}")


async def schedule_bank_interest(app):
    while True:
        await asyncio.sleep(7200)
        try:
            count = await process_bank_interest()
            if count > 0:
                logger.info(f"Bank interest paid to {count} accounts")
        except Exception as e:
            logger.error(f"Bank interest error: {e}")


async def post_stop(app):
    logger.info("Bot stopped.")


async def global_error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Global error: {context.error}", exc_info=context.error)
    try:
        if isinstance(update, Update) and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ Terjadi error internal. Tim kami sudah notified.",
            )
    except Exception:
        pass


def main():
    request = HTTPXRequest(
        connect_timeout=60.0,
        read_timeout=60.0,
        write_timeout=60.0,
    )

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .request(request)
        .post_init(on_startup)
        .post_stop(post_stop)
        .build()
    )

    app.add_handler(MessageHandler(filters.ALL, catch_all_updates), group=-1)
    app.add_handler(CallbackQueryHandler(catch_all_updates), group=-1)

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("profile", cmd_profile))
    app.add_handler(CommandHandler("bots", cmd_profile))
    app.add_handler(CommandHandler("utang", cmd_utang))
    app.add_handler(CommandHandler("nagih", cmd_nagih))
    app.add_handler(CommandHandler("jebak", cmd_jebak))
    app.add_handler(CommandHandler("transfer", cmd_transfer))
    app.add_handler(CommandHandler("leaderboard", cmd_leaderboard))
    app.add_handler(CommandHandler("daily", cmd_daily))
    app.add_handler(CommandHandler("faq", cmd_faq))
    app.add_handler(CommandHandler("help", cmd_faq))
    app.add_handler(CommandHandler("menu", menu_callback))
    app.add_handler(CommandHandler("gang", cmd_gang))
    app.add_handler(CommandHandler("mafia", cmd_gang))
    app.add_handler(CommandHandler("spy", cmd_spy))
    app.add_handler(CommandHandler("sabotage", cmd_sabotage))
    app.add_handler(CommandHandler("trap", cmd_trap))
    app.add_handler(CommandHandler("traps", cmd_trap_list))
    app.add_handler(CommandHandler("bank", cmd_bank))
    app.add_handler(CommandHandler("casino", cmd_casino))
    app.add_handler(CommandHandler("slots", cmd_slots))
    app.add_handler(CommandHandler("bj", cmd_blackjack))
    app.add_handler(CommandHandler("blackjack", cmd_blackjack))
    app.add_handler(CommandHandler("roulette", cmd_roulette))
    app.add_handler(CommandHandler("market", cmd_market))
    app.add_handler(CommandHandler("shop", cmd_market))
    app.add_handler(CommandHandler("buy", cmd_buy))
    app.add_handler(CommandHandler("inv", cmd_inventory))
    app.add_handler(CommandHandler("inventory", cmd_inventory))
    app.add_handler(CommandHandler("lootbox", cmd_lootbox))
    app.add_handler(CommandHandler("loot", cmd_lootbox))
    app.add_handler(CommandHandler("npc", cmd_npc))
    app.add_handler(CommandHandler("court", cmd_court))
    app.add_handler(CommandHandler("sue", cmd_court))
    app.add_handler(CommandHandler("lunas", cmd_lunas))
    app.add_handler(CommandHandler("pay", cmd_lunas))
    app.add_handler(CommandHandler("setname", cmd_setname))
    app.add_handler(CommandHandler("name", cmd_setname))
    app.add_handler(CommandHandler("investbuy", cmd_invest_buy))
    app.add_handler(CommandHandler("investsell", cmd_invest_sell))
    app.add_handler(CommandHandler("shop", cmd_shop))
    app.add_handler(PreCheckoutQueryHandler(pre_checkout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))

    app.add_handler(CallbackQueryHandler(menu_callback, pattern="^(_back|menu_|profile_|daily_|leaderboard_|action_|faq_|credit_|stats_|titles_|title_select_|achievements_|social_|gang_|wanted_|drama_|chaos_|bank_|casino_|market_|inventory_|npc_|court_|trap_|world_|invest_|history_|shop_).*"))

    from handlers.leaderboard import lb_callback
    app.add_handler(CallbackQueryHandler(lb_callback, pattern="^lb_.*"))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(global_error_handler)

    logger.info("Starting Debt War bot...")
    print("⚔️ Debt War — Bot jalan! Tekan Ctrl+C buat berhenti.")
    app.run_polling()


if __name__ == "__main__":
    main()
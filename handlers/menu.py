import logging
import traceback

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from utils.translator import t
from utils.keyboards import (
    main_menu_keyboard, chaos_menu_keyboard, leaderboard_menu_keyboard,
    profile_menu_keyboard, back_to_main_keyboard, social_menu_keyboard, gang_menu_keyboard,
    casino_menu_keyboard, market_menu_keyboard,
)
from database.user_repo import get_leaderboard, get_leaderboard_chaos_detail
from services.economy import apply_daily_reward
from utils.formatter import format_money
from config import SPY_COST, SPY_FAIL_FINE, SABOTAGE_COST, SABOTAGE_FAIL_FINE, SABOTAGE_STEAL_MIN, SABOTAGE_STEAL_MAX, LOOTBOX_PRICES

logger = logging.getLogger(__name__)

_BTN_DESCS = {
    "menu_main": None,
    "menu_chaos": "btn_desc_chaos",
    "profile_show": "btn_desc_profile",
    "daily_claim": "btn_desc_daily",
    "leaderboard_show": "btn_desc_leaderboard",
    "action_utang": "btn_desc_utang",
    "action_nagih": "btn_desc_nagih",
    "action_jebak": "btn_desc_jebak",
    "action_transfer": "btn_desc_transfer",
    "faq_show": "btn_desc_faq",
    "credit_show": "btn_desc_credit",
    "stats_show": "btn_desc_stats",
    "titles_show": "btn_desc_titles",
    "social_menu": "btn_desc_social",
    "gang_menu": "btn_desc_gang",
    "wanted_show": "btn_desc_wanted",
    "drama_show": "btn_desc_drama",
    "world_news_show": "btn_desc_world_news",
    "invest_show": "btn_desc_invest",
    "history_show": "btn_desc_history",
    "shop_menu": "btn_desc_shop",
}


def _push_nav(context, back_to: str):
    nav = context.user_data.setdefault("nav", [])
    if nav and nav[-1] == back_to:
        return
    nav.append(back_to)
    if len(nav) > 20:
        nav.pop(0)


def _pop_nav(context) -> str:
    nav = context.user_data.get("nav", [])
    if nav:
        return nav.pop()
    return "menu_main"


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = update.effective_user
    lang = "id" if getattr(user, "language_code", "").startswith("id") else "en"

    if not query:
        await update.message.reply_text(
            t("menu_main_title", lang),
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard(lang),
        )
        return

    data = query.data

    if data not in ("_back", "menu_main", "leaderboard_show") and not data.startswith("gang_"):
        from database.user_repo import get_user_full
        full = await get_user_full(user.id)
        if full and full.get("needs_name", 0) == 1:
            await query.answer(t("menu_needs_name", lang), show_alert=True)
            return

    from services.rate_limiter import check_rate_limit as rl, get_remaining
    if user and not rl(user.id):
        await query.answer(t("menu_rate_limit", lang, remaining=get_remaining(user.id)), show_alert=True)
        return

    if data == "_back":
        data = _pop_nav(context)

    desc_key = _BTN_DESCS.get(data)
    if desc_key:
        await query.answer(text=t(desc_key, lang), show_alert=False)
    else:
        await query.answer()

    try:
        if data == "menu_main":
            await query.edit_message_text(
                t("menu_main_title", lang),
                parse_mode="Markdown",
                reply_markup=main_menu_keyboard(lang),
            )

        elif data == "menu_chaos":
            _push_nav(context, "menu_main")
            await query.edit_message_text(
                t("menu_chaos_title", lang),
                parse_mode="Markdown",
                reply_markup=chaos_menu_keyboard(lang),
            )

        elif data == "profile_show":
            _push_nav(context, "menu_main")
            from handlers.profile import build_profile_text
            text, keyboard = await build_profile_text(user, lang)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=keyboard)

        elif data == "daily_claim":
            _push_nav(context, "menu_main")
            result = await apply_daily_reward(user.id, lang)
            text = result.get("message", "")
            ach = result.get("ach_msgs", [])
            if ach:
                text += "\n\n" + "\n".join(ach)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "leaderboard_show":
            _push_nav(context, "menu_main")
            text = t("leaderboard_title", lang)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=leaderboard_menu_keyboard(lang))

        elif data.startswith("lb_") and data != "lb_buy_" and not data.startswith("lb_open_"):
            _push_nav(context, "leaderboard_show")

        elif data.startswith("lb_buy_"):
            rarity = data.replace("lb_buy_", "")
            rarity_map = {"common": "common", "rare": "rare", "epic": "epic", "leg": "legendary"}
            r = rarity_map.get(rarity, "common")
            from services.lootbox_service import buy_lootbox
            result = await buy_lootbox(user.id, r, lang)
            await query.edit_message_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data.startswith("lb_open_"):
            rarity = data.replace("lb_open_", "")
            rarity_map = {"common": "common", "rare": "rare", "epic": "epic", "leg": "legendary"}
            r = rarity_map.get(rarity, "common")
            from services.lootbox_service import open_lootbox
            result = await open_lootbox(user.id, r, lang)
            await query.edit_message_text(result["text"], parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data.startswith("lb_"):
            return

        elif data.startswith("action_"):
            action = data.replace("action_", "")
            prompts = {
                "utang": "action_prompt_utang",
                "nagih": "action_prompt_nagih",
                "jebak": "action_prompt_jebak",
                "transfer": "action_prompt_transfer",
            }
            prompt_key = prompts.get(action, "")
            if prompt_key:
                _push_nav(context, "menu_chaos")
                await query.edit_message_text(
                    t(prompt_key, lang),
                    parse_mode="Markdown",
                    reply_markup=back_to_main_keyboard(lang),
                )

        elif data == "faq_show" or data.startswith("faq_"):
            _push_nav(context, "menu_main")
            from handlers.faq import faq_callback_handler
            await faq_callback_handler(update, context)

        elif data == "credit_show":
            _push_nav(context, "menu_main")
            from handlers.credit import credit_callback
            await credit_callback(update, context)

        elif data == "stats_show":
            _push_nav(context, "menu_main")
            from handlers.stats import stats_callback
            await stats_callback(update, context)

        elif data in ("titles_show",) or data.startswith("title_select_"):
            _push_nav(context, "menu_main")
            from handlers.titles import titles_callback
            await titles_callback(update, context)

        elif data == "achievements_show":
            _push_nav(context, "menu_main")
            from database.user_repo import get_user_achievements
            from config import ACHIEVEMENTS
            ach_list = await get_user_achievements(user.id)
            text = t("menu_achievements_title", lang) + "\n\n"
            emoji_map = {
                "first_trap": "🏅", "first_collect": "🎖️", "debt_collector_1000": "💰",
                "debt_collector_5000": "🦈", "big_lender_1000": "💸", "trap_master_10": "🪤",
                "bankrupt_once": "💀", "streak_7": "🔥",
            }
            all_achs = ACHIEVEMENTS
            for aid, adata in all_achs.items():
                unlocked = aid in ach_list if ach_list else False
                symbol = "✅" if unlocked else "🔒"
                emoji = emoji_map.get(aid, "🏅")
                key = adata.get("key", aid)
                name = t(f"ach_{key}", lang).split("\n")[0]
                if name.startswith("ach_"):
                    name = aid.replace("_", " ").title()
                text += f"{symbol} {emoji} {name}\n"
            if not ach_list:
                text += t("menu_achievements_empty", lang) + "\n"
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "profile_settings":
            _push_nav(context, "profile_show")
            await query.edit_message_text(
                t("menu_profile_settings", lang),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "social_menu":
            _push_nav(context, "menu_main")
            await query.edit_message_text(
                t("menu_social_hub", lang),
                parse_mode="Markdown",
                reply_markup=social_menu_keyboard(lang),
            )

        elif data == "social_invite":
            from database.user_repo import create_invite_code
            await query.answer()
            code = await create_invite_code(user.id)
            bot_user = await context.bot.get_me()
            link = f"https://t.me/{bot_user.username}?start={code}"
            await query.edit_message_text(
                t("menu_invite_link", lang, link=link),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )
            return

        elif data == "social_contacts":
            from database.user_repo import get_contacts
            await query.answer()
            cts = await get_contacts(user.id)
            if not cts:
                text = t("contacts_empty", lang)
            else:
                lines = ["📇 *Contacts*\n"]
                for c in cts:
                    name = c.get("display_name") or c.get("username") or f"User#{c['contact_id']}"
                    if c["status"] == "pending":
                        lines.append(f"• `{c['contact_id']}` — {name} {t('contacts_pending', lang)}")
                    else:
                        lines.append(f"• `{c['contact_id']}` — {name} ✅")
                text = "\n".join(lines)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))
            return

        elif data == "gang_menu":
            _push_nav(context, "social_menu")
            await query.edit_message_text(
                t("gang_menu_title", lang),
                parse_mode="Markdown",
                reply_markup=gang_menu_keyboard(lang),
            )

        elif data.startswith("gang_"):
            from handlers.gang import gang_callback
            await gang_callback(update, context)

        elif data == "wanted_show":
            _push_nav(context, "social_menu")
            from handlers.wanted import wanted_callback
            await wanted_callback(update, context)

        elif data == "world_news_show":
            _push_nav(context, "menu_main")
            from services.world_news_service import get_world_news
            from datetime import datetime
            news = await get_world_news(lang)
            text = t("menu_world_news_header", lang, time=datetime.now().strftime('%H:%M')) + "\n\n"

            if news["active_event"]:
                ev = news["active_event"]
                mins = ev["remaining"] // 60
                title = t(ev["title"], lang)
                desc = t(ev["description"], lang)
                text += f"🔥 *{title}*\n_{desc}_\n_{t('menu_world_news_timer', lang, mins=mins)}_\n\n"

            if news["recent_drama"]:
                text += t("menu_world_news_latest", lang) + "\n"
                shown = 0
                for d in news["recent_drama"]:
                    raw = d['drama_text'].strip()
                    if '0%' in raw:
                        continue
                    if shown >= 3:
                        break
                    parts = [p.strip() for p in raw.split('\n') if p.strip()]
                    first = parts[0] if parts else raw
                    rest = ' — '.join(parts[1:]) if len(parts) > 1 else ''
                    if rest:
                        text += f"• {first} — _{rest}_\n"
                    else:
                        text += f"• {first}\n"
                    shown += 1
                if shown == 0:
                    text += t("menu_world_news_none", lang) + "\n"
                text += "\n"

            if news["prev_events"]:
                text += t("menu_world_news_history", lang) + "\n"
                for ev in news["prev_events"][:3]:
                    ttl = t(ev["title"], lang)
                    text += f"• {ttl}\n"

            await query.edit_message_text(
                text, parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "drama_show":
            _push_nav(context, "social_menu")
            from handlers.drama import drama_callback
            await drama_callback(update, context)

        elif data == "chaos_spy":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                t("menu_spy_info", lang, cost=format_money(SPY_COST, lang), fine=format_money(SPY_FAIL_FINE, lang)),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_sabo":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                t("menu_sabotage_info", lang,
                    min=format_money(SABOTAGE_STEAL_MIN, lang),
                    max=format_money(SABOTAGE_STEAL_MAX, lang),
                    cost=format_money(SABOTAGE_COST, lang),
                    fine=format_money(SABOTAGE_FAIL_FINE, lang)),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_casino":
            _push_nav(context, "menu_chaos")
            from utils.disclaimer import casino_disclaimer
            await query.edit_message_text(
                t("menu_casino_info", lang) + "\n" + casino_disclaimer(lang),
                parse_mode="Markdown",
                reply_markup=casino_menu_keyboard(lang),
            )

        elif data == "chaos_market":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                t("menu_market_info", lang),
                parse_mode="Markdown",
                reply_markup=market_menu_keyboard(lang),
            )

        elif data == "chaos_lootbox":
            _push_nav(context, "menu_chaos")
            from utils.disclaimer import lootbox_disclaimer
            lb_common = format_money(LOOTBOX_PRICES["common"], lang)
            lb_rare = format_money(LOOTBOX_PRICES["rare"], lang)
            lb_epic = format_money(LOOTBOX_PRICES["epic"], lang)
            lb_legendary = format_money(LOOTBOX_PRICES["legendary"], lang)
            await query.edit_message_text(
                t("menu_lootbox_info", lang, common=lb_common, rare=lb_rare, epic=lb_epic, legendary=lb_legendary)
                + "\n" + lootbox_disclaimer(lang),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_traps":
            _push_nav(context, "menu_chaos")
            f = lambda v: format_money(v, lang)
            await query.edit_message_text(
                t("menu_traps_info", lang, c0=f(0), c1=f(50), c2=f(100), c3=f(200), c4=f(300)),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_lunas":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                t("menu_lunas_info", lang),
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data.startswith("history_"):
            _push_nav(context, "menu_main")
            from handlers.history import history_callback
            await history_callback(update, context)

        elif data.startswith("invest_"):
            _push_nav(context, "menu_main")
            from handlers.investment import investment_callback
            await investment_callback(update, context)

        elif data == "bank_info":
            _push_nav(context, "menu_main")
            from handlers.bank import bank_callback
            await bank_callback(update, context)

        elif data in ("bank_deposit", "bank_withdraw"):
            _push_nav(context, "bank_info")
            await query.edit_message_text(
                t("menu_bank_usage", lang),
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "bank_history":
            _push_nav(context, "bank_info")
            from services.bank_service import get_bank_transactions
            text = await get_bank_transactions(user.id, lang)
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "casino_slots":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text(t("menu_casino_sub_slots", lang), reply_markup=back_to_main_keyboard(lang))
        elif data == "casino_bj":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text(t("menu_casino_sub_bj", lang), reply_markup=back_to_main_keyboard(lang))
        elif data == "casino_roulette":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text(t("menu_casino_sub_roulette", lang), reply_markup=back_to_main_keyboard(lang))

        elif data == "market_show":
            _push_nav(context, "chaos_market")
            from services.market_service import get_market_items
            items = await get_market_items()
            items_str = ""
            for item in items:
                items_str += f"• *{item['name']}* — {item['price']}💰\n  `{item['id']}`\n"
            text = t("market_help", lang, items=items_str.strip())
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "inventory_show":
            _push_nav(context, "chaos_market")
            from services.market_service import get_user_items, get_active_shields
            items = await get_user_items(user.id)
            shields = await get_active_shields(user.id)
            text = t("inventory_title", lang) + "\n\n" + t("inventory_items_header", lang) + "\n"
            if items:
                for item in items:
                    text += f"• {item['name']} x{item['quantity']}\n"
            else:
                text += t("lootbox_inv_empty", lang) + "\n"
            text += "\n" + t("inventory_shields_header", lang) + "\n"
            if shields:
                for s in shields:
                    text += f"• {s['shield_type']} (exp: {s['expires_at']})\n"
            else:
                text += t("inventory_shields_none", lang) + "\n"
            await query.edit_message_text(text, reply_markup=back_to_main_keyboard(lang))

        elif data == "npc_show":
            _push_nav(context, "social_menu")
            await query.edit_message_text(t("menu_npc_info", lang), parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data.startswith("npc_"):
            pass

        elif data == "court_show":
            _push_nav(context, "social_menu")
            await query.edit_message_text(
                t("menu_court_info", lang),
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data.startswith("court_"):
            pass

        elif data.startswith("cfm_"):
            action = data.replace("cfm_", "")
            if action.startswith("cancel_"):
                context.user_data.pop("pending_action", None)
                await query.edit_message_text(t("transfer_cancelled", lang), reply_markup=back_to_main_keyboard(lang))
                return
            pending = context.user_data.pop("pending_action", None)
            if pending and pending.get("id") == action:
                try:
                    from database.user_repo import update_balance, add_transaction
                    await update_balance(pending["from_id"], -pending["amount"])
                    await update_balance(pending["to_id"], pending["amount"])
                    await add_transaction(pending["from_id"], pending["to_name"], "transfer", pending["amount"])
                    from utils.formatter import format_money
                    await query.edit_message_text(
                        t("transfer_success_confirm", lang, amount=pending['amount_formatted'], target=pending['to_name']),
                        parse_mode="Markdown",
                        reply_markup=back_to_main_keyboard(lang),
                    )
                except Exception as e:
                    await query.edit_message_text(t("transfer_error", lang), reply_markup=back_to_main_keyboard(lang))
                    logger.error(f"Confirm transfer error: {e}")
            else:
                await query.edit_message_text(t("transfer_expired", lang), reply_markup=back_to_main_keyboard(lang))

        elif data.startswith("trap_"):
            _push_nav(context, "menu_chaos")
            trap_id = data.replace("trap_", "")
            await query.edit_message_text(
                f"🪤 Gunakan: /trap {trap_id} @username",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

    except BadRequest as e:
        if "Message is not modified" in str(e):
            pass
        else:
            logger.error(f"Callback BadRequest: {e}\n{traceback.format_exc()}")
            try:
                await query.edit_message_text(
                    t("menu_error", lang),
                    parse_mode="Markdown",
                    reply_markup=back_to_main_keyboard(lang),
                )
            except Exception:
                pass
    except Exception as e:
        logger.error(f"Callback error: {e}\n{traceback.format_exc()}")
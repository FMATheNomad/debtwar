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
            await query.answer("Kamu harus set nama dulu! Ketik /setname", show_alert=True)
            return

    from services.rate_limiter import check_rate_limit as rl, get_remaining
    if user and not rl(user.id):
        await query.answer(f"⏳ Tenang... ({get_remaining(user.id)}/40 per menit)", show_alert=True)
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
            text = "🏆 *Achievements*\n\n"
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
                text += "Belum ada achievement. Ayo main!\n"
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "profile_settings":
            _push_nav(context, "profile_show")
            await query.edit_message_text(
                "⚙️ *Pengaturan Profil*\n\n"
                "Gunakan `/setname <nama>` untuk ganti nama display.\n"
                "Contoh: `/setname Fariz Ganteng`",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "social_menu":
            _push_nav(context, "menu_main")
            await query.edit_message_text(
                "🏴 *Social Hub*\n\nPilih menu sosial:",
                parse_mode="Markdown",
                reply_markup=social_menu_keyboard(lang),
            )

        elif data == "social_invite":
            from handlers.invite import cmd_invite
            update = query
            context.args = []
            await cmd_invite(update, context)

        elif data == "social_contacts":
            from handlers.invite import cmd_contacts
            update = query
            context.args = []
            await cmd_contacts(update, context)

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
            text = f"📰 *WORLD NEWS*\n🔄 Diperbarui: {datetime.now().strftime('%H:%M')}\n\n"

            if news["active_event"]:
                ev = news["active_event"]
                mins = ev["remaining"] // 60
                title = t(ev["title"], lang)
                desc = t(ev["description"], lang)
                text += f"🔥 *{title}*\n_{desc}_\n⏳ Sisa: _{mins} menit_\n\n"

            if news["recent_drama"]:
                text += "📌 *Berita Terkini*\n"
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
                    text += "• Belum ada berita terkini.\n"
                text += "\n"

            if news["prev_events"]:
                text += "📋 *Riwayat Event*\n"
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
                "🕵️ *Spy System*\n\n"
                "Lihat estimasi saldo & utang target.\n\n"
                f"• Biaya: *{format_money(SPY_COST, lang)}*\n"
                "• Cooldown: 2 menit\n"
                "• Success rate: 70%\n"
                f"• Gagal: kena denda {format_money(SPY_FAIL_FINE, lang)}\n"
                "• Terdeteksi: target dapat notifikasi\n\n"
                "Gunakan: `/spy @username`",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_sabo":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                "💣 *Sabotage System*\n\n"
                "Tipe:\n"
                "• `freeze` — freeze akun target 1 jam\n"
                f"• `steal` — curi saldo target ({format_money(SABOTAGE_STEAL_MIN, lang)}-{format_money(SABOTAGE_STEAL_MAX, lang)})\n"
                "• `block_daily` — block daily reward target\n\n"
                f"• Biaya: *{format_money(SABOTAGE_COST, lang)}*\n"
                "• Cooldown: 5 menit\n"
                "• Success rate: 55%\n"
                f"• Gagal: kena denda {format_money(SABOTAGE_FAIL_FINE, lang)}\n\n"
                "Gunakan: `/sabotage <type> @username`",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_casino":
            _push_nav(context, "menu_chaos")
            from utils.disclaimer import CASINO_DISCLAIMER
            await query.edit_message_text(
                f"🎰 *Casino Debt War*\n\n"
                f"Gunakan:\n/slots <bet>\n/bj <bet>\n/roulette <bet> <choice>\n"
                f"{CASINO_DISCLAIMER}",
                parse_mode="Markdown",
                reply_markup=casino_menu_keyboard(lang),
            )

        elif data == "chaos_market":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                "🏪 /market — Lihat shop\n/buy <item> — Beli item\n/inv — Inventory",
                parse_mode="Markdown",
                reply_markup=market_menu_keyboard(lang),
            )

        elif data == "chaos_lootbox":
            _push_nav(context, "menu_chaos")
            from utils.disclaimer import LOOTBOX_DISCLAIMER
            lb_common = format_money(LOOTBOX_PRICES["common"], lang)
            lb_rare = format_money(LOOTBOX_PRICES["rare"], lang)
            lb_epic = format_money(LOOTBOX_PRICES["epic"], lang)
            lb_legendary = format_money(LOOTBOX_PRICES["legendary"], lang)
            await query.edit_message_text(
                "🎁 *Lootbox System*\n\n"
                "Buka lootbox untuk dapat hadiah random!\n\n"
                f"• Common — {lb_common} (uang, debt bomb)\n"
                f"• Rare — {lb_rare} (uang, shield)\n"
                f"• Epic — {lb_epic} (uang besar, chaos buff)\n"
                f"• Legendary — {lb_legendary} (uang gede, title unlock)\n\n"
                "Gunakan:\n/lootbox buy <rarity>\n/lootbox open <rarity>\n"
                f"{LOOTBOX_DISCLAIMER}",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_traps":
            _push_nav(context, "menu_chaos")
            f = lambda v: format_money(v, lang)
            await query.edit_message_text(
                "🪤 *Advanced Traps*\n\n"
                "Gunakan: `/trap <type> @user`\n\n"
                f"• `fake_investment` — 35% | 80-300 dmg | {f(0)}\n"
                f"• `phishing_trap` — 40% | 60-200 dmg | {f(50)}\n"
                f"• `tax_trap` — 30% | 100-400 dmg | {f(100)}\n"
                f"• `pyramid_scheme` — 25% | 150-500 dmg | {f(200)}\n"
                f"• `mafia_extortion` — 20% | 200-800 dmg | {f(300)}\n\n"
                "Ketik `/traps` untuk detail lengkap.",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "chaos_lunas":
            _push_nav(context, "menu_chaos")
            await query.edit_message_text(
                "💳 Gunakan: /lunas <jumlah> @player\n"
                "Contoh:\n/lunas 500 — bayar ke sistem\n"
                "/lunas 500 @user — bayar langsung ke player\n"
                "/lunas — lunasin semua",
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
                "🏦 Gunakan:\n/bank deposit <jumlah>\n/bank withdraw <jumlah>",
                parse_mode="Markdown",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data == "casino_slots":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text("🎰 Gunakan: /slots <bet>", reply_markup=back_to_main_keyboard(lang))
        elif data == "casino_bj":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text("🃏 Gunakan: /bj <bet>", reply_markup=back_to_main_keyboard(lang))
        elif data == "casino_roulette":
            _push_nav(context, "chaos_casino")
            await query.edit_message_text("🎱 Gunakan: /roulette <bet> <red/black/even/odd/number>", reply_markup=back_to_main_keyboard(lang))

        elif data == "market_show":
            _push_nav(context, "chaos_market")
            from services.market_service import get_market_items
            items = await get_market_items()
            text = "🏪 *Market / Shop*\n\n"
            for item in items:
                text += f"• *{item['name']}* — {item['price']}💰\n  `{item['id']}`\n"
            text += "\nGunakan: /buy <item_id>\nContoh: /buy shield_basic"
            await query.edit_message_text(text, parse_mode="Markdown", reply_markup=back_to_main_keyboard(lang))

        elif data == "inventory_show":
            _push_nav(context, "chaos_market")
            from services.market_service import get_user_items, get_active_shields
            items = await get_user_items(user.id)
            shields = await get_active_shields(user.id)
            text = "🎒 INVENTORY\n\nItems:\n"
            if items:
                for item in items:
                    text += f"• {item['name']} x{item['quantity']}\n"
            else:
                text += "(kosong)\n"
            text += "\nActive Shields:\n"
            if shields:
                for s in shields:
                    text += f"• {s['shield_type']} (exp: {s['expires_at']})\n"
            else:
                text += "(tidak ada)\n"
            await query.edit_message_text(text, reply_markup=back_to_main_keyboard(lang))

        elif data == "npc_show":
            _push_nav(context, "social_menu")
            await query.edit_message_text(
                "🤖 Gunakan: /npc <id> <action>\n"
                "Contoh: /npc loan_shark borrow",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data.startswith("npc_"):
            pass

        elif data == "court_show":
            _push_nav(context, "social_menu")
            await query.edit_message_text(
                "🏛️ Gunakan:\n/sue @user <tuduhan>\n/vote <case_id> <guilty/innocent>",
                reply_markup=back_to_main_keyboard(lang),
            )

        elif data.startswith("court_"):
            pass

        elif data.startswith("cfm_"):
            action = data.replace("cfm_", "")
            if action.startswith("cancel_"):
                context.user_data.pop("pending_action", None)
                await query.edit_message_text("❌ Dibatalkan.", reply_markup=back_to_main_keyboard(lang))
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
                        f"✅ *Transfer Berhasil!*\n{pending['amount_formatted']} ke @{pending['to_name']}",
                        parse_mode="Markdown",
                        reply_markup=back_to_main_keyboard(lang),
                    )
                except Exception as e:
                    await query.edit_message_text("⚠️ Gagal memproses transaksi.", reply_markup=back_to_main_keyboard(lang))
                    logger.error(f"Confirm transfer error: {e}")
            else:
                await query.edit_message_text("⏳ Waktu habis atau aksi kadaluarsa.", reply_markup=back_to_main_keyboard(lang))

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
                    "\u26a0\ufe0f Terjadi error. Silakan coba lagi.",
                    parse_mode="Markdown",
                    reply_markup=back_to_main_keyboard(lang),
                )
            except Exception:
                pass
    except Exception as e:
        logger.error(f"Callback error: {e}\n{traceback.format_exc()}")
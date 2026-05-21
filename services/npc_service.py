import logging
import random
from database.db import get_connection
from database.user_repo import get_user_full, update_balance, update_debt
from config import NPC_LOAN_SHARK_MAX, NPC_LOAN_SHARK_INTEREST, NPC_MISSION_COST_MIN, NPC_MISSION_COST_MAX, NPC_MISSION_REWARD_MIN, NPC_MISSION_REWARD_MAX
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)

NPCS = {
    "loan_shark": {
        "name": "Boris si Rentenir",
        "desc": "🧛 Pinjaman kilat, bunga tinggi. Jangan macet ya.",
    },
    "mafia_boss": {
        "name": "Don Corleone",
        "desc": "🕴️ Bos mafia. Punya misi-misi gelap.",
    },
    "scammer": {
        "name": "Jimmy Tipu",
        "desc": "🐍 Ahli phishing. Awas dompetmu!",
    },
    "collector": {
        "name": "Rambo Collector",
        "desc": "💪 Tukang tagih. Bisa bantu nagih utang orang lain.",
    },
}


async def get_npc_info(npc_id: str, lang: str) -> str:
    npc = NPCS.get(npc_id)
    if not npc:
        return None
    name = t(f"npc_{npc_id}_name", lang)
    desc = t(f"npc_{npc_id}_desc", lang)
    return f"*{name}*\n{desc}"


async def interact_npc(user_id: int, npc_id: str, action: str, lang: str) -> dict:
    npc = NPCS.get(npc_id)
    if not npc:
        return {"ok": False, "text": t("npc_not_found", lang)}

    user = await get_user_full(user_id)
    if not user:
        return {"ok": False, "text": t("not_registered", lang)}

    from database.user_repo import add_transaction

    if npc_id == "loan_shark":
        if action == "borrow":
            amount = random.randint(100, NPC_LOAN_SHARK_MAX)
            await update_balance(user_id, amount)
            await update_debt(user_id, int(amount * (1 + NPC_LOAN_SHARK_INTEREST)))
            await log_interaction(user_id, npc_id, "borrow", amount)
            await add_transaction(user_id, f"npc_{npc_id}", "borrow", amount)
            return {
                "ok": True,
                "text": f"🧛 *{t('npc_loan_shark_name', lang)}*\n\n"
                        f"\"{t('npc_loan_shark_borrow', lang, amount=format_money(amount, lang), interest=int(NPC_LOAN_SHARK_INTEREST*100))}\"\n\n"
                        f"{t('npc_loan_shark_borrow_received', lang, amount=format_money(amount, lang))}"
                        f"\n{t('npc_loan_shark_borrow_debt', lang, amount=format_money(int(amount * NPC_LOAN_SHARK_INTEREST), lang))}",
            }
        elif action == "pay":
            debt = user["debt"]
            if debt <= 0:
                return {"ok": False, "text": t("npc_loan_shark_no_debt", lang)}
            if user["balance"] < debt:
                return {"ok": False, "text": t("npc_loan_shark_insufficient", lang, debt=format_money(debt, lang), balance=format_money(user['balance'], lang))}
            await update_balance(user_id, -debt)
            await update_debt(user_id, -debt)
            await log_interaction(user_id, npc_id, "pay", debt)
            await add_transaction(user_id, f"npc_{npc_id}", "pay", debt)
            return {
                "ok": True,
                "text": f"🧛 *{t('npc_loan_shark_name', lang)}*\n\n"
                        f"\"{t('npc_loan_shark_pay_success', lang, amount=format_money(debt, lang))}\"\n\n"
                        f"{t('npc_loan_shark_paid_off', lang)}",
            }

    elif npc_id == "mafia_boss":
        if action == "mission":
            cost = random.randint(NPC_MISSION_COST_MIN, NPC_MISSION_COST_MAX)
            if user["balance"] < cost:
                return {
                    "ok": False,
                    "text": f"🕴️ *{t('npc_mafia_boss_name', lang)}*\n\n"
                            f"\"{t('npc_mafia_insufficient', lang, cost=format_money(cost, lang))}\"",
                }

            await update_balance(user_id, -cost)

            if random.random() < 0.15:
                await log_interaction(user_id, npc_id, "mission_fail", -cost)
                await add_transaction(user_id, f"npc_{npc_id}", "mission_fail", cost)
                return {
                    "ok": True,
                    "text": f"🕴️ *{t('npc_mafia_boss_name', lang)}*\n\n"
                            f"\"{t('npc_mafia_fail', lang, cost=format_money(cost, lang))}\"\n\n"
                            f"{t('npc_mafia_fail_label', lang, cost=format_money(cost, lang))}",
                }

            reward = random.randint(NPC_MISSION_REWARD_MIN, NPC_MISSION_REWARD_MAX)
            await update_balance(user_id, reward)
            await log_interaction(user_id, npc_id, "mission", reward - cost)
            await add_transaction(user_id, f"npc_{npc_id}", "mission", reward)
            missions = [
                "npc_mission_burn_shop",
                "npc_mission_collect_debt",
                "npc_mission_steal_data",
                "npc_mission_sabotage",
                "npc_mission_protect_boss",
            ]
            mission_key = random.choice(missions)
            mission = t(mission_key, lang)
            net = reward - cost
            sign = "+" if net >= 0 else ""
            return {
                "ok": True,
                "text": f"🕴️ *{t('npc_mafia_boss_name', lang)}*\n\n"
                        f"\"{t('npc_mafia_mission_accept', lang, mission=mission)}\"\n\n"
                        f"{t('npc_mission_cost_label', lang, cost=format_money(cost, lang))}\n"
                        f"{t('npc_mission_reward_label', lang, reward=format_money(reward, lang))}\n"
                        f"{t('npc_mission_total_label', lang, total=sign + format_money(net, lang))}",
            }

    elif npc_id == "scammer":
        if action == "phish":
            if random.random() < 0.4:
                loss = random.randint(50, 200)
                await update_balance(user_id, -loss)
                await log_interaction(user_id, npc_id, "phish_fail", -loss)
                await add_transaction(user_id, f"npc_{npc_id}", "phish_fail", loss)
                return {
                    "ok": True,
                    "text": f"🐍 *{t('npc_scammer_name', lang)}*\n\n"
                            f"\"{t('npc_scammer_fail', lang, loss=format_money(loss, lang))}\"",
                }
            else:
                gain = random.randint(30, 150)
                await update_balance(user_id, gain)
                await log_interaction(user_id, npc_id, "phish_success", gain)
                await add_transaction(user_id, f"npc_{npc_id}", "phish_success", gain)
                return {
                    "ok": True,
                    "text": f"🐍 *{t('npc_scammer_name', lang)}*\n\n"
                            f"\"{t('npc_scammer_success', lang, gain=format_money(gain, lang))}\"",
                }

    elif npc_id == "collector":
        if action == "help_collect":
            from database.user_repo import get_user_full as guf
            from services.economy import apply_nagih
            from database.user_repo import get_all_debtors
            debtors = await get_all_debtors()
            if not debtors:
                return {"ok": False, "text": t("npc_collector_no_debtors", lang)}
            target = random.choice(debtors)
            amount = target["debt"]
            if amount <= 0:
                return {"ok": False, "text": t("npc_collector_no_debt", lang)}
            fee = int(amount * 0.3)
            net = amount - fee
            await update_balance(user_id, net)
            await update_debt(target["id"], -amount)
            await log_interaction(user_id, npc_id, "collect", net)
            await add_transaction(user_id, f"npc_{npc_id}", "collect", net)
            return {
                "ok": True,
                "text": f"💪 *{t('npc_collector_name', lang)}*\n\n"
                        f"\"{t('npc_collector_success', lang, target=target['username'], amount=format_money(amount, lang))}\"\n\n"
                        f"{t('npc_collector_received', lang, net=format_money(net, lang))}",
            }

    npc_name = t(f"npc_{npc_id}_name", lang)
    return {"ok": False, "text": t("npc_action_unknown", lang).format(npc_name)}


async def log_interaction(user_id: int, npc_type: str, action: str, reward: int):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO npc_interactions (user_id, npc_type, action, reward) VALUES (?, ?, ?, ?)",
            (user_id, npc_type, action, reward),
        )
        await conn.commit()
    finally:
        await conn.close()

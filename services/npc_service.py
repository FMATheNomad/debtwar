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
    return f"*{npc['name']}*\n{npc['desc']}"


async def interact_npc(user_id: int, npc_id: str, action: str, lang: str) -> dict:
    npc = NPCS.get(npc_id)
    if not npc:
        return {"ok": False, "text": "NPC tidak dikenal."}

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
                "text": f"🧛 *{npc['name']}*\n\n"
                        f"\"Pinjem {format_money(amount, lang)}? OK, plus bunga {int(NPC_LOAN_SHARK_INTEREST*100)}%. "
                        f"Jangan lupa bayar ya... atau... 😈\"\n\n"
                        f"💸 Diterima: +{format_money(amount, lang)}"
                        f"\n💳 Utang: +{format_money(int(amount * NPC_LOAN_SHARK_INTEREST), lang)} (bunga)",
            }
        elif action == "pay":
            debt = user["debt"]
            if debt <= 0:
                return {"ok": False, "text": "Kamu tidak punya utang ke Boris."}
            if user["balance"] < debt:
                return {"ok": False, "text": f"Saldo tidak cukup! Utangmu {format_money(debt, lang)}, saldomu {format_money(user['balance'], lang)}."}
            await update_balance(user_id, -debt)
            await update_debt(user_id, -debt)
            await log_interaction(user_id, npc_id, "pay", debt)
            await add_transaction(user_id, f"npc_{npc_id}", "pay", debt)
            return {
                "ok": True,
                "text": f"🧛 *{npc['name']}*\n\n"
                        f"\"Lunas. {format_money(debt, lang)} diterima. Pintu selalu terbuka untukmu...\"\n\n"
                        f"✅ Utang lunas!",
            }

    elif npc_id == "mafia_boss":
        if action == "mission":
            cost = random.randint(NPC_MISSION_COST_MIN, NPC_MISSION_COST_MAX)
            if user["balance"] < cost:
                return {
                    "ok": False,
                    "text": f"🕴️ *{npc['name']}*\n\n"
                            f"\"Misi butuh modal {format_money(cost, lang)} untuk suap dan peralatan. "
                            f"Saldomu tidak cukup. Kembali kalau sudah punya duit.\"",
                }

            await update_balance(user_id, -cost)

            if random.random() < 0.15:
                await log_interaction(user_id, npc_id, "mission_fail", -cost)
                await add_transaction(user_id, f"npc_{npc_id}", "mission_fail", cost)
                return {
                    "ok": True,
                    "text": f"🕴️ *{npc['name']}*\n\n"
                            f"\"Misi gagal! Informasi bocor, target kabur. "
                            f"Kamu kehilangan modal {format_money(cost, lang)}. "
                            f"Hilang dari sini sebelum bos marah.\"\n\n"
                            f"❌ Rugi: -{format_money(cost, lang)}",
                }

            reward = random.randint(NPC_MISSION_REWARD_MIN, NPC_MISSION_REWARD_MAX)
            await update_balance(user_id, reward)
            await log_interaction(user_id, npc_id, "mission", reward - cost)
            await add_transaction(user_id, f"npc_{npc_id}", "mission", reward)
            missions = [
                "Bakar warung saingan",
                "Tagih utang ke Debtor",
                "Curi data nasabah bank",
                "Sabotase gang lawan",
                "Lindungi bos dari raid",
            ]
            mission = random.choice(missions)
            net = reward - cost
            return {
                "ok": True,
                "text": f"🕴️ *{npc['name']}*\n\n"
                        f"\"Ada misi untukmu: *{mission}*. Lakukan diam-diam.\"\n\n"
                        f"💸 Modal: -{format_money(cost, lang)}\n"
                        f"💰 Reward: +{format_money(reward, lang)}\n"
                        f"📊 Total: {'+' if net >= 0 else ''}{format_money(net, lang)}",
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
                    "text": f"🐍 *{npc['name']}*\n\n"
                            f"\"Hehe, kena tipu! Kamu kehilangan {format_money(loss, lang)}. Next time jangan percaya orang kayak aku.\"",
                }
            else:
                gain = random.randint(30, 150)
                await update_balance(user_id, gain)
                await log_interaction(user_id, npc_id, "phish_success", gain)
                await add_transaction(user_id, f"npc_{npc_id}", "phish_success", gain)
                return {
                    "ok": True,
                    "text": f"🐍 *{npc['name']}*\n\n"
                            f"\"Kamu berhasil membalikkan tipuan! Dapet {format_money(gain, lang)} dari si penipu.\"",
                }

    elif npc_id == "collector":
        if action == "help_collect":
            from database.user_repo import get_user_full as guf
            from services.economy import apply_nagih
            from database.user_repo import get_all_debtors
            debtors = await get_all_debtors()
            if not debtors:
                return {"ok": False, "text": "Tidak ada yang punya utang saat ini."}
            target = random.choice(debtors)
            amount = target["debt"]
            if amount <= 0:
                return {"ok": False, "text": "Target tidak punya utang."}
            fee = int(amount * 0.3)
            net = amount - fee
            await update_balance(user_id, net)
            await update_debt(target["id"], -amount)
            await log_interaction(user_id, npc_id, "collect", net)
            await add_transaction(user_id, f"npc_{npc_id}", "collect", net)
            return {
                "ok": True,
                "text": f"💪 *{npc['name']}*\n\n"
                        f"\"Beres! Aku tagih @{target['username']} sebesar {format_money(amount, lang)}. "
                        f"Fee ku 30% ya.\"\n\n"
                        f"💰 Kamu terima: {format_money(net, lang)}",
            }

    return {"ok": False, "text": f"*{npc['name']}* tidak mengerti perintah itu."}


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

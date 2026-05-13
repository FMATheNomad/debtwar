import logging
import random
from database.db import get_connection
from database.user_repo import update_balance, get_user_full
from config import CASINO_MIN_BET, CASINO_MAX_BET, CASINO_RTP
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)

SLOT_SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "💎", "7️⃣", "⭐"]
SLOT_PAYOUTS = {
    "🍒🍒🍒": 3, "🍋🍋🍋": 5, "🍊🍊🍊": 8,
    "🍇🍇🍇": 10, "💎💎💎": 15, "7️⃣7️⃣7️⃣": 25, "⭐⭐⭐": 50,
    "7️⃣7️⃣⭐": 10, "⭐⭐7️⃣": 15, "💎💎7️⃣": 8,
}


async def play_slots(user_id: int, bet: int, lang: str) -> dict:
    if bet < CASINO_MIN_BET or bet > CASINO_MAX_BET:
        return {"ok": False, "text": t("casino_bet_range", lang, min=CASINO_MIN_BET, max=CASINO_MAX_BET)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < bet:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    await update_balance(user_id, -bet)
    await update_casino_stat(user_id, "slot_plays", bet)

    reels = [random.choice(SLOT_SYMBOLS) for _ in range(3)]
    result_str = " | ".join(reels)

    win_multiplier = SLOT_PAYOUTS.get("".join(reels), 0)

    if random.random() > CASINO_RTP and win_multiplier > 0:
        if random.random() < 0.3:
            win_multiplier = 0

    winnings = int(bet * win_multiplier) if win_multiplier > 0 else 0

    if winnings > 0:
        await update_balance(user_id, winnings)
        await update_casino_stat(user_id, "slot_wins", winnings)
        net = winnings - bet
        text = (
            f"🎰 *SLOTS*\n\n"
            f"{result_str}\n\n"
            f"✅ *KAMU MENANG {format_money(winnings, lang)}!* "
            f"({'+' if net >= 0 else ''}{format_money(net, lang)})"
        )
    else:
        await update_casino_stat(user_id, "slot_losses", bet)
        text = (
            f"🎰 *SLOTS*\n\n"
            f"{result_str}\n\n"
            f"❌ Kalah {format_money(bet, lang)}. Coba lagi!"
        )

    return {"ok": True, "text": text}


async def play_blackjack(user_id: int, bet: int, lang: str) -> dict:
    if bet < CASINO_MIN_BET or bet > CASINO_MAX_BET:
        return {"ok": False, "text": t("casino_bet_range", lang, min=CASINO_MIN_BET, max=CASINO_MAX_BET)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < bet:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    await update_balance(user_id, -bet)
    await update_casino_stat(user_id, "blackjack_plays", bet)

    player = sum(random.randint(1, 10) for _ in range(2))
    dealer = sum(random.randint(1, 10) for _ in range(2))

    if player > 21:
        player = 0

    dealer_hit = dealer < 17
    while dealer_hit:
        dealer += random.randint(1, 10)
        if dealer > 21:
            dealer = 0
            break
        dealer_hit = dealer < 17

    if player > dealer:
        winnings = int(bet * 2)
        await update_balance(user_id, winnings)
        await update_casino_stat(user_id, "blackjack_wins", winnings)
        net = winnings - bet
        text = (
            f"🃏 *BLACKJACK*\n\n"
            f"Kamu: {player} | Dealer: {dealer}\n\n"
            f"✅ *MENANG!* +{format_money(net, lang)}"
        )
    elif player == dealer:
        await update_balance(user_id, bet)
        text = (
            f"🃏 *BLACKJACK*\n\n"
            f"Kamu: {player} | Dealer: {dealer}\n\n"
            f"🤝 *SERI!* Uang kembali."
        )
    else:
        await update_casino_stat(user_id, "blackjack_losses", bet)
        text = (
            f"🃏 *BLACKJACK*\n\n"
            f"Kamu: {player} | Dealer: {dealer}\n\n"
            f"❌ *KALAH!* -{format_money(bet, lang)}"
        )

    return {"ok": True, "text": text}


async def play_roulette(user_id: int, bet: int, choice: str, lang: str) -> dict:
    if bet < CASINO_MIN_BET or bet > CASINO_MAX_BET:
        return {"ok": False, "text": t("casino_bet_range", lang, min=CASINO_MIN_BET, max=CASINO_MAX_BET)}

    user = await get_user_full(user_id)
    if not user or user["balance"] < bet:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    await update_balance(user_id, -bet)
    await update_casino_stat(user_id, "roulette_plays", bet)

    number = random.randint(0, 36)
    color = "merah" if number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] else "hitam"
    if number == 0:
        color = "hijau"

    win = False
    multiplier = 0
    if choice == "red" and color == "merah":
        win, multiplier = True, 2
    elif choice == "black" and color == "hitam":
        win, multiplier = True, 2
    elif choice == "even" and number > 0 and number % 2 == 0:
        win, multiplier = True, 2
    elif choice == "odd" and number % 2 == 1:
        win, multiplier = True, 2
    elif choice == str(number):
        win, multiplier = True, 36

    result_str = f"🎱 *{number}* ({color})"

    if win:
        winnings = bet * multiplier
        await update_balance(user_id, winnings)
        await update_casino_stat(user_id, "roulette_wins", winnings)
        net = winnings - bet
        text = f"{result_str}\n\n✅ *MENANG!* +{format_money(net, lang)}"
    else:
        await update_casino_stat(user_id, "roulette_losses", bet)
        text = f"{result_str}\n\n❌ *KALAH!* -{format_money(bet, lang)}"

    return {"ok": True, "text": text}


async def update_casino_stat(user_id: int, stat: str, amount: int):
    conn = await get_connection()
    try:
        await conn.execute(
            f"INSERT INTO casino_stats (user_id, {stat}) VALUES (?, ?) "
            f"ON CONFLICT(user_id) DO UPDATE SET {stat} = {stat} + ?",
            (user_id, amount, amount),
        )
        await conn.commit()
    finally:
        await conn.close()


async def get_casino_stats(user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM casino_stats WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            return dict(row) if row else {
                "total_bet": 0, "total_won": 0, "total_lost": 0,
                "slot_plays": 0, "blackjack_plays": 0, "roulette_plays": 0,
            }
    finally:
        await conn.close()

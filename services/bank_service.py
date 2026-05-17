import logging
from datetime import datetime
from database.db import get_connection
from database.user_repo import get_user_full, update_balance, add_transaction
from config import BANK_INTEREST_RATE, BANK_WITHDRAW_FEE, BANK_MAX_BALANCE
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)


async def get_bank_account(user_id: int) -> dict:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM bank_accounts WHERE user_id = ?", (user_id,)
        ) as cur:
            row = await cur.fetchone()
            if row:
                return dict(row)
            await conn.execute(
                "INSERT INTO bank_accounts (user_id) VALUES (?)", (user_id,)
            )
            await conn.commit()
            return {"user_id": user_id, "balance": 0, "last_interest": None, "total_deposited": 0, "total_withdrawn": 0, "total_interest": 0}
    finally:
        await conn.close()


async def bank_deposit(user_id: int, amount: int, lang: str) -> dict:
    user = await get_user_full(user_id)
    if not user or user["balance"] < amount:
        return {"ok": False, "text": t("insufficient_balance", lang, balance=format_money(user.get("balance", 0) if user else 0, lang))}

    account = await get_bank_account(user_id)
    if account["balance"] + amount > BANK_MAX_BALANCE:
        return {"ok": False, "text": t("bank_max_deposit", lang, max=format_money(BANK_MAX_BALANCE, lang))}

    conn = await get_connection()
    try:
        await update_balance(user_id, -amount)
        await conn.execute(
            "UPDATE bank_accounts SET balance = balance + ?, total_deposited = total_deposited + ? WHERE user_id = ?",
            (amount, amount, user_id),
        )
        await conn.commit()
    finally:
        await conn.close()

    await add_transaction(user_id, "bank", "deposit", amount)

    return {"ok": True, "text": t("bank_deposited", lang, amount=format_money(amount, lang), balance=format_money(account["balance"] + amount, lang))}


async def bank_withdraw(user_id: int, amount: int, lang: str) -> dict:
    account = await get_bank_account(user_id)
    if account["balance"] < amount:
        return {"ok": False, "text": t("bank_insufficient", lang, balance=format_money(account["balance"], lang))}

    fee = int(amount * BANK_WITHDRAW_FEE)
    net = amount - fee
    if net <= 0:
        return {"ok": False, "text": t("bank_withdraw_fee_too_high", lang)}

    conn = await get_connection()
    try:
        await conn.execute(
            "UPDATE bank_accounts SET balance = balance - ?, total_withdrawn = total_withdrawn + ? WHERE user_id = ?",
            (amount, amount, user_id),
        )
        await update_balance(user_id, net)
        await conn.commit()
    finally:
        await conn.close()

    await add_transaction(user_id, "bank", "withdraw", net)

    return {"ok": True, "text": t("bank_withdrawn", lang, amount=format_money(amount, lang), net=format_money(net, lang), fee=format_money(fee, lang))}


async def get_bank_info(user_id: int, lang: str) -> str:
    account = await get_bank_account(user_id)
    user = await get_user_full(user_id)
    balance = user["balance"] if user else 0
    total_interest = account.get("total_interest", 0)

    return (
        f"🏦 *Bank Sentral Debt War*\n\n"
        f"💳 Saldo Rekening: *{format_money(account['balance'], lang)}*\n"
        f"👛 Saldo Dompet: *{format_money(balance, lang)}*\n"
        f"📈 Total Deposit: {format_money(account['total_deposited'], lang)}\n"
        f"📉 Total Withdraw: {format_money(account['total_withdrawn'], lang)}\n"
        f"📊 Keuntungan Bunga: *{format_money(total_interest, lang)}*\n"
        f"💸 Bunga: {BANK_INTEREST_RATE*100}% per hari\n"
        f"🏧 Fee Withdraw: {BANK_WITHDRAW_FEE*100}%\n"
        f"📦 Max Rekening: {format_money(BANK_MAX_BALANCE, lang)}\n\n"
        f"Gunakan:\n/bank deposit <jumlah>\n/bank withdraw <jumlah>"
    )


async def get_bank_transactions(user_id: int, lang: str) -> str:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT type, amount, timestamp FROM transactions WHERE from_id = ? AND to_user = 'bank' ORDER BY timestamp DESC LIMIT 20",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
    finally:
        await conn.close()

    account = await get_bank_account(user_id)
    total_interest = account.get("total_interest", 0)

    if not rows:
        return (
            f"🏦 *Riwayat Bank*\n\n"
            f"Belum ada transaksi.\n"
            f"📊 Total Keuntungan Bunga: {format_money(total_interest, lang)}"
        )

    lines = [f"🏦 *Riwayat Bank*\n"]
    for r in rows:
        icon = "📥" if r["type"] == "deposit" else "📤" if r["type"] == "withdraw" else "💸"
        lines.append(f"{icon} {r['type'].upper()} — {format_money(r['amount'], lang)}")
    lines.append(f"\n📊 Total Keuntungan Bunga: *{format_money(total_interest, lang)}*")

    return "\n".join(lines)


async def process_bank_interest():
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT user_id, balance FROM bank_accounts WHERE balance > 0"
        ) as cur:
            accounts = await cur.fetchall()

        for acc in accounts:
            interest = int(acc["balance"] * BANK_INTEREST_RATE / 12)
            if interest > 0:
                await conn.execute(
                    "UPDATE bank_accounts SET balance = balance + ?, total_interest = COALESCE(total_interest, 0) + ?, last_interest = datetime('now', 'localtime') WHERE user_id = ?",
                    (interest, interest, acc["user_id"]),
                )
        await conn.commit()
        return len(accounts)
    finally:
        await conn.close()




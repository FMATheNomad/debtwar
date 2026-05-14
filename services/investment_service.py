import logging
import random
from datetime import datetime
from database.db import get_connection
from database.user_repo import update_balance, get_user_full
from utils.formatter import format_money
from utils.translator import t

logger = logging.getLogger(__name__)

INSTRUMENT_LABELS = {
    "stock": "Saham",
    "mutual_fund": "Reksadana",
    "bond": "Obligasi",
}


async def get_all_prices():
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM investment_prices ORDER BY instrument_type, instrument_name"
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]
    finally:
        await conn.close()


async def get_instruments_by_type(itype: str) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM investment_prices WHERE instrument_type = ? ORDER BY instrument_name",
            (itype,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]
    finally:
        await conn.close()


async def get_portfolio(user_id: int) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM ("
            "SELECT ip.instrument_type, ip.instrument_id, ip.instrument_name, ip.current_price, "
            "COALESCE(SUM(iv.shares), 0) as shares, "
            "COALESCE(SUM(iv.total_invested), 0) as total_invested "
            "FROM investment_prices ip "
            "LEFT JOIN investment_portfolios iv ON ip.instrument_id = iv.instrument_id "
            "AND ip.instrument_type = iv.instrument_type AND iv.user_id = ? "
            "GROUP BY ip.instrument_type, ip.instrument_id, ip.instrument_name, ip.current_price"
            ") sub WHERE shares > 0",
            (user_id,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(r) for r in rows]
    finally:
        await conn.close()


async def buy_instrument(user_id: int, itype: str, iid: str, amount: int, lang: str) -> dict:
    from database.user_repo import add_transaction

    user = await get_user_full(user_id)
    if not user or user["balance"] < amount:
        bal = format_money(user["balance"] if user else 0, lang)
        return {"ok": False, "text": f"Saldo gak cukup. Kamu cuma punya {bal}."}

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT * FROM investment_prices WHERE instrument_type = ? AND instrument_id = ?",
            (itype, iid),
        ) as cur:
            instr = await cur.fetchone()

        if not instr:
            return {"ok": False, "text": "Instrumen gak ditemukan."}

        price = instr["current_price"]
        shares = amount / price

        await conn.execute(
            "UPDATE users SET balance = MAX(0, balance - ?) WHERE id = ?",
            (amount, user_id),
        )
        await conn.execute(
            "INSERT INTO investment_portfolios (user_id, instrument_type, instrument_id, shares, total_invested) VALUES (?, ?, ?, ?, ?)",
            (user_id, itype, iid, shares, amount),
        )
        await conn.commit()

        await add_transaction(user_id, instr["instrument_name"], "invest_buy", amount)

        return {
            "ok": True,
            "text": f"✅ Dibeli {shares:.2f} unit {instr['instrument_name']} seharga {format_money(amount, lang)}.",
        }
    finally:
        await conn.close()


async def sell_instrument(user_id: int, itype: str, iid: str, lang: str) -> dict:
    from database.user_repo import add_transaction

    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT SUM(shares) as total_shares, SUM(total_invested) as total_invested "
            "FROM investment_portfolios WHERE user_id = ? AND instrument_type = ? AND instrument_id = ?",
            (user_id, itype, iid),
        ) as cur:
            holding = await cur.fetchone()

        if not holding or not holding["total_shares"] or holding["total_shares"] <= 0:
            return {"ok": False, "text": "Kamu gak punya instrumen ini."}

        async with conn.execute(
            "SELECT * FROM investment_prices WHERE instrument_type = ? AND instrument_id = ?",
            (itype, iid),
        ) as cur:
            instr = await cur.fetchone()
            if not instr:
                return {"ok": False, "text": "Instrumen gak ditemukan."}

        current_price = instr["current_price"]
        total_value = int(holding["total_shares"] * current_price)

        await conn.execute(
            "UPDATE users SET balance = balance + ? WHERE id = ?",
            (total_value, user_id),
        )
        await conn.execute(
            "DELETE FROM investment_portfolios WHERE user_id = ? AND instrument_type = ? AND instrument_id = ?",
            (user_id, itype, iid),
        )
        await conn.commit()

        await add_transaction(user_id, instr["instrument_name"], "invest_sell", total_value)

        profit = total_value - holding["total_invested"]
        pnl = f"+{format_money(profit, lang)}" if profit >= 0 else format_money(profit, lang)
        return {
            "ok": True,
            "text": f"✅ Dijual {holding['total_shares']:.2f} unit {instr['instrument_name']}.\n"
            f"Diterima: {format_money(total_value, lang)} ({pnl})",
        }
    finally:
        await conn.close()


async def simulate_prices():
    from services.world_event_service import get_active_event
    event = await get_active_event()
    event_mult = event["multiplier"] if event else 1.0

    conn = await get_connection()
    try:
        async with conn.execute("SELECT * FROM investment_prices") as cur:
            instruments = await cur.fetchall()

        for instr in instruments:
            price = instr["current_price"]
            itype = instr["instrument_type"]

            if itype == "bond":
                change = random.uniform(-0.001, 0.005) * price
            elif itype == "mutual_fund":
                change = random.uniform(-0.02, 0.03) * price * event_mult
            else:
                change = random.uniform(-0.05, 0.06) * price * event_mult

            new_price = max(1, price + change)
            await conn.execute(
                "UPDATE investment_prices SET current_price = ?, previous_price = ?, updated_at = NOW() WHERE instrument_type = ? AND instrument_id = ?",
                (round(new_price, 2), round(price, 2), itype, instr["instrument_id"]),
            )

        await conn.commit()
    finally:
        await conn.close()

import logging
import random
from datetime import datetime
from database.db import get_connection

logger = logging.getLogger(__name__)

DRAMA_TEMPLATES = [
    "{user} baru saja menipu {count} orang dalam 10 menit. Chaos level: over 9000!",
    "Laporan dari pasar gelap: {user} diduga menjual utang palsu ke {count} korban.",
    "BREAKING: Ekonomi Debt War sedang goyang! {user} diduga dalang di balik kekacauan ini.",
    "Rumor beredar: {user} bersekutu dengan mafia untuk mengontrol pasar utang.",
    "{user} tertangkap kamera sedang merayakan setelah menjebak {count} orang.",
    "Krisis kepercayaan melanda! {user} dituduh sebagai biang kerok utang macet.",
    "Wanted: {user} — hadiah {bounty} bagi siapa yang berhasil membalaskan dendam.",
    "Ledakan ekonomi! {user} baru saja mentransfer kekayaan dalam jumlah besar.",
    "Bank sentral Debt War mengeluarkan peringatan: waspadai aktivitas {user}.",
    "Serial scammer {user} kembali beraksi! {count} korbannya melapor hari ini.",
    "Dunia Debt War berguncang! {user} mencapai rekor chaos baru.",
    "Kartel bawah tanah mengumumkan: {user} adalah most wanted player minggu ini.",
]

EVENT_TEMPLATES = {
    "debt_crisis": ["📉 *KRISIS UTANG* 📉\n\nSemua utang naik {percent}% drastis! Waktunya waspada!"],
    "tax_season": ["💰 *MUSIM PAJAK* 💰\n\nPemerintah memotong saldo pemain sebesar {percent}%!"],
    "gov_audit": ["🔍 *AUDIT PAJAK* 🔍\n\nSemua transaksi diaudit! Pajak naik {percent}%!"],
    "inflation": ["📈 *INFLASI* 📈\n\nHarga-harga naik! Biaya transaksi meningkat {percent}%!"],
    "crypto_crash": ["📉 *CRYPTO CRASH* 📉\n\nPasar crypto ambruk! Semua kehilangan {percent}% saldo!"],
    "stimulus": ["🎁 *STIMULUS EKONOMI* 🎁\n\nPemerintah memberi {amount} gratis ke semua pemain!"],
    "default": [
        "📰 *WORLD EVENT*\n\nTerjadi peristiwa global di Debt War!",
    ],
}


async def record_drama(text: str):
    conn = await get_connection()
    try:
        await conn.execute(
            "INSERT INTO drama_log (drama_text) VALUES (?)", (text,)
        )
        await conn.commit()
    finally:
        await conn.close()


async def generate_drama(username: str, count: int = 1, bounty: int = 0) -> str:
    template = random.choice(DRAMA_TEMPLATES)
    text = template.format(user=username, count=count, bounty=bounty)
    await record_drama(text)
    return text


async def generate_world_drama(event_type: str, percent: int = 0, amount: int = 0) -> str:
    templates = EVENT_TEMPLATES.get(event_type, EVENT_TEMPLATES["default"])
    template = random.choice(templates)
    text = template.format(percent=percent, amount=amount)
    await record_drama(text)
    return text


async def get_recent_drama(limit: int = 5) -> list:
    conn = await get_connection()
    try:
        async with conn.execute(
            "SELECT drama_text, created_at FROM drama_log ORDER BY created_at DESC LIMIT ?",
            (limit,),
        ) as cur:
            rows = await cur.fetchall()
            return [dict(row) for row in rows]
    finally:
        await conn.close()

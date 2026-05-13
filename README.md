# ⚔️ Debt War — Social Chaos Economy MMO

Game utang-piutang paling chaos di Telegram. Pinjam, tagih, jebak, sabotage, dan kuasai ekonomi bawah tanah.

## Fitur

### 💰 Ekonomi
- Utang / Tagih / Transfer antar pemain
- Bunga 5% per hari (otomatis ke pemberi utang)
- Credit Score 0-1000 (mempengaruhi bunga & success rate)
- Bank: deposit/withdraw + bunga 2%
- Lootbox: 4 rarity (common → legendary)
- Market: shield, booster, tools

### 🎮 Chaos
- 5 Advanced Traps (fake invest, phishing, tax, pyramid, mafia)
- Spy system — mata-matai pemain lain
- Sabotage — freeze/steal/block daily
- Casino: Slots, Blackjack, Roulette (18+)

### 🏆 Progresi
- 8 Achievements + 10 Title/Rank (bisa pilih title aktif)
- Season 30 hari + Leaderboard
- Wanted list — makin chaos makin diburu

### 👥 Sosial
- Gang/Mafia — vault, reputation, gang wars
- 4 NPC interaktif (loan shark, mafia boss, scammer, collector)
- Court/Pengadilan — sue, vote, sidang
- World News — event global + drama realtime

### 🛡️ Lainnya
- Ghost system — pemain yang belum join bisa di-utang
- Rate limiter + anti-abuse
- Multi bahasa (ID/EN)
- Display name kustom

## Tech Stack

- Python 3.13+
- python-telegram-bot 22.x
- PostgreSQL / SQLite (dual backend)
- APScheduler
- Asyncpg / aiosqlite

## Deploy

```bash
# 1. Clone
git clone https://github.com/FMATheNomad/debtwar.git
cd debtwar

# 2. Install
pip install -r requirements.txt

# 3. Run
DEBTWAR_TOKEN=token_kamu python3 main.py
```

### Deploy ke Railway

1. Push repo ke GitHub
2. Railway → New Project → Deploy from GitHub
3. Add env variable: `DEBTWAR_TOKEN`
4. (Optional) Add PostgreSQL for persistent data

## Command

| Command | Fungsi |
|---------|--------|
| `/start` | Mulai / daftar |
| `/profile` | Profil & saldo |
| `/daily` | Reward harian |
| `/menu` | Menu utama |
| `/leaderboard` | Peringkat |
| `/utang @user 200` | Pinjamkan |
| `/nagih @user` | Tagih utang |
| `/lunas @user` | Bayar utang |
| `/jebak @user` | Pasang jebakan |
| `/trap <type> @user` | Advanced trap |
| `/transfer @user 200` | Transfer |
| `/spy @user` | Mata-matai |
| `/sabotage <type> @user` | Sabotase |
| `/bank deposit/withdraw` | Bank |
| `/slots` / `/bj` / `/roulette` | Casino |
| `/market` / `/buy` | Shop |
| `/lootbox buy|open` | Lootbox |
| `/gang` | Gang system |
| `/npc` | NPC interaksi |
| `/sue @user` | Pengadilan |
| `/setname <nama>` | Ganti nama |
| `/faq` | Bantuan |

## Disclaimer

Casino & lootbox adalah fitur hiburan semata. 18+. Tidak ada uang asli.

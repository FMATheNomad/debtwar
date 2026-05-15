_translations = {

    # ── COOLDOWN ──
    "wait": {"id": "Tunggu", "en": "Wait"},
    "seconds": {"id": "detik", "en": "seconds"},
    "before_using": {
        "id": "lagi sebelum pakai command ini.",
        "en": "more before using this command.",
    },

    # ── REGISTRATION ──
    "not_registered": {
        "id": "Kamu belum terdaftar. Ketik /start dulu ya!",
        "en": "You're not registered yet. Type /start first!",
    },
    "welcome_ghost": {
        "id": "\n\n⚠️ *Eh, kamu sudah punya hutang {debt}* sebelum main!\nSeseorang sudah 'mendaftarkan' kamu. Welcome to Debt War.  😈",
        "en": "\n\n⚠️ *Hey, you already have a debt of {debt}* before playing!\nSomeone already 'registered' you. Welcome to Debt War. 😈",
    },

    # ── VALIDATION ──
    "invalid_format_utang": {
        "id": "Format: /utang @username jumlah\nContoh: /utang @fariz 200",
        "en": "Format: /utang @username amount\nExample: /utang @fariz 200",
    },
    "invalid_format_nagih": {
        "id": "Format: /nagih @username",
        "en": "Format: /nagih @username",
    },
    "invalid_format_jebak": {
        "id": "Format: /jebak @username",
        "en": "Format: /jebak @username",
    },
    "invalid_format_transfer": {
        "id": "Format: /transfer @username jumlah\nContoh: /transfer @fariz 200",
        "en": "Format: /transfer @username amount\nExample: /transfer @fariz 200",
    },
    "amount_must_be_number": {
        "id": "Jumlahnya harus angka, bro.",
        "en": "Amount must be a number, bro.",
    },
    "amount_positive": {
        "id": "Minjem minimal 1 koin dong.",
        "en": "Lend at least 1 coin.",
    },
    "self_utang": {
        "id": "Utang ke diri sendiri? Terapi dulu kali.",
        "en": "Lending to yourself? Seek therapy first.",
    },
    "self_nagih": {
        "id": "Nagih ke diri sendiri? Serius nih?",
        "en": "Collecting from yourself? Seriously?",
    },
    "self_jebak": {
        "id": "Jebak diri sendiri? Respect, tapi tidak.",
        "en": "Trapping yourself? Respect, but no.",
    },
    "self_transfer": {
        "id": "Transfer ke diri sendiri? Mau ngapain?",
        "en": "Transfer to yourself? What are you doing?",
    },
    "insufficient_balance": {
        "id": "Saldo kamu cuma {balance}. Mau minjemin apa?",
        "en": "Your balance is only {balance}. How can you lend?",
    },
    "debt_full": {
        "id": "Utang @{username} sudah penuh ({debt}/{max_debt}). Gabisa nambah lagi!",
        "en": "@{username}'s debt is full ({debt}/{max_debt}). Can't add more!",
    },
    "debt_full_trap": {
        "id": "Utang @{username} sudah penuh ({debt}/{max_debt}). Jebakan gabisa nambah!",
        "en": "@{username}'s debt is full ({debt}/{max_debt}). Trap can't add more!",
    },
    "target_not_found": {
        "id": "User @{username} tidak ditemukan.",
        "en": "User @{username} not found.",
    },
    "no_debt_to_collect": {
        "id": "@{username} tidak punya utang ke kamu.",
        "en": "@{username} has no debt to collect.",
    },
    "nagih_not_creditor": {
        "id": "Kamu tidak punya piutang ke @{username}. Cuma kreditor yang bisa nagih.",
        "en": "You have no receivables from @{username}. Only creditors can collect.",
    },

    # ── BANKRUPTCY ──
    "bankrupt_status": {
        "id": "\n\n💀 *KAMU BANGKRUT!* Tidak bisa melakukan transaksi sampai {date}.",
        "en": "\n\n💀 *YOU ARE BANKRUPT!* Cannot transact until {date}.",
    },
    "bankrupt_occurred": {
        "id": "💀 *BANGKRUT!* Utangmu terlalu besar! Kamu kehilangan semua saldo dan utang di-reset.\nKamu tidak bisa bertransaksi selama 24 jam.",
        "en": "💀 *BANKRUPT!* Your debt was too high! You lost all balance and debt was reset.\nYou cannot transact for 24 hours.",
    },

    # ── NOTIFICATIONS ──
    "notify_debt": {
        "id": "⚠️ @{lender} mengutangimu {amount}! Cek /profile untuk lihat utangmu.",
        "en": "⚠️ @{lender} lent you {amount}! Check /profile to see your debt.",
    },
    "notify_trap": {
        "id": "🪤 @{trapper} memasang jebakan! Utangmu bertambah {amount}!",
        "en": "🪤 @{trapper} set a trap! Your debt increased by {amount}!",
    },
    "notify_trap_fail": {
        "id": "😅 @{trapper} gagal menjebakmu! Jebakannya meleset.",
        "en": "😅 @{trapper} failed to trap you! The trap missed.",
    },
    "notify_collect": {
        "id": "💰 @{lender} berhasil menagih {amount} darimu! Utangmu lunas.",
        "en": "💰 @{lender} collected {amount} from you! Your debt is cleared.",
    },
    "notify_transfer": {
        "id": "💸 @{sender} mentransfer {amount} kepadamu!",
        "en": "💸 @{sender} transferred {amount} to you!",
    },
    "notification_sent": {
        "id": "📨 Notifikasi terkirim.",
        "en": "📨 Notification sent.",
    },
    "notification_failed": {
        "id": "📭 Tidak bisa kirim DM. User belum pernah chat bot.",
        "en": "📭 Cannot send DM. User hasn't started the bot.",
    },

    # ── CHAOS MESSAGES: UTANG ──
    "utang_chaos_0": {
        "id": "💸 Duit melayang! {lender} baru aja ditipu halus sama {debtor}. Klasik.",
        "en": "💸 Money flies! {lender} just got smoothly scammed by {debtor}. Classic.",
    },
    "utang_chaos_1": {
        "id": "🤝 Deal gelap terjadi. {debtor} ambil {amount} koin dari {lender}. Semoga balik...",
        "en": "🤝 Dark deal made. {debtor} took {amount} coins from {lender}. Hope it returns...",
    },
    "utang_chaos_2": {
        "id": "😈 {lender} baru kena PHP finansial dari {debtor}. {amount} koin raib.",
        "en": "😈 {lender} just got financially manipulated by {debtor}. {amount} coins gone.",
    },
    "utang_chaos_3": {
        "id": "📜 Kontrak utang ditandatangani pake ludah. {debtor} berutang {amount} ke {lender}.",
        "en": "📜 Debt contract signed with spit. {debtor} owes {amount} to {lender}.",
    },
    "utang_chaos_4": {
        "id": "💀 {lender} percaya sama {debtor}. Besar sekali keberaniannya itu.",
        "en": "💀 {lender} trusts {debtor}. That takes some courage.",
    },
    "utang_chaos_5": {
        "id": "🏦 Bank of {debtor} baru dapet suntikan dana {amount} dari {lender}. Bodoh tapi legit.",
        "en": "🏦 Bank of {debtor} just got {amount} funding from {lender}. Foolish but legit.",
    },
    "utang_chaos_6": {
        "id": "🎰 {debtor} dapet modal {amount}. {lender} dapet... doa. That's it.",
        "en": "🎰 {debtor} got {amount} capital. {lender} got... prayers. That's it.",
    },
    "utang_chaos_7": {
        "id": "😂 {amount} berpindah tangan. {lender} masih senyum. Tunggu aja.",
        "en": "😂 {amount} changed hands. {lender} is still smiling. Just wait.",
    },
    "utang_chaos_8": {
        "id": "🐍 {debtor} bilang 'nanti dibalikin'. {lender} percaya. Dua-duanya lucu.",
        "en": "🐍 {debtor} said 'I'll pay back'. {lender} believed it. Both are funny.",
    },
    "utang_chaos_9": {
        "id": "⚔️ Debt War resmi dimulai. {lender} vs {debtor}. {amount} jadi taruhannya.",
        "en": "⚔️ Debt War officially begins. {lender} vs {debtor}. {amount} is at stake.",
    },

    # ── CHAOS MESSAGES: NAGIH ──
    "nagih_success_0": {
        "id": "💰 MIRACLE! {debtor} bayar utang! Catat tanggalnya, ini langka.",
        "en": "💰 MIRACLE! {debtor} paid their debt! Mark the date, this is rare.",
    },
    "nagih_success_1": {
        "id": "😤 {lender} nagih dan berhasil! {amount} koin balik. Dunia masih adil rupanya.",
        "en": "😤 {lender} collected and succeeded! {amount} coins returned. The world is still just.",
    },
    "nagih_success_2": {
        "id": "🎉 {debtor} melunasi utang {amount}. Langit cerah hari ini.",
        "en": "🎉 {debtor} paid off {amount}. The sky is clear today.",
    },
    "nagih_success_3": {
        "id": "👏 {lender} gigih nagih dan menang! {debtor} menyerah dan bayar {amount}.",
        "en": "👏 {lender} persistently collected and won! {debtor} gave up and paid {amount}.",
    },
    "nagih_success_4": {
        "id": "💸 Transfer berhasil! {amount} balik ke {lender}. Ini tidak biasa.",
        "en": "💸 Transfer successful! {amount} returned to {lender}. This is unusual.",
    },
    "nagih_fail_0": {
        "id": "😭 {lender} nagih tapi {debtor} pura-pura tidur. Utang masih nol.",
        "en": "😭 {lender} collected but {debtor} pretended to sleep. Debt untouched.",
    },
    "nagih_fail_1": {
        "id": "🤡 {debtor} bilang 'bentar lagi'. Itu bohong. Kamu tahu itu bohong.",
        "en": "🤡 {debtor} said 'soon'. That's a lie. You know it's a lie.",
    },
    "nagih_fail_2": {
        "id": "🏃 {debtor} lagi 'sibuk'. {lender} diminta sabar. Sabar sampai kapan?",
        "en": "🏃 {debtor} is 'busy'. {lender} told to be patient. How long?",
    },
    "nagih_fail_3": {
        "id": "📵 Nomornya seperti tidak aktif. Padahal tadi online.",
        "en": "📵 Number seems inactive. They were online just now.",
    },
    "nagih_fail_4": {
        "id": "😤 {lender} nagih. {debtor} ketawa. Tidak ada yang bayar hari ini.",
        "en": "😤 {lender} asked. {debtor} laughed. Nobody paid today.",
    },

    # ── CHAOS MESSAGES: JEBAK ──
    "jebak_success_0": {
        "id": "🪤 JEBAKAN BERHASIL! {target} kena trap dari {trapper}! Dapet debt {amount} + reward {reward}!",
        "en": "🪤 TRAP SUCCESS! {target} got trapped by {trapper}! Debt +{amount} + reward {reward}!",
    },
    "jebak_success_1": {
        "id": "😈 {trapper} pasang jebakan, {target} injak. Debt nambah {amount}! {trapper} dapet {reward}!",
        "en": "😈 {trapper} set a trap, {target} stepped on it. Debt +{amount}! {trapper} got {reward}!",
    },
    "jebak_success_2": {
        "id": "💣 BOOM! {target} kena jebak {trapper}. Debt +{amount}. {trapper} dapet komisi {reward}.",
        "en": "💣 BOOM! {target} trapped by {trapper}. Debt +{amount}. {trapper} got {reward} commission.",
    },
    "jebak_success_3": {
        "id": "🎭 Drama Debt War: {trapper} jadi villain, {target} jadi korban. {trapper} dapet {reward}.",
        "en": "🎭 Debt War drama: {trapper} is the villain, {target} is the victim. {trapper} got {reward}.",
    },
    "jebak_success_4": {
        "id": "🐀 {target} masuk perangkap {trapper}. {trapper} cuan {reward} dari hasil jebakan!",
        "en": "🐀 {target} fell into {trapper}'s trap. {trapper} earned {reward} from the trap!",
    },
    "jebak_fail_0": {
        "id": "😅 Jebakan {trapper} gagal total. {target} malah ketawa.",
        "en": "😅 {trapper}'s trap failed completely. {target} is laughing.",
    },
    "jebak_fail_1": {
        "id": "🤦 {trapper} pasang jebakan tapi injak sendiri. Skill issue.",
        "en": "🤦 {trapper} set a trap but stepped on it themselves. Skill issue.",
    },
    "jebak_fail_2": {
        "id": "💨 Angin. Kosong. Jebakan tidak mempan ke {target}.",
        "en": "💨 Wind. Empty. Trap had no effect on {target}.",
    },
    "jebak_fail_3": {
        "id": "😂 {target} terlalu waspada. {trapper} pulang dengan malu.",
        "en": "😂 {target} too alert. {trapper} goes home in shame.",
    },
    "jebak_fail_4": {
        "id": "🎯 Miss! Jebakan meleset jauh. {target} selamat hari ini.",
        "en": "🎯 Miss! Trap missed by a mile. {target} survives today.",
    },
    "trap_penalty": {
        "id": "Kamu kehilangan {penalty} karena jebakan gagal!",
        "en": "You lost {penalty} due to failed trap!",
    },
    "trap_reward": {
        "id": "\n\n🎉 Kamu dapet reward {amount} dari jebakan berhasil!",
        "en": "\n\n🎉 You got {amount} reward from the successful trap!",
    },

    # ── TRANSFER ──
    "transfer_success": {
        "id": "💸 Transfer {amount} ke @{target} berhasil!",
        "en": "💸 Transfer {amount} to @{target} successful!",
    },

    # ── DAILY ──
    "daily_success": {
        "id": "🎁 *Daily Reward!*\nKamu dapat {amount}!\n🔥 Streak: {streak} hari",
        "en": "🎁 *Daily Reward!*\nYou got {amount}!\n🔥 Streak: {streak} days",
    },
    "daily_streak_bonus": {
        "id": "\n🌟 Streak bonus: +{bonus}!",
        "en": "\n🌟 Streak bonus: +{bonus}!",
    },
    "daily_already_claimed": {
        "id": "⏳ Kamu sudah klaim daily hari ini.\nCoba lagi dalam {time}.",
        "en": "⏳ You already claimed daily today.\nTry again in {time}.",
    },

    # ── LEADERBOARD ──
    "leaderboard_title": {
        "id": "🏆 *LEADERBOARD*",
        "en": "🏆 *LEADERBOARD*",
    },
    "leaderboard_richest": {
        "id": "💰 *Terkaya*",
        "en": "💰 *Richest*",
    },
    "leaderboard_debt": {
        "id": "💳 *Utang Terbesar*",
        "en": "💳 *Biggest Debt*",
    },
"leaderboard_chaos": {
        "id": "\U0001f608 *Chaos Player*",
        "en": "\U0001f608 *Chaos Player*",
    },
    "leaderboard_chaos_detail": {"id": "\U0001f4ca Detail", "en": "\U0001f4ca Detail"},
    "leaderboard_chaos_detail_title": {
        "id": "\U0001f4ca *CHAOS DETAIL \u2014 Top 10*\n\nPeringkat berdasarkan chaos score (trap + pinjaman + tagihan).\nMenampilkan title aktif, jumlah title, dan pencapaian.\n",
        "en": "\U0001f4ca *CHAOS DETAIL \u2014 Top 10*\n\nRanked by chaos score (traps + lending + collections).\nShows active title, title count, and achievements.\n",
    },
    "leaderboard_chaos_header": {
        "id": "{medal} @{name}\n\U0001f4ca Score: {score} | \U0001faa8 Trap: {t}/{ts} | \U0001f4b0 Pinjam: {lent} | \U0001f4b0 Tagih: {col} | \U0001f3c6 Ach: {ach}\n",
        "en": "{medal} @{name}\n\U0001f4ca Score: {score} | \U0001faa8 Trap: {t}/{ts} | \U0001f4b0 Lend: {lent} | \U0001f4b0 Collect: {col} | \U0001f3c6 Ach: {ach}\n",
    },
    "leaderboard_empty": {
        "id": "(belum ada data)",
        "en": "(no data yet)",
    },

    # ── PROFILE ──
    "profile_title": {
        "id": "\U0001f464 *Profil Kamu*",
        "en": "\U0001f464 *Your Profile*",
    },
    "profile_id": {"id": "\U0001f194 ID", "en": "\U0001f194 ID"},
    "profile_username": {"id": "\U0001f4db Username", "en": "\U0001f4db Username"},
    "profile_balance": {"id": "\U0001f4b0 Saldo", "en": "\U0001f4b0 Balance"},
    "profile_debt": {"id": "\U0001f4b3 Utang", "en": "\U0001f4b3 Debt"},
    "profile_stats": {
        "id": "Stats",
        "en": "Stats",
    },
    "profile_achievements": {
        "id": "Achievements",
        "en": "Achievements",
    },
    "profile_total_lent": {"id": "Total minjemin", "en": "Total lent"},
    "profile_total_collected": {"id": "Total tagihan", "en": "Total collected"},
    "profile_traps_set": {"id": "Jebakan dipasang", "en": "Traps set"},
    "profile_traps_successful": {"id": "Jebakan berhasil", "en": "Traps successful"},
    "profile_daily_streak": {"id": "Daily streak", "en": "Daily streak"},
    "profile_bankrupt_count": {"id": "Bangkrut", "en": "Bankrupted"},

    # ── MENU ──
    "menu_main_title": {
        "id": "⚔️ *Debt War — Main Menu*\n\nPilih aksi di bawah:",
        "en": "⚔️ *Debt War — Main Menu*\n\nChoose an action below:",
    },
    "menu_chaos_title": {
        "id": "😈 *Chaos Menu*\n\nPilih senjata kamu:",
        "en": "😈 *Chaos Menu*\n\nChoose your weapon:",
    },
    "menu_btn_profile": {"id": "💰 Profile", "en": "💰 Profile"},
    "menu_btn_daily": {"id": "🎁 Daily", "en": "🎁 Daily"},
    "menu_btn_leaderboard": {"id": "🏆 Leaderboard", "en": "🏆 Leaderboard"},
    "menu_btn_chaos": {"id": "😈 Chaos Menu", "en": "😈 Chaos Menu"},
    "menu_btn_utang": {"id": "💸 Utang", "en": "💸 Lend"},
    "menu_btn_nagih": {"id": "💰 Nagih", "en": "💰 Collect"},
    "menu_btn_jebak": {"id": "🪤 Jebak", "en": "🪤 Trap"},
    "menu_btn_transfer": {"id": "🔄 Transfer", "en": "🔄 Transfer"},
    "menu_btn_back": {"id": "🔙 Kembali", "en": "🔙 Back"},
    "menu_btn_refresh": {"id": "🔄 Refresh", "en": "🔄 Refresh"},

    # ── ACTION PROMPTS ──
    "action_prompt_utang": {
        "id": "💸 Ketik: /utang @username jumlah\nContoh: /utang @fariz 200",
        "en": "💸 Type: /utang @username amount\nExample: /utang @fariz 200",
    },
    "action_prompt_nagih": {
        "id": "💰 Ketik: /nagih @username\nContoh: /nagih @fariz",
        "en": "💰 Type: /nagih @username\nExample: /nagih @fariz",
    },
    "action_prompt_jebak": {
        "id": "🪤 Ketik: /jebak @username\nContoh: /jebak @fariz",
        "en": "🪤 Type: /jebak @username\nExample: /jebak @fariz",
    },
    "action_prompt_transfer": {
        "id": "🔄 Ketik: /transfer @username jumlah\nContoh: /transfer @fariz 200",
        "en": "🔄 Type: /transfer @username amount\nExample: /transfer @fariz 200",
    },

    # ── ANTI-ABUSE ──
    "anti_abuse_daily_lend_limit": {
        "id": "⚠️ Limit harian utang tercapai ({limit} per hari). Besok lagi ya!",
        "en": "⚠️ Daily lend limit reached ({limit}/day). Try again tomorrow!",
    },
    "anti_abuse_daily_transfer_limit": {
        "id": "⚠️ Limit harian transfer tercapai ({limit} per hari). Besok lagi ya!",
        "en": "⚠️ Daily transfer limit reached ({limit}/day). Try again tomorrow!",
    },
    "anti_abuse_too_fast": {
        "id": "⏳ Kebanyakan transaksi! Tunggu bentar.",
        "en": "⏳ Too many transactions! Slow down.",
    },
    "anti_abuse_bankrupt": {
        "id": "💀 Kamu sedang bangkrut. Tidak bisa transaksi sampai {date}.",
        "en": "💀 You are bankrupt. Cannot transact until {date}.",
    },

    # ── RANDOM EVENTS ──
    "event_crisis": {
        "id": "📉 *KRISIS EKONOMI!* Semua utang naik {percent}!",
        "en": "📉 *ECONOMY CRISIS!* All debts increased by {percent}!",
    },
    "event_boom": {
        "id": "📈 *BOOM EKONOMI!* Semua balance naik {percent}!",
        "en": "📈 *ECONOMY BOOM!* All balances increased by {percent}!",
    },
    "event_gift": {
        "id": "💰 *BANK SEDEKAH!* Kamu dapat {amount} gratis!",
        "en": "💰 *BANK CHARITY!* You got {amount} for free!",
    },

    # ── ACHIEVEMENTS ──
    "ach_first_trap": {
        "id": "🏅 *Achievement: First Blood!*\nKamu berhasil menjebak seseorang!",
        "en": "🏅 *Achievement: First Blood!*\nYou successfully trapped someone!",
    },
    "ach_first_collect": {
        "id": "🏅 *Achievement: Debt Collector!*\nKamu berhasil menagih utang pertama!",
        "en": "🏅 *Achievement: Debt Collector!*\nYou successfully collected your first debt!",
    },
    "ach_debt_collector": {
        "id": "🏅 *Achievement: Debt Collector 1000!*\nTotal tagihanmu mencapai 1000!",
        "en": "🏅 *Achievement: Debt Collector 1000!*\nYour total collections reached 1000!",
    },
    "ach_debt_collector_5000": {
        "id": "🏅 *Achievement: Shark Loan!*\nTotal tagihanmu mencapai 5000! Kamu predator!",
        "en": "🏅 *Achievement: Shark Loan!*\nYour total collections reached 5000! You predator!",
    },
    "ach_big_lender": {
        "id": "🏅 *Achievement: Big Spender!*\nTotal pinjamanmu mencapai 1000!",
        "en": "🏅 *Achievement: Big Spender!*\nYour total lending reached 1000!",
    },
    "ach_trap_master": {
        "id": "🏅 *Achievement: Trap Master!*\nKamu berhasil memasang 10 jebakan!",
        "en": "🏅 *Achievement: Trap Master!*\nYou successfully set 10 traps!",
    },
    "ach_bankrupt": {
        "id": "🏅 *Achievement: Hancur!*\nKamu bangkrut! Dari atas jatuh ke bawah.",
        "en": "🏅 *Achievement: Wrecked!*\nYou went bankrupt! From top to bottom.",
    },
    "ach_streak_7": {
        "id": "🏅 *Achievement: Dedicated!*\nDaily streak 7 hari! Konsisten!",
        "en": "🏅 *Achievement: Dedicated!*\n7-day daily streak! Consistent!",
    },

    # ── INTEREST ──
    "interest_notify": {
        "id": "📈 Bunga utang {percent}: utangmu bertambah {amount}!",
        "en": "📈 Debt interest {percent}: your debt increased by {amount}!",
    },

    # ── BUTTON DESCRIPTIONS (shown on click) ──
    "btn_desc_profile": {
        "id": "📋 Menampilkan profil, saldo, statistik, dan riwayat kamu",
        "en": "📋 Shows your profile, balance, stats, and history",
    },
    "btn_desc_daily": {
        "id": "🎁 Klaim reward harian + streak bonus setiap hari",
        "en": "🎁 Claim daily reward + streak bonus every day",
    },
    "btn_desc_leaderboard": {
        "id": "🏆 Lihat peringkat pemain terkaya, utang terbesar, dan chaos player",
        "en": "🏆 View rankings: richest, biggest debt, and chaos players",
    },
    "btn_desc_chaos": {
        "id": "😈 Buka chaos menu: utang, nagih, jebak, dan transfer",
        "en": "😈 Open chaos menu: lend, collect, trap, and transfer",
    },
    "btn_desc_utang": {
        "id": "💸 Pinjamkan uang ke user lain (otomatis bikin akun baru)",
        "en": "💸 Lend money to another user (auto-creates new account)",
    },
    "btn_desc_nagih": {
        "id": "💰 Tagih utang dari user lain dan dapatkan uangmu kembali",
        "en": "💰 Collect debt from another user and get your money back",
    },
    "btn_desc_jebak": {
        "id": "🪤 Pasang jebakan! Target kena debt, kamu dapet reward 20%",
        "en": "🪤 Set a trap! Target gets debt, you get 20% reward",
    },
    "btn_desc_transfer": {
        "id": "🔄 Transfer saldo ke user lain",
        "en": "🔄 Transfer balance to another user",
    },
    "btn_desc_refresh": {
        "id": "🔄 Refresh tampilan",
        "en": "🔄 Refresh display",
    },
    "btn_desc_back": {
        "id": "🔙 Kembali ke menu utama",
        "en": "🔙 Back to main menu",
    },
    "btn_desc_faq": {
        "id": "❓ Bantuan lengkap: semua fitur, command, dan cara main",
        "en": "❓ Complete help: all features, commands, and how to play",
    },
    "btn_desc_credit": {
        "id": "💳 Lihat credit score dan tier kamu",
        "en": "💳 View your credit score and tier",
    },
    "btn_desc_stats": {
        "id": "📊 Statistik lengkap permainan kamu",
        "en": "📊 Your complete game statistics",
    },
    "btn_desc_titles": {
        "id": "👑 Lihat title/rank yang sudah di-unlock",
        "en": "👑 View unlocked titles/ranks",
    },

    # ── WELCOME ──
    "welcome_new_user": {
        "id": "💰 Saldo awal kamu",
        "en": "💰 Your starting balance",
    },
    "welcome_returning_user": {
        "id": "💰 Saldo",
        "en": "💰 Balance",
    },
    "welcome_game_desc": {
        "id": (
            "\n\n\u2694\ufe0f *Debt War* \u2014 Social Chaos Economy MMO di Telegram!\n\n"
            "\U0001f4cc *Fitur Utama:*\n"
            "\u2022 \U0001f4b8 Pinjam / tagih utang (/utang, /nagih, /lunas)\n"
            "\u2022 \U0001faa4 Jebakan + 5 Advanced Traps (/jebak, /trap)\n"
            "\u2022 \U0001f381 Daily reward + streak bonus (/daily)\n"
            "\u2022 \U0001f4c8 Bunga 5%/hari + Credit Score 0-1000\n"
            "\u2022 \U0001f3e6 Bank: deposit/withdraw + bunga 2%\n"
            "\u2022 \U0001f3b2 Casino: Slots, Blackjack, Roulette (18+)\n"
            "\u2022 \U0001f3ea Market: shield, booster, tools\n"
            "\u2022 \U0001f4a3 Spy + Sabotage (freeze/steal/block)\n"
            "\u2022 \U0001f3c6 8 Achievements + 10 Title/Rank\n"
            "\u2022 \U0001f3b1 Lootbox: 4 rarity (common\u2192legendary)\n"
            "\u2022 \U0001f9ea Gang/War + Vault + Reputation\n"
            "\u2022 \U0001f9d1\u200d\u2642\ufe0f 4 NPC interaktif + Misi\n"
            "\u2022 \U0001f3db\ufe0f Pengadilan + voting + denda\n"
            "\u2022 \U0001f3ad World News + Event global\n"
            "\u2022 \U0001f4c8 Investasi saham, reksadana, obligasi\n"
            "\u2022 \U0001f4cb Riwayat transaksi + saldo (/history)\n"
            "\u2022 \U0001f3af Season 30 hari + Leaderboard\n\n"
            "\U0001f6a9 *Peringatan:* Casino & lootbox hanya untuk hiburan. 18+.\n"
            "Bermainlah dengan bijak dan bertanggung jawab.\n\n"
            "Gunakan tombol di bawah untuk navigasi \U0001f447"
        ),
        "en": (
            "\n\n\u2694\ufe0f *Debt War* \u2014 Social Chaos Economy MMO on Telegram!\n\n"
            "\U0001f4cc *Main Features:*\n"
            "\u2022 \U0001f4b8 Lend / Collect / Pay debt (/utang, /nagih, /lunas)\n"
            "\u2022 \U0001faa4 Traps + 5 Advanced Traps (/jebak, /trap)\n"
            "\u2022 \U0001f381 Daily reward + streak bonus (/daily)\n"
            "\u2022 \U0001f4c8 5% interest + Credit Score 0-1000\n"
            "\u2022 \U0001f3e6 Bank: deposit/withdraw + 2% interest\n"
            "\u2022 \U0001f3b2 Casino: Slots, Blackjack, Roulette (18+)\n"
            "\u2022 \U0001f3ea Market: shields, boosters, tools\n"
            "\u2022 \U0001f4a3 Spy + Sabotage (freeze/steal/block)\n"
            "\u2022 \U0001f3c6 8 Achievements + 10 Title/Ranks\n"
            "\u2022 \U0001f3b1 Lootbox: 4 rarities (common\u2192legendary)\n"
            "\u2022 \U0001f9ea Gangs/Wars + Vault + Reputation\n"
            "\u2022 \U0001f9d1\u200d\u2642\ufe0f 4 Interactive NPCs + Missions\n"
            "\u2022 \U0001f3db\ufe0f Court + voting + fines\n"
            "\u2022 \U0001f3ad World News + Global events\n"
            "\u2022 \U0001f3af 30-day Season + Leaderboard\n\n"
            "\U0001f6a9 *Warning:* Casino & lootbox are for entertainment only. 18+.\n"
            "Play responsibly.\n\n"
            "Use the buttons below to navigate \U0001f447"
        ),
    },
    # ── GHOST NOTIFICATIONS ──
    "ghost_summary_title": {
        "id": "\n\n\U0001f514 *Aktivitas saat kamu offline:*",
        "en": "\n\n\U0001f514 *Activity while you were away:*",
    },
    "ghost_action_lent": {
        "id": "\n\U0001f4b8 @{name} ngutangin kamu \U0001f4b0{amount}",
        "en": "\n\U0001f4b8 @{name} lent you \U0001f4b0{amount}",
    },
    "ghost_action_trap": {
        "id": "\n\U0001faa4 @{name} pasang jebakan! Debt +{amount}",
        "en": "\n\U0001faa4 @{name} trapped you! Debt +{amount}",
    },
    "ghost_join_cta": {
        "id": "\n\n\U0001f525 *Balas dendam!* Ketik /start buat main dan lakuin hal yang sama ke mereka!",
        "en": "\n\n\U0001f525 *Get revenge!* Type /start to play and do the same to them!",
    },
    # ── FAQ ──
    "faq_title": {
        "id": "❓ *Bantuan Debt War*",
        "en": "❓ *Debt War Help*",
    },
    "faq_commands": {
        "id": (
            "\n\n📌 *DAFTAR COMMAND*\n\n"
            "🔹 `/start` — Mulai / daftar ulang\n"
            "🔹 `/profile` — Lihat profil & saldo\n"
            "🔹 `/daily` — Klaim reward harian\n"
            "🔹 `/menu` — Buka menu utama\n"
            "🔹 `/leaderboard` — Peringkat pemain\n"
            "🔹 `/history` — Riwayat transaksi\n"
            "🔹 `/setname <nama>` — Ganti nama display\n\n"
            "*Transaksi:*\n"
            "🔹 `/utang @user 200` — Pinjamkan 200\n"
            "🔹 `/nagih @user` — Tagih utang\n"
            "🔹 `/lunas <jumlah> @user` — Bayar utang\n"
            "🔹 `/transfer @user 200` — Transfer\n\n"
            "*Chaos:*\n"
            "🔹 `/jebak @user` — Pasang jebakan\n"
            "🔹 `/trap <type> @user` — Advanced trap\n"
            "🔹 `/spy @user` — Mata-matai player\n"
            "🔹 `/sabotage <type> @user` — Sabotase\n\n"
            "*Ekonomi:*\n"
            "🔹 `/bank deposit/withdraw` — Bank\n"
            "🔹 `/slots` / `/bj` / `/roulette` — Casino\n"
            "🔹 `/market` / `/buy` — Shop\n"
            "🔹 `/inv` — Inventory\n"
            "🔹 `/lootbox buy|open` — Lootbox\n"
            "🔹 `/investbuy <type> <id> <jumlah>` — Beli investasi\n"
            "🔹 `/investsell <type> <id>` — Jual investasi\n\n"
            "*Sosial:*\n"
            "🔹 `/gang create|join|leave` — Gang\n"
            "🔹 `/npc <id> <action>` — NPC interaksi\n"
            "🔹 `/sue @user <charge>` — Pengadilan\n"
            "🔹 `/vote <id> guilty/innocent` — Voting\n\n"
            "🔹 `/faq` — Bantuan ini"
        ),
        "en": (
            "\n\n📌 *COMMAND LIST*\n\n"
            "🔹 `/start` — Start / re-register\n"
            "🔹 `/profile` — View profile & balance\n"
            "🔹 `/daily` — Claim daily reward\n"
            "🔹 `/menu` — Open main menu\n"
            "🔹 `/leaderboard` — Player rankings\n"
            "🔹 `/history` — Transaction history\n"
            "🔹 `/setname <name>` — Change display name\n\n"
            "*Transactions:*\n"
            "🔹 `/utang @user 200` — Lend 200\n"
            "🔹 `/nagih @user` — Collect debt\n"
            "🔹 `/lunas <amount> @user` — Pay debt\n"
            "🔹 `/transfer @user 200` — Transfer\n\n"
            "*Chaos:*\n"
            "🔹 `/jebak @user` — Set trap\n"
            "🔹 `/trap <type> @user` — Advanced trap\n"
            "🔹 `/spy @user` — Spy on player\n"
            "🔹 `/sabotage <type> @user` — Sabotage\n\n"
            "*Economy:*\n"
            "🔹 `/bank deposit/withdraw` — Bank\n"
            "🔹 `/slots` / `/bj` / `/roulette` — Casino\n"
            "🔹 `/market` / `/buy` — Shop\n"
            "🔹 `/inv` — Inventory\n"
            "🔹 `/lootbox buy|open` — Lootbox\n"
            "🔹 `/investbuy <type> <id> <amount>` — Buy investment\n"
            "🔹 `/investsell <type> <id>` — Sell investment\n\n"
            "*Social:*\n"
            "🔹 `/gang create|join|leave` — Gang\n"
            "🔹 `/npc <id> <action>` — NPC interact\n"
            "🔹 `/sue @user <charge>` — Court\n"
            "🔹 `/vote <id> guilty/innocent` — Vote\n\n"
            "🔹 `/faq` — This help"
        ),
    },
    "faq_economy": {
        "id": (
            "\n\n💰 *BIAYA & BIAYA*\n\n"
            "• Gratis: /utang, /nagih, /jebak, /daily, /profile, /leaderboard\n"
            "• /transfer — Rp0 (tapi limit Rp3000/hari)\n"
            "• /spy — Rp100 (gagal kena denda Rp50)\n"
            "• /sabotage — Rp150 (gagal kena denda Rp80)\n"
            "• /bank deposit — gratis\n"
            "• /bank withdraw — fee 2%\n"
            "• /lootbox buy common/rare/epic/legendary — Rp200/500/1200/3000\n"
            "• /trap <type> — biaya trap (0-300 tergantung jenis)\n"
            "\n"
            "💰 *SISTEM EKONOMI*\n"
            "• Saldo awal: *Rp1000*\n"
            "• Max utang per user: *Rp5000*\n"
            "• Bunga utang: *5% per hari* (keuntungan lender)\n"
            "• Bangkrut: utang > Rp10000 \u2192 reset + lock 24 jam\n"
            "• Reward jebakan: *20%* dari jumlah debt\n"
            "• Credit Score: 0-1000, mempengaruhi bunga & rate\n"
            "• Bank: deposit/withdraw + bunga 2% per hari + max Rp50rb\n"
            "• 5 Advanced Traps: fake invest, phising, tax, pyramid, mafia\n"
            "• Casino: Slots / Blackjack / Roulette (RTP 85%, 18+)\n"
            "• Market: shield, trap booster, spy tools\n"
            "• Lootbox: 4 rarity (common\u2192legendary)\n"
            "• Season: 30 hari + XP + leaderboard\n"
            "• Lunas: bayar utang ke player/NPC (economy sink)\n"
            "• Transfer: antar player (max Rp3000/hari)"
        ),
        "en": (
            "\n\n💰 *COSTS OVERVIEW*\n\n"
            "• Free: /utang, /nagih, /jebak, /daily, /profile, /leaderboard\n"
            "• /transfer — Rp0 (limit Rp3000/day)\n"
            "• /spy — Rp100 (fail: Rp50 fine)\n"
            "• /sabotage — Rp150 (fail: Rp80 fine)\n"
            "• /bank deposit — free\n"
            "• /bank withdraw — 2% fee\n"
            "• /lootbox buy common/rare/epic/legendary — Rp200/500/1200/3000\n"
            "• /trap <type> — cost varies (0-300)\n"
            "\n"
            "💰 *ECONOMY SYSTEM*\n"
            "• Starting balance: *$1000*\n"
            "• Max debt per user: *$5000*\n"
            "• Debt interest: *5% daily* (goes to lender)\n"
            "• Bankruptcy: debt > $10000 \u2192 reset + 24h lock\n"
            "• Trap reward: *20%* of debt amount\n"
            "• Credit Score: 0-1000, affects interest & rates\n"
            "• Bank: deposit/withdraw + 2% daily interest + max $50k\n"
            "• 5 Advanced Traps: fake invest, phising, tax, pyramid, mafia\n"
            "• Casino: Slots / Blackjack / Roulette (85% RTP, 18+)\n"
            "• Market: shields, trap boosters, spy tools\n"
            "• Lootbox: 4 rarities (common\u2192legendary)\n"
            "• Season: 30 days + XP + leaderboard\n"
            "• Lunas: pay debt to player/NPC (economy sink)\n"
            "• Transfer: max Rp3000/day"
        ),
    },
    "faq_tips": {
        "id": (
            "\n\n🔥 *TIPS & TRICKS*\n\n"
            "• Jaga credit score \u2265600 buat bunga & rate terbaik\n"
            "• Deposit uang di bank biar dapet bunga 2% per hari\n"
            "• Spy dulu sebelum sabotage biar tahu target punya uang (spy Rp100)\n"
            "• Sabotage Rp150 — pastiin target punya saldo sebelum nyuri\n"
            "• Beli shield di market buat proteksi dari spy/trap\n"
            "• Gabung gang buat vault dan proteksi bersama\n"
            "• Main casino hati-hati, house edge 15%!\n"
            "• Buka lootbox legendary kalau lagi hoki (Rp3000)\n"
            "• Ikut season buat dapet leaderboard reward\n"
            "• Jangan lupa daily streak! Bonusnya gede\n"
            "• Lunasin utang sebelum bunga membengkak\n"
            "• Bayar langsung ke player: /lunas @player\n"
            "• Coba 5 advanced traps: /trap list"
        ),
        "en": (
            "\n\n🔥 *TIPS & TRICKS*\n\n"
            "• Keep credit score \u2265600 for best interest rates\n"
            "• Deposit money in bank for 2% daily interest\n"
            "• Spy before sabotage to know target's balance (spy Rp100)\n"
            "• Sabotage costs Rp150 — check target balance first!\n"
            "• Buy shields in market for spy/trap protection\n"
            "• Join a gang for shared vault and protection\n"
            "• Casino has 15% house edge - gamble wisely!\n"
            "• Open legendary lootboxes when you're lucky (Rp3000)\n"
            "• Join seasons for leaderboard rewards\n"
            "• Don't miss daily streaks! Big bonus rewards\n"
            "• Pay debt before interest blows up\n"
            "• Pay directly to player: /lunas @player\n"
            "• Try 5 advanced traps: /trap list"
        ),
    },
    "menu_btn_faq": {"id": "❓ Bantuan", "en": "❓ Help"},
    "faq_btn_commands": {"id": "📌 Commands", "en": "📌 Commands"},
    "faq_btn_economy": {"id": "💰 Economy", "en": "💰 Economy"},
    "faq_btn_tips": {"id": "🔥 Tips", "en": "🔥 Tips"},

    "no_target_in_message": {
        "id": "Gunakan command ini dengan reply ke pesan user atau sertakan @username.",
        "en": "Use this command by replying to a user's message or include @username.",
    },

    # ── CREDIT SCORE ──
    "credit_title": {
        "id": "💳 *Credit Score*",
        "en": "💳 *Credit Score*",
    },
    "credit_score_label": {
        "id": "Skor Kredit",
        "en": "Credit Score",
    },
    "credit_tier": {
        "id": "Tier",
        "en": "Tier",
    },
    "credit_repayed": {
        "id": "Total Dibayar",
        "en": "Total Repaid",
    },
    "credit_defaulted": {
        "id": "Total Gagal Bayar",
        "en": "Total Defaulted",
    },
    "credit_interest_mod": {
        "id": "Mod Bunga: {multiplier}x",
        "en": "Interest Mod: {multiplier}x",
    },
    "credit_trap_mod": {
        "id": "Mod Jebakan: {multiplier}x",
        "en": "Trap Mod: {multiplier}x",
    },
    "credit_spy_mod": {
        "id": "Mod Spy: {multiplier}x",
        "en": "Spy Mod: {multiplier}x",
    },

    # ── TITLES ──
    "title_current": {
        "id": "👑 Title Aktif",
        "en": "👑 Active Title",
    },
    "title_unlocked": {
        "id": "🏅 Title Terkunci",
        "en": "🏅 Unlocked Titles",
    },
    "title_new_unlock": {
        "id": "🏅 *Title Baru: {title}!*",
        "en": "🏅 *New Title: {title}!*",
    },

    # ── STATS ──
    "stats_title": {
        "id": "📊 *Statistik Pemain*",
        "en": "📊 *Player Statistics*",
    },
    "stats_total_lent": {
        "id": "Total Pinjaman",
        "en": "Total Lent",
    },
    "stats_total_collected": {
        "id": "Total Tagihan",
        "en": "Total Collected",
    },
    "stats_traps_set": {
        "id": "Jebakan Dipasang",
        "en": "Traps Set",
    },
    "stats_traps_success": {
        "id": "Jebakan Berhasil",
        "en": "Traps Successful",
    },
    "stats_trap_rate": {
        "id": "Rate Sukses Jebakan",
        "en": "Trap Success Rate",
    },
    "stats_peak_balance": {
        "id": "Saldo Tertinggi",
        "en": "Peak Balance",
    },
    "stats_bankruptcies": {
        "id": "Bangkrut",
        "en": "Bankruptcies",
    },
    "stats_daily_claimed": {
        "id": "Daily Diklaim",
        "en": "Daily Claimed",
    },
    "stats_chaos_score": {
        "id": "Chaos Score",
        "en": "Chaos Score",
    },

    # ── BUTTONS NEW ──
    "menu_btn_credit": {
        "id": "💳 Credit Score",
        "en": "💳 Credit Score",
    },
    "menu_btn_stats": {
        "id": "📊 Stats",
        "en": "📊 Stats",
    },
    "menu_btn_titles": {
        "id": "👑 Titles",
        "en": "👑 Titles",
    },
    "menu_btn_gang": {
        "id": "🏴 Gang",
        "en": "🏴 Gang",
    },
    "menu_btn_wanted": {
        "id": "🚨 Wanted",
        "en": "🚨 Wanted",
    },
    "menu_btn_drama": {
        "id": "📰 Drama",
        "en": "📰 Drama",
    },

    # ── GANG SYSTEM ──
    "gang_already_in": {
        "id": "Kamu sudah di dalam gang. Keluar dulu sebelum buat/join gang baru.",
        "en": "You're already in a gang. Leave first before creating/joining a new gang.",
    },
    "gang_insufficient_funds": {
        "id": "Saldo tidak cukup! Buat gang butuh {cost}.",
        "en": "Insufficient balance! Creating a gang costs {cost}.",
    },
    "gang_name_exists": {
        "id": "Nama gang sudah dipakai. Pilih nama lain.",
        "en": "Gang name already taken. Choose another name.",
    },
    "gang_create_failed": {
        "id": "Gagal membuat gang. Coba lagi.",
        "en": "Failed to create gang. Try again.",
    },
    "gang_created": {
        "id": "🏴 *Gang {name} berhasil dibuat!*\nBiaya pendirian: {cost}\nSekarang rekrut anggota!",
        "en": "🏴 *Gang {name} created!*\nSetup cost: {cost}\nNow recruit members!",
    },
    "gang_not_found": {
        "id": "Gang '{name}' tidak ditemukan.",
        "en": "Gang '{name}' not found.",
    },
    "gang_full": {
        "id": "Gang sudah penuh!",
        "en": "Gang is full!",
    },
    "gang_join_failed": {
        "id": "Gagal join gang. Coba lagi.",
        "en": "Failed to join gang. Try again.",
    },
    "gang_joined": {
        "id": "✅ Kamu bergabung dengan *{name}!*",
        "en": "✅ You joined *{name}!*",
    },
    "gang_not_in": {
        "id": "Kamu tidak berada di gang manapun.",
        "en": "You're not in any gang.",
    },
    "gang_left": {
        "id": "Kamu keluar dari *{name}*.",
        "en": "You left *{name}*.",
    },
    "gang_left_disbanded": {
        "id": "Kamu keluar dan *{name}* dibubarkan (tidak ada anggota lagi).",
        "en": "You left and *{name}* has been disbanded (no members left).",
    },
    "gang_owner_only": {
        "id": "Hanya owner/co-owner gang yang bisa melakukan ini.",
        "en": "Only gang owner/co-owner can do this.",
    },
    "gang_vault_deposited": {
        "id": "🏦 {amount} disimpan ke vault *{name}*.",
        "en": "🏦 {amount} deposited to *{name}* vault.",
    },
    "gang_vault_insufficient": {
        "id": "Vault gang tidak cukup!",
        "en": "Gang vault balance insufficient!",
    },
    "gang_vault_withdrawn": {
        "id": "🏦 {amount} ditarik dari vault *{name}*.",
        "en": "🏦 {amount} withdrawn from *{name}* vault.",
    },
    "gang_lb_title": {
        "id": "Gang Leaderboard",
        "en": "Gang Leaderboard",
    },
    "gang_lb_empty": {
        "id": "Belum ada gang terbentuk.",
        "en": "No gangs formed yet.",
    },
    "gang_war_self": {
        "id": "Tidak bisa deklarasi perang ke gang sendiri!",
        "en": "Can't declare war on your own gang!",
    },
    "gang_war_exists": {
        "id": "Sudah ada perang antara gang ini. Selesaikan dulu!",
        "en": "War already exists between these gangs. Finish it first!",
    },
    "gang_war_declared": {
        "id": "⚔️ *PERANG!* {attacker} mendeklarasikan perang ke {defender}!",
        "en": "⚔️ *WAR!* {attacker} declared war on {defender}!",
    },

    # ── WANTED ──
    "wanted_title": {
        "id": "🚨 *MOST WANTED*",
        "en": "🚨 *MOST WANTED*",
    },
    "wanted_empty": {
        "id": "Tidak ada yang masuk wanted list. Tenang... untuk sekarang.",
        "en": "No one is on the wanted list. Calm... for now.",
    },
    "wanted_entry": {
        "id": "{medal} @{name} — Level {level} | Bounty: {bounty} | Crimes: {crimes}",
        "en": "{medal} @{name} — Level {level} | Bounty: {bounty} | Crimes: {crimes}",
    },
    "wanted_you_are_wanted": {
        "id": "🚨 *KAMU DIINGINKAN!* Hati-hati, kamu jadi target empuk!",
        "en": "🚨 *YOU ARE WANTED!* Watch out, you're an easy target!",
    },

    # ── DRAMA ──
    "drama_title": {
        "id": "📰 *Drama & Berita Terkini*",
        "en": "📰 *Latest Drama & News*",
    },
    "drama_empty": {
        "id": "Belum ada drama. Ayo mulai chaos!",
        "en": "No drama yet. Go create some chaos!",
    },
    "gang_menu_title": {
        "id": "🏴 *Gang Menu*\n\nKelola gang kamu di sini:",
        "en": "🏴 *Gang Menu*\n\nManage your gang here:",
    },
    "gang_prompt_create": {
        "id": "📝 Ketik: /gang create <nama>\nContoh: /gang create ShadowMafia",
        "en": "📝 Type: /gang create <name>\nExample: /gang create ShadowMafia",
    },
    "gang_prompt_join": {
        "id": "📝 Ketik: /gang join <nama>\nContoh: /gang join ShadowMafia",
        "en": "📝 Type: /gang join <name>\nExample: /gang join ShadowMafia",
    },
    "gang_help": {
        "id": "🏴 *Command Gang*\n/gang info — Info gang kamu\n/gang create <nama> — Buat gang\n/gang join <nama> — Join gang\n/gang leave — Keluar gang\n/gang vault deposit/withdraw <jumlah>\n/gang war <nama> — Deklarasi perang",
        "en": "🏴 *Gang Commands*\n/gang info — Your gang info\n/gang create <name> — Create gang\n/gang join <name> — Join gang\n/gang leave — Leave gang\n/gang vault deposit/withdraw <amount>\n/gang war <name> — Declare war",
    },
    "gang_vault_usage": {
        "id": "Gunakan: /gang vault deposit/withdraw <jumlah>",
        "en": "Usage: /gang vault deposit/withdraw <amount>",
    },
    "btn_desc_social": {
        "id": "🏴 Social hub: gang, wanted, drama",
        "en": "🏴 Social hub: gang, wanted, drama",
    },
    "btn_desc_gang": {
        "id": "🏴 Kelola gang/mafia kamu",
        "en": "🏴 Manage your gang/mafia",
    },
    "btn_desc_wanted": {
        "id": "🚨 Lihat most wanted players",
        "en": "🚨 View most wanted players",
    },
    "btn_desc_drama": {
        "id": "📰 Drama dan berita terkini",
        "en": "📰 Latest drama and news",
    },
    "btn_desc_world_news": {
        "id": "📰 Berita dan event terkini di dunia Debt War",
        "en": "📰 Latest news and events in Debt War",
    },
    "btn_desc_invest": {
        "id": "💹 Investasi saham, reksadana, dan obligasi",
        "en": "💹 Invest in stocks, mutual funds, and bonds",
    },
    "btn_desc_history": {
        "id": "📜 Riwayat transaksi terkini",
        "en": "📜 Recent transaction history",
    },
    "btn_desc_shop": {
        "id": "🏪 Beli Season Pass, Gems, dan paket lainnya",
        "en": "🏪 Buy Season Pass, Gems, and more",
    },
    "unknown_error": {
        "id": "Terjadi error. Coba lagi.",
        "en": "An error occurred. Try again.",
    },

    # ── SPY SYSTEM ──
    "spy_failed": {
        "id": "🕵️ Spy gagal! Kamu kehilangan {fine}.",
        "en": "🕵️ Spy failed! You lost {fine}.",
    },
    "self_spy": {
        "id": "Mata-matai diri sendiri? Curiga sama diri sendiri?",
        "en": "Spy on yourself? Suspicious of yourself?",
    },

    # ── SABOTAGE ──
    "sabotage_failed": {
        "id": "💣 Sabotase gagal! Kamu kena denda {fine}.",
        "en": "💣 Sabotage failed! You were fined {fine}.",
    },
    "sabotage_freeze": {
        "id": "🧊 *Freeze!* Akun @{target} dibekukan selama {duration}!",
        "en": "🧊 *Freeze!* @{target}'s account frozen for {duration}!",
    },
    "sabotage_steal": {
        "id": "💰 *Dicuri!* Kamu mencuri {amount} dari @{target}!",
        "en": "💰 *Stolen!* You stole {amount} from @{target}!",
    },
    "sabotage_steal_empty": {
        "id": "😅 @{target} tidak punya uang untuk dicuri.",
        "en": "😅 @{target} has no money to steal.",
    },
    "sabotage_block_daily": {
        "id": "🚫 *Daily Blocked!* @{target} tidak bisa klaim daily hari ini!",
        "en": "🚫 *Daily Blocked!* @{target} can't claim daily today!",
    },
    "sabotage_unknown_type": {
        "id": "Tipe sabotase tidak dikenal. Pilih: freeze, steal, block_daily",
        "en": "Unknown sabotage type. Choose: freeze, steal, block_daily",
    },
    "self_sabotage": {
        "id": "Sabotase diri sendiri? Cari hiburan lain bang.",
        "en": "Sabotaging yourself? Find another hobby.",
    },

    # ── ADVANCED TRAPS ──
    "trap_unknown": {
        "id": "Jenis jebakan tidak dikenal. Ketik /traps untuk lihat daftar.",
        "en": "Unknown trap type. Type /traps to see the list.",
    },

    # ── BANK ──
    "bank_deposited": {
        "id": "📥 {amount} disimpan. Saldo rekening: {balance}",
        "en": "📥 {amount} deposited. Bank balance: {balance}",
    },
    "bank_insufficient": {
        "id": "Saldo rekening tidak cukup! Hanya {balance}.",
        "en": "Insufficient bank balance! Only {balance}.",
    },
    "bank_max_deposit": {
        "id": "Rekening penuh! Max {max}.",
        "en": "Account full! Max {max}.",
    },
    "bank_withdrawn": {
        "id": "📤 {amount} ditarik. Diterima: {net} (fee: {fee})",
        "en": "📤 {amount} withdrawn. Received: {net} (fee: {fee})",
    },
    "bank_withdraw_fee_too_high": {
        "id": "Jumlah terlalu kecil, fee withdraw lebih besar.",
        "en": "Amount too small, withdraw fee exceeds it.",
    },
    "bank_usage": {
        "id": "Gunakan:\n/bank deposit <jumlah>\n/bank withdraw <jumlah>\n💰 Fee withdraw: 2%",
        "en": "Usage:\n/bank deposit <amount>\n/bank withdraw <amount>\n💰 Withdraw fee: 2%",
    },

    # ── CASINO ──
    "casino_bet_range": {
        "id": "Bet minimal {min}, maksimal {max}.",
        "en": "Min bet {min}, max bet {max}.",
    },
    "casino_usage": {
        "id": "🎰 /slots <bet>\n🃏 /bj <bet>\n🎱 /roulette <bet> <red/black/even/odd/number>",
        "en": "🎰 /slots <bet>\n🃏 /bj <bet>\n🎱 /roulette <bet> <red/black/even/odd/number>",
    },

    # ── MARKET ──
    "market_item_not_found": {
        "id": "Item tidak ditemukan.",
        "en": "Item not found.",
    },
    "market_bought": {
        "id": "✅ {name} dibeli seharga {price}!",
        "en": "✅ {name} purchased for {price}!",
    },

    # ── LOOTBOX ──
    "lootbox_invalid_rarity": {
        "id": "Rarity tidak valid. Pilih: common, rare, epic, legendary",
        "en": "Invalid rarity. Choose: common, rare, epic, legendary",
    },
    "lootbox_bought": {
        "id": "{emoji} *{rarity} Lootbox* dibeli! Harga: {price}",
        "en": "{emoji} *{rarity} Lootbox* purchased! Price: {price}",
    },
    "lootbox_none": {
        "id": "Kamu tidak punya {rarity} lootbox!",
        "en": "You don't have any {rarity} lootbox!",
    },
    "lootbox_money": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n💰 Dapet uang {amount}!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n💰 Got {amount} money!",
    },
    "lootbox_debt_bomb": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n💣 *DEBT BOMB!* Utang naik {amount}!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n💣 *DEBT BOMB!* Debt +{amount}!",
    },
    "lootbox_shield": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n🛡️ Dapet Shield 24 jam!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n🛡️ Got 24h Shield!",
    },
    "lootbox_chaos_buff": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n🔥 *CHAOS BUFF!* Kekacauanmu meningkat!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n🔥 *CHAOS BUFF!* Your chaos increases!",
    },
    "lootbox_curse": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n👻 *KUTUKAN!* Kamu kehilangan {penalty}!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n👻 *CURSED!* You lost {penalty}!",
    },
    "lootbox_title": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n👑 *TITLE UNLOCK!* Kamu mendapat title spesial!",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n👑 *TITLE UNLOCK!* You got a special title!",
    },
    "lootbox_nothing": {
        "id": "{emoji} *{rarity} LOOTBOX*\n\n😅 Dapat apa-apa... Hampa.",
        "en": "{emoji} *{rarity} LOOTBOX*\n\n😅 Got nothing... Empty.",
    },

    # ── COURT ──
    "court_usage": {
        "id": "🏛️ *Pengadilan*\n/sue @user <tuduhan> — Gugat\n/vote <id> <guilty/innocent> — Voting\nBiaya pengacara: 300💰",
        "en": "🏛️ *Court*\n/sue @user <charge> — Sue\n/vote <id> <guilty/innocent> — Vote\nLawyer fee: 300💰",
    },

    # ── WORLD EVENTS ──
    "event_title_debt_crisis": {
        "id": "📉 Krisis Utang",
        "en": "📉 Debt Crisis",
    },
    "event_desc_debt_crisis": {
        "id": "Semua utang naik drastis!",
        "en": "All debts have increased dramatically!",
    },
    "event_title_tax_season": {
        "id": "💰 Musim Pajak",
        "en": "💰 Tax Season",
    },
    "event_desc_tax_season": {
        "id": "Pemerintah memotong saldo semua pemain!",
        "en": "Government is taxing all players!",
    },
    "event_title_gov_audit": {
        "id": "🔍 Audit Pemerintah",
        "en": "🔍 Government Audit",
    },
    "event_desc_gov_audit": {
        "id": "Semua transaksi diaudit! Limit transaksi dikurangi.",
        "en": "All transactions audited! Transaction limits reduced.",
    },
    "event_title_inflation": {
        "id": "📈 Inflasi",
        "en": "📈 Inflation",
    },
    "event_desc_inflation": {
        "id": "Harga-harga naik! Biaya transaksi meningkat.",
        "en": "Prices rising! Transaction costs increased.",
    },
    "event_title_crypto_crash": {
        "id": "📉 Crypto Crash",
        "en": "📉 Crypto Crash",
    },
    "event_desc_crypto_crash": {
        "id": "Pasar crypto ambruk! Semua kehilangan saldo!",
        "en": "Crypto market crashed! Everyone lost balance!",
    },
    "event_title_stimulus": {
        "id": "🎁 Stimulus Ekonomi",
        "en": "🎁 Economic Stimulus",
    },
    "event_desc_stimulus": {
        "id": "Pemerintah memberi stimulus ke semua pemain!",
        "en": "Government is giving stimulus to all players!",
    },
}


def t(key: str, lang: str, **kwargs) -> str:
    entry = _translations.get(key)
    if not entry:
        return key
    text = entry.get(lang, entry.get("en", key))
    if kwargs:
        escaped = {}
        for k, v in kwargs.items():
            val = str(v)
            if "_" in val or "*" in val:
                val = f"`{val}`"
            escaped[k] = val
        return text.format(**escaped)
    return text
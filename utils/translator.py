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
        "id": "🎭 Drama Debt War: {trapper} jadi villain, {target} jadi korban. Debt +{amount}! {trapper} dapet {reward}.",
        "en": "🎭 Debt War drama: {trapper} is the villain, {target} is the victim. Debt +{amount}! {trapper} got {reward}.",
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
            "\n\n⚔️ *Debt War* — Game Ngutang-Ngutangan!\n\n"
            "💰 Kamu punya *Rp1.000*. Pinjemin ke temen, dapet bunga 5%/hari.\n\n"
            "▸ *Reply pesan temen* + ketik `/utang 200`\n"
            "▸ Kalo dia gak bayar, reply + `/nagih`\n"
            "▸ Mau jahili? reply + `/jebak` — target kena debt, lo dapet duit\n\n"
            "💸 Gak punya duit? `/daily` gratisan tiap hari.\n"
            "🔥 `/menu` buat fitur lain: bank, casino, gang, dll.\n"
            "❓ `/faq` kalo bingung."
        ),
        "en": (
            "\n\n⚔️ *Debt War* — The Debt Lending Game!\n\n"
            "💰 You have *$1.000*. Lend it to friends, earn 5% daily interest.\n\n"
            "▸ *Reply to their message* + type `/utang 200`\n"
            "▸ If they don't pay, reply + `/nagih`\n"
            "▸ Wanna be evil? reply + `/jebak` — target gets debt, you get paid\n\n"
            "💸 No money? `/daily` is free every day.\n"
            "🔥 `/menu` for more: bank, casino, gang, etc.\n"
            "❓ `/faq` if you're stuck."
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
    "faq_howtoplay": {
        "id": (
            "\n\n🎮 *CARA MAIN*\n\n"
            "1️⃣ *Dapetin duit*\n"
            "‣ `/daily` — gratis tiap hari (Rp50-200)\n"
            "‣ `/profile` cek saldo & utang lo\n\n"
            "2️⃣ *Pinjemin ke orang*\n"
            "‣ *Reply pesan* temen + `/utang 200` (gausah @username)\n"
            "‣ Duit lo turun 200, utang temen lo naik 200\n"
            "‣ Tiap hari utangnya naik 5% (bunga)\n\n"
            "3️⃣ *Tagih balik*\n"
            "‣ Reply + `/nagih` — ambil semua utang + bunga\n"
            "‣ Lo dapet duit lo balik + untung dari bunga\n\n"
            "4️⃣ *Atau jadi biang onar*\n"
            "‣ `/jebak` — kasi utang ke musuh, lo dapet komisi\n"
            "‣ `/spy` — intip saldo & utang target\n"
            "‣ `/sabotage` — freeze/curi/block daily target\n\n"
            "5️⃣ *Kalo boncos*\n"
            "‣ `/bank deposit` — nyimpen duit, dapet bunga 2%\n"
            "‣ `/casino` — gamble (tapi hati-hati, house edge 15%)\n"
            "‣ Kalo utang > Rp10.000 → *BANGKRUT* (reset + lock 24 jam)\n\n"
            "🔥 *Tips:* Reply pesan orang = gak perlu @username!\n"
            "💡 `/invite` buat ngajak temen main."
        ),
        "en": (
            "\n\n🎮 *HOW TO PLAY*\n\n"
            "1️⃣ *Get money*\n"
            "‣ `/daily` — free every day ($50-200)\n"
            "‣ `/profile` check balance & debt\n\n"
            "2️⃣ *Lend to people*\n"
            "‣ *Reply to message* + `/utang 200` (no @username needed)\n"
            "‣ Your money -200, their debt +200\n"
            "‣ Debt grows 5% daily (interest)\n\n"
            "3️⃣ *Collect your debt*\n"
            "‣ Reply + `/nagih` — take all debt + interest\n"
            "‣ You get your money back + profit\n\n"
            "4️⃣ *Or be a menace*\n"
            "‣ `/jebak` — give debt to enemies, earn commission\n"
            "‣ `/spy` — check target's balance & debt\n"
            "‣ `/sabotage` — freeze/steal/block daily reward\n\n"
            "5️⃣ *If you're broke*\n"
            "‣ `/bank deposit` — save money, earn 2% interest\n"
            "‣ `/casino` — gamble (but careful, 15% house edge)\n"
            "‣ Debt > $10.000 → *BANKRUPTCY* (reset + 24h lock)\n\n"
            "🔥 *Tip:* Reply to message = no @username needed!\n"
            "💡 `/invite` to invite friends."
        ),
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
            "🔹 `/setname <nama>` — Ganti nama display\n"
            "🔹 `/invite` — Dapetin link buat ngajak temen\n"
            "🔹 `/contacts` — Lihat player yang terhubung\n"
            "🔹 `/player <id>` — Cari player berdasarkan ID\n\n"
            "*🎯 Cara Tagging:*\n"
            "🔹 *Reply pesan target* lalu ketik command (gak perlu @username)\n"
            "🔹 Contoh: reply pesan seseorang lalu ketik `/nagih`\n"
            "🔹 Atau ketik `/utang @username 200` seperti biasa\n"
            "🔹 Kalo reply + command: target otomatis terdaftar\n\n"
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
            "🔹 `/setname <name>` — Change display name\n"
            "🔹 `/invite` — Get invite link to add friends\n"
            "🔹 `/contacts` — View connected players\n"
            "🔹 `/player <id>` — Lookup player by ID\n\n"
            "*🎯 How To Tag:*\n"
            "🔹 *Reply to someone's message* then type command (no @username needed)\n"
            "🔹 Example: reply to a message then type `/nagih`\n"
            "🔹 Or type `/utang @username 200` as before\n"
            "🔹 Reply + command: target auto-registered\n\n"
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
            "• /transfer — $0 (limit $3000/day)\n"
            "• /spy — $100 (fail: $50 fine)\n"
            "• /sabotage — $150 (fail: $80 fine)\n"
            "• /bank deposit — free\n"
            "• /bank withdraw — 2% fee\n"
            "• /lootbox buy common/rare/epic/legendary — $200/$500/$1200/$3000\n"
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
            "• Transfer: max $3000/day"
        ),
    },
    "faq_tips": {
        "id": (
            "\n\n🔥 *TIPS & TRICKS*\n\n"
            "• Gak punya @username? *Reply pesan target* + command bisa langsung main!\n"
            "• Pakai `/invite` buat ngajak temen. Kalo mereka join, otomatis terhubung.\n"
            "• `/contacts` buat lihat semua player yang pernah berinteraksi sama kamu.\n"
            "• [/player 123] buat cari info player tanpa @username — pake ID dari `/profile`\n"
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
            "• No @username? *Reply to target's message* + command works!\n"
            "• Use `/invite` to invite friends. Auto-connected when they join.\n"
            "• `/contacts` shows all players you've interacted with.\n"
            "• `/player <id>` to look up players without @username — ID from `/profile`\n"
            "• Keep credit score \u2265600 for best interest rates\n"
            "• Deposit money in bank for 2% daily interest\n"
            "• Spy before sabotage to know target's balance (spy $100)\n"
            "• Sabotage costs $150 — check target balance first!\n"
            "• Buy shields in market for spy/trap protection\n"
            "• Join a gang for shared vault and protection\n"
            "• Casino has 15% house edge - gamble wisely!\n"
            "• Open legendary lootboxes when you're lucky ($3000)\n"
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
    "faq_btn_howtoplay": {"id": "🎮 Cara Main", "en": "🎮 How To Play"},
    "faq_btn_tagging": {"id": "🎯 Cara Tagging", "en": "🎯 How To Tag"},

    "faq_tagging": {
        "id": (
            "\n\n🎯 *CARA TAGGING PLAYER*\n\n"
            "Ada *3 cara* buat tag target di Debt War:\n\n"
            "1️⃣ *REPLY PESAN* (Paling Gampang)\n"
            "‣ Reply pesan seseorang di grup\n"
            "‣ Ketik: `/nagih` (gausah @username)\n"
            "‣ Bot otomatis baca siapa yang di-reply\n"
            "‣ Cocok buat main di grup tanpa tau username\n\n"
            "2️⃣ *@USERNAME* (Cara Lama)\n"
            "‣ Ketik: `/utang @fariz 200`\n"
            "‣ Target harus punya @username\n\n"
            "3️⃣ *INVITE LINK + ID*\n"
            "‣ `/invite` — dapetin link undangan\n"
            "‣ Kalo temen kamu join lewat link, otomatis terhubung\n"
            "‣ `/contacts` — lihat semua player yang terhubung\n"
            "‣ `/player 123` — cari info player pake ID dari /profile\n\n"
            "💡 *Tips:*\n"
            "‣ Reply system work di grup MANAPUN\n"
            "‣ Kalo reply + command sekaligus: target otomatis didaftarin\n"
            "‣ Gak perlu khawatir soal @username lagi!"
        ),
        "en": (
            "\n\n🎯 *HOW TO TAG PLAYERS*\n\n"
            "There are *3 ways* to tag a target in Debt War:\n\n"
            "1️⃣ *REPLY TO MESSAGE* (Easiest)\n"
            "‣ Reply to someone's message in a group\n"
            "‣ Type: `/nagih` (no @username needed)\n"
            "‣ Bot automatically reads who you replied to\n"
            "‣ Perfect for group play without knowing usernames\n\n"
            "2️⃣ *@USERNAME* (Original Way)\n"
            "‣ Type: `/utang @fariz 200`\n"
            "‣ Target must have an @username\n\n"
            "3️⃣ *INVITE LINK + ID*\n"
            "‣ `/invite` — get your invite link\n"
            "‣ When friends join via your link, you're auto-connected\n"
            "‣ `/contacts` — see all connected players\n"
            "‣ `/player 123` — look up player info by ID from /profile\n\n"
            "💡 *Tips:*\n"
            "‣ Reply system works in ANY group\n"
            "‣ Reply + command auto-registers the target\n"
            "‣ No more @username worries!"
        ),
    },
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
    # ── NPC SYSTEM ──
    "npc_loan_shark_name": {"id": "Boris si Rentenir", "en": "Boris the Loan Shark"},
    "npc_loan_shark_desc": {"id": "🧛 Pinjaman kilat, bunga tinggi. Jangan macet ya.", "en": "🧛 Quick loans, high interest. Don't default, okay."},
    "npc_mafia_boss_name": {"id": "Don Corleone", "en": "Don Corleone"},
    "npc_mafia_boss_desc": {"id": "🕴️ Bos mafia. Punya misi-misi gelap.", "en": "🕴️ Mafia boss. Has dark missions."},
    "npc_scammer_name": {"id": "Jimmy Tipu", "en": "Jimmy the Scammer"},
    "npc_scammer_desc": {"id": "🐍 Ahli phishing. Awas dompetmu!", "en": "🐍 Phishing expert. Watch your wallet!"},
    "npc_collector_name": {"id": "Rambo Collector", "en": "Rambo the Collector"},
    "npc_collector_desc": {"id": "💪 Tukang tagih. Bisa bantu nagih utang orang lain.", "en": "💪 Debt collector. Can help collect others' debts."},
    "npc_hub_title": {"id": "🤖 *NPC Hub*", "en": "🤖 *NPC Hub*"},
    "npc_hub_action_loan_shark": {"id": "`borrow` pinjem duit, `pay` bayar utang", "en": "`borrow` borrow money, `pay` pay debt"},
    "npc_hub_action_mafia_boss": {"id": "`mission` ambil misi", "en": "`mission` take a mission"},
    "npc_hub_action_scammer": {"id": "`phish` tipu balik", "en": "`phish` phish back"},
    "npc_hub_action_collector": {"id": "`help_collect` tagih random debtor", "en": "`help_collect` collect from random debtor"},
    "npc_hub_usage": {"id": "Gunakan: /npc <id> <action>\nContoh: `/npc loan_shark borrow`", "en": "Usage: /npc <id> <action>\nExample: `/npc loan_shark borrow`"},
    "npc_not_found_list": {"id": "NPC tidak dikenal. Coba: loan_shark, mafia_boss, scammer, collector", "en": "NPC not found. Try: loan_shark, mafia_boss, scammer, collector"},
    "npc_not_found": {"id": "NPC tidak dikenal.", "en": "NPC not found."},
    "npc_info_usage": {"id": "{}\n\nGunakan: /npc {} <action>", "en": "{}\n\nUsage: /npc {} <action>"},
    "npc_action_unknown": {"id": "{} tidak mengerti perintah itu.", "en": "{} doesn't understand that command."},
    "npc_loan_shark_borrow": {"id": "Pinjem {amount}? OK, plus bunga {interest}%. Jangan lupa bayar ya... atau... 😈", "en": "Borrow {amount}? OK, plus {interest}% interest. Don't forget to pay... or... 😈"},
    "npc_loan_shark_borrow_received": {"id": "💸 Diterima: +{amount}", "en": "💸 Received: +{amount}"},
    "npc_loan_shark_borrow_debt": {"id": "💳 Utang: +{amount} (bunga)", "en": "💳 Debt: +{amount} (interest)"},
    "npc_loan_shark_no_debt": {"id": "Kamu tidak punya utang ke Boris.", "en": "You don't have any debt to Boris."},
    "npc_loan_shark_insufficient": {"id": "Saldo tidak cukup! Utangmu {debt}, saldomu {balance}.", "en": "Insufficient balance! Your debt is {debt}, your balance is {balance}."},
    "npc_loan_shark_pay_success": {"id": "Lunas. {amount} diterima. Pintu selalu terbuka untukmu...", "en": "Paid off. {amount} received. My door is always open for you..."},
    "npc_loan_shark_paid_off": {"id": "✅ Utang lunas!", "en": "✅ Debt paid off!"},
    "npc_mafia_insufficient": {"id": "Misi butuh modal {cost} untuk suap dan peralatan. Saldomu tidak cukup. Kembali kalau sudah punya duit.", "en": "The mission needs {cost} capital for bribes and equipment. Your balance isn't enough. Come back when you have the money."},
    "npc_mafia_fail": {"id": "Misi gagal! Informasi bocor, target kabur. Kamu kehilangan modal {cost}. Hilang dari sini sebelum bos marah.", "en": "Mission failed! Information leaked, target escaped. You lost {cost} capital. Get out of here before the boss gets angry."},
    "npc_mafia_fail_label": {"id": "❌ Rugi: -{cost}", "en": "❌ Loss: -{cost}"},
    "npc_mafia_mission_accept": {"id": "Ada misi untukmu: *{mission}*. Lakukan diam-diam.", "en": "I have a mission for you: *{mission}*. Do it quietly."},
    "npc_mission_cost_label": {"id": "💸 Modal: -{cost}", "en": "💸 Capital: -{cost}"},
    "npc_mission_reward_label": {"id": "💰 Reward: +{reward}", "en": "💰 Reward: +{reward}"},
    "npc_mission_total_label": {"id": "📊 Total: {total}", "en": "📊 Total: {total}"},
    "npc_mission_burn_shop": {"id": "Bakar warung saingan", "en": "Burn rival's shop"},
    "npc_mission_collect_debt": {"id": "Tagih utang ke Debtor", "en": "Collect debt from Debtor"},
    "npc_mission_steal_data": {"id": "Curi data nasabah bank", "en": "Steal bank customer data"},
    "npc_mission_sabotage": {"id": "Sabotase gang lawan", "en": "Sabotage rival gang"},
    "npc_mission_protect_boss": {"id": "Lindungi bos dari raid", "en": "Protect the boss from raids"},
    "npc_scammer_fail": {"id": "Hehe, kena tipu! Kamu kehilangan {loss}. Next time jangan percaya orang kayak aku.", "en": "Hehe, gotcha! You lost {loss}. Next time don't trust people like me."},
    "npc_scammer_success": {"id": "Kamu berhasil membalikkan tipuan! Dapet {gain} dari si penipu.", "en": "You successfully turned the tables! Got {gain} from the scammer."},
    "npc_collector_no_debtors": {"id": "Tidak ada yang punya utang saat ini.", "en": "No one has any debt right now."},
    "npc_collector_no_debt": {"id": "Target tidak punya utang.", "en": "Target has no debt."},
    "npc_collector_success": {"id": "Beres! Aku tagih @{target} sebesar {amount}. Fee ku 30% ya.", "en": "Done! I collected from @{target} totaling {amount}. My fee is 30%."},
    "npc_collector_received": {"id": "💰 Kamu terima: {net}", "en": "💰 You received: {net}"},
    "menu_btn_contacts": {"id": "📇 Contacts", "en": "📇 Contacts"},
    "menu_btn_invite": {"id": "🔗 Invite", "en": "🔗 Invite"},
    "menu_btn_bank": {"id": "🏦 Bank", "en": "🏦 Bank"},
    "menu_btn_history": {"id": "📜 History", "en": "📜 History"},
    "menu_btn_invest": {"id": "💹 Investasi", "en": "💹 Invest"},
    "menu_btn_social": {"id": "🏴 Social", "en": "🏴 Social"},
    "menu_btn_world_news": {"id": "📰 World News", "en": "📰 World News"},
    "chaos_btn_traps": {"id": "🪤 Traps", "en": "🪤 Traps"},
    "chaos_btn_spy": {"id": "🕵️ Spy", "en": "🕵️ Spy"},
    "chaos_btn_sabotage": {"id": "💣 Sabotage", "en": "💣 Sabotage"},
    "chaos_btn_casino": {"id": "🎰 Casino", "en": "🎰 Casino"},
    "chaos_btn_lootbox": {"id": "🎁 Lootbox", "en": "🎁 Lootbox"},
    "chaos_btn_market": {"id": "🏪 Market", "en": "🏪 Market"},
    "chaos_btn_lunas": {"id": "💳 Lunas", "en": "💳 Pay Debt"},
    "profile_btn_achievements": {"id": "🏆 Achievements", "en": "🏆 Achievements"},
    "profile_btn_set_name": {"id": "⚙️ Set Name", "en": "⚙️ Set Name"},
    "gang_btn_create": {"id": "➕ Create", "en": "➕ Create"},
    "gang_btn_join": {"id": "🔗 Join", "en": "🔗 Join"},
    "gang_btn_leave": {"id": "🚪 Leave", "en": "🚪 Leave"},
    "gang_btn_vault": {"id": "🏦 Vault", "en": "🏦 Vault"},
    "bank_btn_deposit": {"id": "📥 Deposit", "en": "📥 Deposit"},
    "bank_btn_withdraw": {"id": "📤 Withdraw", "en": "📤 Withdraw"},
    "bank_btn_history": {"id": "📜 Riwayat", "en": "📜 History"},
    "casino_btn_slots": {"id": "🎰 Slots", "en": "🎰 Slots"},
    "casino_btn_blackjack": {"id": "🃏 Blackjack", "en": "🃏 Blackjack"},
    "casino_btn_roulette": {"id": "🎱 Roulette", "en": "🎱 Roulette"},
    "market_btn_shop": {"id": "🏪 Shop", "en": "🏪 Shop"},
    "market_btn_inventory": {"id": "🎒 Inventory", "en": "🎒 Inventory"},
    "lootbox_btn_buy_common": {"id": "📦 Common (200)", "en": "📦 Common (200)"},
    "lootbox_btn_buy_rare": {"id": "🎁 Rare (500)", "en": "🎁 Rare (500)"},
    "lootbox_btn_buy_epic": {"id": "💎 Epic (1200)", "en": "💎 Epic (1200)"},
    "lootbox_btn_buy_legendary": {"id": "👑 Legendary (3000)", "en": "👑 Legendary (3000)"},
    "lootbox_btn_open_common": {"id": "📂 Buka Common", "en": "📂 Open Common"},
    "lootbox_btn_open_rare": {"id": "📂 Buka Rare", "en": "📂 Open Rare"},
    "lootbox_btn_open_epic": {"id": "📂 Buka Epic", "en": "📂 Open Epic"},
    "lootbox_btn_open_legendary": {"id": "📂 Buka Legendary", "en": "📂 Open Legendary"},
    "trap_btn_fake_investment": {"id": "🎣 Fake Investment", "en": "🎣 Fake Investment"},
    "trap_btn_phishing": {"id": "📧 Phishing", "en": "📧 Phishing"},
    "trap_btn_tax_trap": {"id": "🧾 Tax Trap", "en": "🧾 Tax Trap"},
    "trap_btn_pyramid": {"id": "🔺 Pyramid", "en": "🔺 Pyramid"},
    "trap_btn_mafia_extortion": {"id": "💀 Mafia Extortion", "en": "💀 Mafia Extortion"},
    "npc_btn_loan_shark": {"id": "🧛 Loan Shark", "en": "🧛 Loan Shark"},
    "npc_btn_mafia_boss": {"id": "🕴️ Mafia Boss", "en": "🕴️ Mafia Boss"},
    "npc_btn_scammer": {"id": "🐍 Scammer", "en": "🐍 Scammer"},
    "npc_btn_collector": {"id": "💪 Collector", "en": "💪 Collector"},
    "court_btn_file_case": {"id": "⚖️ File Case", "en": "⚖️ File Case"},
    "court_btn_vote": {"id": "🗳️ Vote", "en": "🗳️ Vote"},
    "social_btn_court": {"id": "🏛️ Court", "en": "🏛️ Court"},
    "social_btn_npc": {"id": "🤖 NPC", "en": "🤖 NPC"},
    "utang_reply_prompt": {"id": "Reply pesan + ketik jumlah.\nContoh: `/utang 200` (sambil reply pesan target)", "en": "Reply to message + type amount.\nExample: `/utang 200` (while replying to target's message)"},
    "utang_format_help": {"id": "Reply pesan target atau ketik:\n`/utang @username <jumlah>`", "en": "Reply to target's message or type:\n`/utang @username <amount>`"},
    "nagih_format_help": {"id": "Reply pesan target atau ketik:\n`/nagih @username`", "en": "Reply to target's message or type:\n`/nagih @username`"},
    "jebak_format_help": {"id": "Reply pesan target atau ketik:\n`/jebak @username`", "en": "Reply to target's message or type:\n`/jebak @username`"},
    "lunas_no_debt": {"id": "✅ Kamu tidak punya utang! Bebas hutang! 🎉", "en": "✅ You have no debt! Debt free! 🎉"},
    "lunas_amount_not_number": {"id": "Jumlah harus angka.", "en": "Amount must be a number."},
    "lunas_min_amount": {"id": "Jumlah minimal 1.", "en": "Minimum amount is 1."},
    "lunas_insufficient": {"id": "Saldo kamu cuma {balance}. Gak cukup buat bayar {amount}.", "en": "Your balance is only {balance}. Not enough to pay {amount}."},
    "lunas_paid_to_player": {"id": "\n\n💸 Uang langsung dikirim ke @{target}!", "en": "\n\n💸 Money sent directly to @{target}!"},
    "lunas_paid_to_system": {"id": "\n\n🏛️ Uang lenyap ke sistem (bank sentral).", "en": "\n\n🏛️ Money disappeared into the system (central bank)."},
    "transfer_format_help": {"id": "Reply pesan target + jumlah, atau ketik:\n`/transfer @username <jumlah>`", "en": "Reply to target's message + amount, or type:\n`/transfer @username <amount>`"},
    "transfer_confirm": {"id": "⚠️ *Konfirmasi Transfer*\n\nTransfer {amount} ke @{target}?", "en": "⚠️ *Confirm Transfer*\n\nTransfer {amount} to @{target}?"},
    "transfer_success_confirm": {"id": "✅ *Transfer Berhasil!*\n{amount} ke @{target}", "en": "✅ *Transfer Successful!*\n{amount} to @{target}"},
    "transfer_error": {"id": "⚠️ Gagal memproses transaksi.", "en": "⚠️ Failed to process transaction."},
    "transfer_expired": {"id": "⏳ Waktu habis atau aksi kadaluarsa.", "en": "⏳ Time expired or action expired."},
    "transfer_cancelled": {"id": "❌ Dibatalkan.", "en": "❌ Cancelled."},
    "spy_help": {"id": "🕵️ *Spy System*\n\nGunakan: /spy @username\nAtau reply pesan target + /spy\nBiaya: {cost}\n\n📊 Spy Stats: {total} total | {successes} sukses | {failures} gagal", "en": "🕵️ *Spy System*\n\nUsage: /spy @username\nOr reply to target's message + /spy\nCost: {cost}\n\n📊 Spy Stats: {total} total | {successes} success | {failures} failed"},
    "sabotage_help": {"id": "💣 *Sabotage System*\n\nReply pesan target atau ketik:\n/sabotage <type> @username\n\nTipe:\n• `freeze` — Freeze balance target (1 jam)\n• `steal` — Curi uang target\n• `block_daily` — Block daily reward target\n\nBiaya: {cost}", "en": "💣 *Sabotage System*\n\nReply to target's message or type:\n/sabotage <type> @username\n\nTypes:\n• `freeze` — Freeze target's balance (1 hour)\n• `steal` — Steal target's money\n• `block_daily` — Block target's daily reward\n\nCost: {cost}"},
    "casino_help": {"id": "🎰 *Casino Debt War*\n\n📊 Statistik:\n• Total Bet: {total_bet}\n• Total Won: {total_won}\n• Total Lost: {total_lost}\n\nGunakan:\n• /slots <bet>\n• /bj <bet>\n• /roulette <bet> <red/black/even/odd/number>", "en": "🎰 *Casino Debt War*\n\n📊 Stats:\n• Total Bet: {total_bet}\n• Total Won: {total_won}\n• Total Lost: {total_lost}\n\nUsage:\n• /slots <bet>\n• /bj <bet>\n• /roulette <bet> <red/black/even/odd/number>"},
    "casino_slots_usage": {"id": "Gunakan: /slots <bet>\nContoh: /slots 100", "en": "Usage: /slots <bet>\nExample: /slots 100"},
    "casino_bj_usage": {"id": "Gunakan: /bj <bet>\nContoh: /bj 100", "en": "Usage: /bj <bet>\nExample: /bj 100"},
    "casino_roulette_usage": {"id": "Gunakan: /roulette <bet> <red/black/even/odd/number>\nContoh: /roulette 100 red", "en": "Usage: /roulette <bet> <red/black/even/odd/number>\nExample: /roulette 100 red"},
    "lootbox_help_header": {"id": "🎁 *Lootbox System*", "en": "🎁 *Lootbox System*"},
    "lootbox_price_header": {"id": "*Harga:*", "en": "*Prices:*"},
    "lootbox_inv_header": {"id": "*Inventory:*", "en": "*Inventory:*"},
    "lootbox_inv_empty": {"id": "(kosong)", "en": "(empty)"},
    "lootbox_help_footer": {"id": "\nGunakan:\n/lootbox buy <rarity>\n/lootbox open <rarity>", "en": "\nUsage:\n/lootbox buy <rarity>\n/lootbox open <rarity>"},
    "lootbox_usage": {"id": "Gunakan: /lootbox buy/open <rarity>", "en": "Usage: /lootbox buy/open <rarity>"},
    "lootbox_usage_full": {"id": "Gunakan: /lootbox buy <rarity> atau /lootbox open <rarity>", "en": "Usage: /lootbox buy <rarity> or /lootbox open <rarity>"},
    "market_help": {"id": "🏪 *Market / Shop*\n\n{items}\n\nGunakan: /buy <item_id>\nContoh: /buy shield_basic", "en": "🏪 *Market / Shop*\n\n{items}\n\nUsage: /buy <item_id>\nExample: /buy shield_basic"},
    "market_buy_usage": {"id": "Gunakan: /buy <item_id>", "en": "Usage: /buy <item_id>"},
    "inventory_title": {"id": "🎒 *Inventory*", "en": "🎒 *Inventory*"},
    "inventory_items_header": {"id": "*Items:*", "en": "*Items:*"},
    "inventory_shields_header": {"id": "*Active Shields:*", "en": "*Active Shields:*"},
    "inventory_shields_none": {"id": "(tidak ada)", "en": "(none)"},
    "court_help_title": {"id": "🏛️ *Pengadilan Debt War*", "en": "🏛️ *Debt War Court*"},
    "court_cases_header": {"id": "*Kasus Tertunda:*", "en": "*Pending Cases:*"},
    "court_no_cases": {"id": "Tidak ada kasus tertunda.", "en": "No pending cases."},
    "court_help_footer": {"id": "\nGunakan:\n/sue @user <tuduhan>\n/vote <case_id> <guilty/innocent>", "en": "\nUsage:\n/sue @user <charge>\n/vote <case_id> <guilty/innocent>"},
    "court_case_id_number": {"id": "Case ID harus angka.", "en": "Case ID must be a number."},
    "court_vote_choice": {"id": "Vote: guilty atau innocent", "en": "Vote: guilty or innocent"},
    "gang_vault_hint": {"id": "\n\n💡 Gunakan: /gang vault deposit/withdraw <jumlah>", "en": "\n\n💡 Usage: /gang vault deposit/withdraw <amount>"},
    "profile_display_name_label": {"id": "📛 Nama", "en": "📛 Name"},
    "profile_borrowed_from": {"id": "\n\n📌 *Diutangin oleh:*", "en": "\n\n📌 *Lent by:*"},
    "profile_lent_to": {"id": "\n\n📌 *Kamu ngutangin:*", "en": "\n\n📌 *You lent to:*"},
    "stats_chaos_score_label": {"id": "💀 Chaos Score: *{score}*", "en": "💀 Chaos Score: *{score}*"},
    "stats_title_label": {"id": "👑 Title: *{title}*", "en": "👑 Title: *{title}*"},
    "stats_total_lent_label": {"id": "💰 Total Pinjaman: {amount}", "en": "💰 Total Lent: {amount}"},
    "stats_total_collected_label": {"id": "💸 Total Tagihan: {amount}", "en": "💸 Total Collected: {amount}"},
    "stats_traps_label": {"id": "🪤 Jebakan: {count} ({rate} sukses)", "en": "🪤 Traps: {count} ({rate} success)"},
    "stats_peak_balance_label": {"id": "🏔️ Saldo Tertinggi: {amount}", "en": "🏔️ Peak Balance: {amount}"},
    "stats_bankruptcies_label": {"id": "💀 Bangkrut: {count}x", "en": "💀 Bankruptcies: {count}x"},
    "stats_daily_claimed_label": {"id": "🎁 Daily Diklaim: {count}x", "en": "🎁 Daily Claimed: {count}x"},
    "stats_daily_streak_label": {"id": "🔥 Daily Streak: {days} hari", "en": "🔥 Daily Streak: {days} days"},
    "credit_skor_label": {"id": "📊 Skor: *{score}/1000*", "en": "📊 Score: *{score}/1000*"},
    "credit_tier_label": {"id": "🏅 Tier: *{tier} ({label})*", "en": "🏅 Tier: *{tier} ({label})*"},
    "credit_mod_interest": {"id": "🔹 Mod Bunga: {value}x", "en": "🔹 Interest Mod: {value}x"},
    "credit_mod_trap": {"id": "🔹 Mod Jebakan: {value}x", "en": "🔹 Trap Mod: {value}x"},
    "credit_mod_spy": {"id": "🔹 Mod Spy: {value}x", "en": "🔹 Spy Mod: {value}x"},
    "credit_repaid_total": {"id": "✅ Total Dibayar: {amount}", "en": "✅ Total Repaid: {amount}"},
    "credit_defaulted_total": {"id": "❌ Total Gagal Bayar: {amount}", "en": "❌ Total Defaulted: {amount}"},
    "titles_header": {"id": "👑 *Title / Rank*", "en": "👑 *Title / Rank*"},
    "titles_current_label": {"id": "🎯 Title Aktif: *{title}*", "en": "🎯 Active Title: *{title}*"},
    "titles_all_header": {"id": "🏅 *Semua Title:*", "en": "🏅 *All Titles:*"},
    "titles_click_hint": {"id": "\nKlik title yang sudah di-unlock untuk mengaktifkannya.", "en": "\nClick an unlocked title to activate it."},
    "titles_activated": {"id": "✅ Title aktif diubah ke: *{name}*", "en": "✅ Active title changed to: *{name}*"},
    "titles_active_mark": {"id": " 👈 AKTIF", "en": " 👈 ACTIVE"},
    "history_header": {"id": "📜 *Riwayat Transaksi*\n💰 Saldo: *{balance}*", "en": "📜 *Transaction History*\n💰 Balance: *{balance}*"},
    "history_empty": {"id": "Belum ada transaksi.", "en": "No transactions yet."},
    "history_type_utang": {"id": "Pinjamkan", "en": "Lend"},
    "history_type_nagih": {"id": "Tagihan", "en": "Collection"},
    "history_type_jebak_success": {"id": "Jebakan Berhasil", "en": "Trap Success"},
    "history_type_jebak_fail": {"id": "Jebakan Gagal", "en": "Trap Failed"},
    "history_type_transfer": {"id": "Transfer", "en": "Transfer"},
    "history_type_interest": {"id": "Bunga", "en": "Interest"},
    "history_type_interest_profit": {"id": "Bunga Masuk", "en": "Interest Earned"},
    "history_type_daily": {"id": "Daily Reward", "en": "Daily Reward"},
    "history_type_lootbox": {"id": "Lootbox", "en": "Lootbox"},
    "history_type_bank_deposit": {"id": "Deposit Bank", "en": "Bank Deposit"},
    "history_type_bank_withdraw": {"id": "Tarik Bank", "en": "Bank Withdraw"},
    "history_type_trap": {"id": "Trap", "en": "Trap"},
    "history_type_spy": {"id": "Spy", "en": "Spy"},
    "history_type_sabotage": {"id": "Sabotase", "en": "Sabotage"},
    "history_type_system": {"id": "Sistem", "en": "System"},
    "history_type_invest_buy": {"id": "Beli Investasi", "en": "Buy Investment"},
    "history_type_invest_sell": {"id": "Jual Investasi", "en": "Sell Investment"},
    "history_more_btn": {"id": "⬇️ Lainnya", "en": "⬇️ More"},
    "leaderboard_not_found": {"id": "Leaderboard gak ditemukan.", "en": "Leaderboard not found."},
    "leaderboard_error": {"id": "⚠️ Error memuat leaderboard.", "en": "⚠️ Error loading leaderboard."},
    "shop_header": {"id": "🏪 *Debt War Shop*\n\n💎 Gems kamu: *{gems}*\n🎟️ Season Pass: {sp_status}\n\nPilih produk:\n", "en": "🏪 *Debt War Shop*\n\n💎 Your Gems: *{gems}*\n🎟️ Season Pass: {sp_status}\n\nChoose a product:\n"},
    "shop_sp_active": {"id": "✅ Aktif", "en": "✅ Active"},
    "shop_sp_inactive": {"id": "❌ Belum", "en": "❌ Not Active"},
    "shop_gems_info": {"id": "💎 *Pakai Gems*\n\nKamu punya *{gems} Gems*.\n\nGems bisa dipake buat:\n• Legendary Lootbox — 100 Gems\n• Instant Cooldown — 20 Gems\n• Ganti Title — 50 Gems\n• Season XP Boost (24h) — 40 Gems\n\nFitur ini akan datang segera!", "en": "💎 *Use Gems*\n\nYou have *{gems} Gems*.\n\nGems can be used for:\n• Legendary Lootbox — 100 Gems\n• Instant Cooldown — 20 Gems\n• Change Title — 50 Gems\n• Season XP Boost (24h) — 40 Gems\n\nThis feature coming soon!"},
    "shop_invoice": {"id": "🧾 *Invoice #{id}*\n\n{product}\nTotal: *{total}*", "en": "🧾 *Invoice #{id}*\n\n{product}\nTotal: *{total}*"},
    "shop_payment_unavailable": {"id": "⚠️ *Pembayaran otomatis belum aktif.*\n\nOwner bot sedang mengatur metode pembayaran.\nSementara ini bisa hubungi owner langsung.", "en": "⚠️ *Automated payment not yet active.*\n\nBot owner is setting up the payment method.\nFor now, contact the owner directly."},
    "invest_menu_desc": {"id": "💹 *Pasar Investasi*\n\nPilih instrumen investasi:\n• Harga saham & reksadana berubah tiap jam\n• Obligasi return tetap\n• Terpengaruh oleh World Events!", "en": "💹 *Investment Market*\n\nChoose an investment instrument:\n• Stock & mutual fund prices change hourly\n• Bonds have fixed returns\n• Affected by World Events!"},
    "invest_portfolio_empty": {"id": "📂 *Portfolio Kamu*\n\nKosong. Beli instrumen dulu ya!", "en": "📂 *Your Portfolio*\n\nEmpty. Buy some instruments first!"},
    "invest_portfolio_title": {"id": "📂 *Portfolio Kamu*", "en": "📂 *Your Portfolio*"},
    "invest_buy_usage": {"id": "Gunakan: /investbuy <type> <id> <jumlah>\nContoh: /investbuy stock TECH 5000", "en": "Usage: /investbuy <type> <id> <amount>\nExample: /investbuy stock TECH 5000"},
    "invest_sell_usage": {"id": "Gunakan: /investsell <type> <id>\nContoh: /investsell stock TECH", "en": "Usage: /investsell <type> <id>\nExample: /investsell stock TECH"},
    "invest_amount_not_number": {"id": "Jumlah harus angka.", "en": "Amount must be a number."},
    "invest_min_amount": {"id": "Jumlah minimal 1.", "en": "Minimum amount is 1."},
    "setname_welcome": {"id": "👋 Selamat datang di Debt War!\n\nSebelum mulai, kamu harus buat nama display dulu.\n\nGunakan: `/setname <nama>`\nContoh: `/setname Fariz Ganteng`\n\nMaks 20 karakter. Huruf, angka, spasi aja.", "en": "👋 Welcome to Debt War!\n\nBefore starting, you need to set a display name.\n\nUsage: `/setname <name>`\nExample: `/setname Fariz Ganteng`\n\nMax 20 characters. Letters, numbers, spaces only."},
    "setname_usage": {"id": "Gunakan: `/setname <nama>`\nContoh: `/setname Fariz Ganteng`\n\nMaks 20 karakter. Huruf, angka, spasi, dan underscore aja.", "en": "Usage: `/setname <name>`\nExample: `/setname Fariz Ganteng`\n\nMax 20 characters. Letters, numbers, spaces, and underscores only."},
    "setname_invalid_chars": {"id": "Nama cuma boleh huruf, angka, spasi, dan underscore.", "en": "Name can only contain letters, numbers, spaces, and underscores."},
    "setname_success": {"id": "✅ Nama display diubah jadi: *{name}*", "en": "✅ Display name changed to: *{name}*"},
    "setname_ready": {"id": "\n\n🔥 Sekarang kamu bisa main! Ketik /menu untuk mulai.", "en": "\n\n🔥 Now you can play! Type /menu to start."},
    "traps_list_title": {"id": "🪤 *Advanced Traps*\n\n{trap_list}\n\nGunakan: /trap <nama> @username\nContoh: /trap phishing @fariz", "en": "🪤 *Advanced Traps*\n\n{trap_list}\n\nUsage: /trap <name> @username\nExample: /trap phishing @fariz"},
    "traps_list_item": {"id": "• *{name}*\n  Rate: {rate}% | DMG: {min}-{max}\n  CD: {cd}s | Cost: {cost}", "en": "• *{name}*\n  Rate: {rate}% | DMG: {min}-{max}\n  CD: {cd}s | Cost: {cost}"},
    "traps_success": {"id": "🪤 *{name} BERHASIL!*\n\n🎯 Target: @{target}\n💥 Damage: +{damage} debt\n💰 Reward: +{reward}", "en": "🪤 *{name} SUCCESS!*\n\n🎯 Target: @{target}\n💥 Damage: +{damage} debt\n💰 Reward: +{reward}"},
    "traps_fail": {"id": "❌ *{name} GAGAL!*\n\nJebakan tidak mempan ke @{target}.", "en": "❌ *{name} FAILED!*\n\nTrap had no effect on @{target}."},
    "invite_text": {"id": "🔗 *Invite Link*\n\nKirim link ini ke temenmu:\n`{link}`\n\nKalo dia join, kalian otomatis terhubung!", "en": "🔗 *Invite Link*\n\nSend this link to your friends:\n`{link}`\n\nWhen they join, you'll be auto-connected!"},
    "contacts_empty": {"id": "📇 *Contacts*\n\nKamu belum punya kontak.\nMain sama orang dulu, atau gunakan `/invite` buat ngajak temen!", "en": "📇 *Contacts*\n\nYou don't have any contacts yet.\nPlay with someone first, or use `/invite` to invite friends!"},
    "contacts_not_found": {"id": "📇 *Contacts*\n\nGak ada kontak cocok dengan \"{query}\".", "en": "📇 *Contacts*\n\nNo contacts matching \"{query}\"."},
    "contacts_pending": {"id": "⏳ (undang dulu!)", "en": "⏳ (invite first!)"},
    "player_usage": {"id": "Gunakan: `/player <user_id>`", "en": "Usage: `/player <user_id>`"},
    "player_id_not_number": {"id": "User ID harus angka.", "en": "User ID must be a number."},
    "player_not_found": {"id": "Player tidak ditemukan.", "en": "Player not found."},
    "player_info": {"id": "👤 *Player Info*\n\nID: `{id}`\nNama: {name}\nBalance: {balance}\nUtang: {debt}", "en": "👤 *Player Info*\n\nID: `{id}`\nName: {name}\nBalance: {balance}\nDebt: {debt}"},
    "start_welcome": {"id": "👋 Selamat datang, {name}!", "en": "👋 Welcome, {name}!"},
    "start_ghost_unknown": {"id": "\n📬 @{name} melakukan {action} ({amount})", "en": "\n📬 @{name} did {action} ({amount})"},
    "menu_needs_name": {"id": "Kamu harus set nama dulu! Ketik /setname", "en": "You must set a name first! Type /setname"},
    "menu_rate_limit": {"id": "⏳ Tenang... ({remaining}/40 per menit)", "en": "⏳ Slow down... ({remaining}/40 per minute)"},
    "menu_achievements_title": {"id": "🏆 *Achievements*", "en": "🏆 *Achievements*"},
    "menu_achievements_empty": {"id": "Belum ada achievement. Ayo main!", "en": "No achievements yet. Go play!"},
    "menu_profile_settings": {"id": "⚙️ *Pengaturan Profil*\n\nGunakan `/setname <nama>` untuk ganti nama display.\nContoh: `/setname Fariz Ganteng`", "en": "⚙️ *Profile Settings*\n\nUse `/setname <name>` to change your display name.\nExample: `/setname Fariz Ganteng`"},
    "menu_social_hub": {"id": "🏴 *Social Hub*\n\nPilih menu sosial:", "en": "🏴 *Social Hub*\n\nChoose social menu:"},
    "menu_invite_link": {"id": "🔗 *Invite Link*\n\nKirim link ini ke temenmu:\n`{link}`", "en": "🔗 *Invite Link*\n\nSend this link to your friends:\n`{link}`"},
    "menu_contacts_empty": {"id": "📇 *Contacts*\n\nKamu belum punya kontak.\nMain sama orang dulu, atau gunakan `/invite`.", "en": "📇 *Contacts*\n\nYou don't have any contacts yet.\nPlay with someone first, or use `/invite`."},
    "menu_world_news_header": {"id": "📰 *WORLD NEWS*\n🔄 Diperbarui: {time}", "en": "📰 *WORLD NEWS*\n🔄 Updated: {time}"},
    "menu_world_news_timer": {"id": "⏳ Sisa: {mins} menit", "en": "⏳ Remaining: {mins} minutes"},
    "menu_world_news_latest": {"id": "📌 *Berita Terkini*", "en": "📌 *Latest News*"},
    "menu_world_news_none": {"id": "• Belum ada berita terkini.", "en": "• No latest news."},
    "menu_world_news_history": {"id": "📋 *Riwayat Event*", "en": "📋 *Event History*"},
    "menu_spy_info": {"id": "🕵️ *Spy System*\n\nLihat estimasi saldo & utang target.\n\n• Biaya: *{cost}*\n• Cooldown: 2 menit\n• Success rate: 70%\n• Gagal: kena denda {fine}\n• Terdeteksi: target dapat notifikasi\n\nGunakan: `/spy @username`", "en": "🕵️ *Spy System*\n\nView target's estimated balance & debt.\n\n• Cost: *{cost}*\n• Cooldown: 2 minutes\n• Success rate: 70%\n• Fail: fined {fine}\n• Detected: target gets notified\n\nUsage: `/spy @username`"},
    "menu_sabotage_info": {"id": "💣 *Sabotage System*\n\nTipe:\n• `freeze` — freeze akun target 1 jam\n• `steal` — curi saldo target ({min}-{max})\n• `block_daily` — block daily reward target\n\n• Biaya: *{cost}*\n• Cooldown: 5 menit\n• Success rate: 55%\n• Gagal: kena denda {fine}\n\nGunakan: `/sabotage <type> @username`", "en": "💣 *Sabotage System*\n\nTypes:\n• `freeze` — freeze target's account 1 hour\n• `steal` — steal target's balance ({min}-{max})\n• `block_daily` — block target's daily reward\n\n• Cost: *{cost}*\n• Cooldown: 5 minutes\n• Success rate: 55%\n• Fail: fined {fine}\n\nUsage: `/sabotage <type> @username`"},
    "menu_casino_info": {"id": "🎰 *Casino Debt War*\n\nGunakan:\n/slots <bet>\n/bj <bet>\n/roulette <bet> <choice>", "en": "🎰 *Casino Debt War*\n\nUsage:\n/slots <bet>\n/bj <bet>\n/roulette <bet> <choice>"},
    "menu_market_info": {"id": "🏪 /market — Lihat shop\n/buy <item> — Beli item\n/inv — Inventory", "en": "🏪 /market — View shop\n/buy <item> — Buy item\n/inv — Inventory"},
    "menu_lootbox_info": {"id": "🎁 *Lootbox System*\n\nBuka lootbox untuk dapat hadiah random!\n\n• Common — {common} (uang, debt bomb)\n• Rare — {rare} (uang, shield)\n• Epic — {epic} (uang besar, chaos buff)\n• Legendary — {legendary} (uang gede, title unlock)\n\nGunakan:\n/lootbox buy <rarity>\n/lootbox open <rarity>", "en": "🎁 *Lootbox System*\n\nOpen lootboxes for random rewards!\n\n• Common — {common} (money, debt bomb)\n• Rare — {rare} (money, shield)\n• Epic — {epic} (big money, chaos buff)\n• Legendary — {legendary} (huge money, title unlock)\n\nUsage:\n/lootbox buy <rarity>\n/lootbox open <rarity>"},
    "menu_traps_info": {"id": "🪤 *Advanced Traps*\n\nGunakan: `/trap <type> @user`\n\n• `fake_investment` — 35% | 80-300 dmg | {c0}\n• `phishing_trap` — 40% | 60-200 dmg | {c1}\n• `tax_trap` — 30% | 100-400 dmg | {c2}\n• `pyramid_scheme` — 25% | 150-500 dmg | {c3}\n• `mafia_extortion` — 20% | 200-800 dmg | {c4}\n\nKetik `/traps` untuk detail lengkap.", "en": "🪤 *Advanced Traps*\n\nUsage: `/trap <type> @user`\n\n• `fake_investment` — 35% | 80-300 dmg | {c0}\n• `phishing_trap` — 40% | 60-200 dmg | {c1}\n• `tax_trap` — 30% | 100-400 dmg | {c2}\n• `pyramid_scheme` — 25% | 150-500 dmg | {c3}\n• `mafia_extortion` — 20% | 200-800 dmg | {c4}\n\nType `/traps` for full details."},
    "menu_lunas_info": {"id": "💳 Gunakan: /lunas <jumlah> @player\nContoh:\n/lunas 500 — bayar ke sistem\n/lunas 500 @user — bayar langsung ke player\n/lunas — lunasin semua", "en": "💳 Usage: /lunas <amount> @player\nExample:\n/lunas 500 — pay to system\n/lunas 500 @user — pay directly to player\n/lunas — pay all"},
    "menu_bank_usage": {"id": "🏦 Gunakan:\n/bank deposit <jumlah>\n/bank withdraw <jumlah>", "en": "🏦 Usage:\n/bank deposit <amount>\n/bank withdraw <amount>"},
    "menu_casino_sub_slots": {"id": "🎰 Gunakan: /slots <bet>", "en": "🎰 Usage: /slots <bet>"},
    "menu_casino_sub_bj": {"id": "🃏 Gunakan: /bj <bet>", "en": "🃏 Usage: /bj <bet>"},
    "menu_casino_sub_roulette": {"id": "🎱 Gunakan: /roulette <bet> <red/black/even/odd/number>", "en": "🎱 Usage: /roulette <bet> <red/black/even/odd/number>"},
    "menu_npc_info": {"id": "🤖 *NPC Interaktif*\n\n🧛 *loan_shark* — Boris si Rentenir\n   Pinjaman kilat, bunga tinggi\n   • `borrow` — Pinjem duit (otomatis +bunga)\n   • `pay` — Bayar utang ke Boris\n\n🕴️ *mafia_boss* — Don Corleone\n   Misi-misi gelap\n   • `mission` — Ambil misi random + reward\n\n🐍 *scammer* — Jimmy Tipu\n   Ahli phishing\n   • `phish` — Coba tipu balik (60% berhasil)\n\n💪 *collector* — Rambo Collector\n   Bantu nagih utang orang (fee 30%)\n   • `help_collect` — Tagih random debtor\n\nContoh: `/npc loan_shark borrow`", "en": "🤖 *Interactive NPCs*\n\n🧛 *loan_shark* — Boris the Loan Shark\n   Quick loans, high interest\n   • `borrow` — Borrow money (auto +interest)\n   • `pay` — Pay debt to Boris\n\n🕴️ *mafia_boss* — Don Corleone\n   Dark missions\n   • `mission` — Take random mission + reward\n\n🐍 *scammer* — Jimmy the Scammer\n   Phishing expert\n   • `phish` — Try to scam back (60% success)\n\n💪 *collector* — Rambo Collector\n   Help collect others' debts (30% fee)\n   • `help_collect` — Collect from random debtor\n\nExample: `/npc loan_shark borrow`"},
    "menu_court_info": {"id": "🏛️ Gunakan:\n/sue @user <tuduhan>\n/vote <case_id> <guilty/innocent>", "en": "🏛️ Usage:\n/sue @user <charge>\n/vote <case_id> <guilty/innocent>"},
    "menu_error": {"id": "⚠️ Terjadi error. Silakan coba lagi.", "en": "⚠️ An error occurred. Please try again."},
    "spy_result_title": {"id": "🕵️ *Hasil Spy*", "en": "🕵️ *Spy Result*"},
    "spy_result_target": {"id": "🎯 Target: @{username}", "en": "🎯 Target: @{username}"},
    "spy_balance_est": {"id": "💰 Estimasi Saldo: ~{balance}", "en": "💰 Est. Balance: ~{balance}"},
    "spy_debt_est": {"id": "💳 Estimasi Utang: ~{debt}", "en": "💳 Est. Debt: ~{debt}"},
    "spy_chaos_score_label": {"id": "💀 Chaos Score: {score}", "en": "💀 Chaos Score: {score}"},
    "spy_last_active": {"id": "📅 Last Active: {date}", "en": "📅 Last Active: {date}"},
    "spy_last_active_unknown": {"id": "Tidak diketahui", "en": "Unknown"},
    "spy_detected": {"id": "🚨 *Kamu terdeteksi!* Target mendapat notifikasi!", "en": "🚨 *You were detected!* Target got notified!"},
    "drama_template_0": {"id": "{user} baru saja menipu {count} orang dalam 10 menit. Chaos level: over 9000!", "en": "{user} just scammed {count} people in 10 minutes. Chaos level: over 9000!"},
    "drama_template_1": {"id": "Laporan dari pasar gelap: {user} diduga menjual utang palsu ke {count} korban.", "en": "Black market report: {user} suspected of selling fake debt to {count} victims."},
    "drama_template_2": {"id": "BREAKING: Ekonomi Debt War sedang goyang! {user} diduga dalang di balik kekacauan ini.", "en": "BREAKING: Debt War economy is shaking! {user} suspected mastermind behind this chaos."},
    "drama_template_3": {"id": "Rumor beredar: {user} bersekutu dengan mafia untuk mengontrol pasar utang.", "en": "Rumors circulate: {user} allied with mafia to control the debt market."},
    "drama_template_4": {"id": "{user} tertangkap kamera sedang merayakan setelah menjebak {count} orang.", "en": "{user} caught on camera celebrating after trapping {count} people."},
    "drama_template_5": {"id": "Krisis kepercayaan melanda! {user} dituduh sebagai biang kerok utang macet.", "en": "Trust crisis strikes! {user} accused of being the mastermind behind bad debts."},
    "drama_template_6": {"id": "Wanted: {user} — hadiah {bounty} bagi siapa yang berhasil membalaskan dendam.", "en": "Wanted: {user} — reward {bounty} for anyone who gets revenge."},
    "drama_template_7": {"id": "Ledakan ekonomi! {user} baru saja mentransfer kekayaan dalam jumlah besar.", "en": "Economic explosion! {user} just transferred a massive fortune."},
    "drama_template_8": {"id": "Bank sentral Debt War mengeluarkan peringatan: waspadai aktivitas {user}.", "en": "Debt War central bank warns: beware of {user}'s activities."},
    "drama_template_9": {"id": "Serial scammer {user} kembali beraksi! {count} korbannya melapor hari ini.", "en": "Serial scammer {user} strikes again! {count} victims reported today."},
    "drama_template_10": {"id": "Dunia Debt War berguncang! {user} mencapai rekor chaos baru.", "en": "Debt War world shaken! {user} reached a new chaos record."},
    "drama_template_11": {"id": "Kartel bawah tanah mengumumkan: {user} adalah most wanted player minggu ini.", "en": "Underground cartel announces: {user} is this week's most wanted player."},
    "drama_event_debt_crisis": {"id": "📉 *KRISIS UTANG* 📉\n\nSemua utang naik {percent}% drastis! Waktunya waspada!", "en": "📉 *DEBT CRISIS* 📉\n\nAll debts skyrocketed {percent}%! Time to be alert!"},
    "drama_event_tax_season": {"id": "💰 *MUSIM PAJAK* 💰\n\nPemerintah memotong saldo pemain sebesar {percent}%!", "en": "💰 *TAX SEASON* 💰\n\nGovernment cuts player balances by {percent}%!"},
    "drama_event_gov_audit": {"id": "🔍 *AUDIT PAJAK* 🔍\n\nSemua transaksi diaudit! Pajak naik {percent}%!", "en": "🔍 *TAX AUDIT* 🔍\n\nAll transactions audited! Tax increased {percent}%!"},
    "drama_event_inflation": {"id": "📈 *INFLASI* 📈\n\nHarga-harga naik! Biaya transaksi meningkat {percent}%!", "en": "📈 *INFLATION* 📈\n\nPrices rising! Transaction costs increased {percent}%!"},
    "drama_event_crypto_crash": {"id": "📉 *CRYPTO CRASH* 📉\n\nPasar crypto ambruk! Semua kehilangan {percent}% saldo!", "en": "📉 *CRYPTO CRASH* 📉\n\nCrypto market crashed! Everyone lost {percent}% balance!"},
    "drama_event_stimulus": {"id": "🎁 *STIMULUS EKONOMI* 🎁\n\nPemerintah memberi {amount} gratis ke semua pemain!", "en": "🎁 *ECONOMIC STIMULUS* 🎁\n\nGovernment gives {amount} free to all players!"},
    "drama_event_default": {"id": "📰 *WORLD EVENT*\n\nTerjadi peristiwa global di Debt War!", "en": "📰 *WORLD EVENT*\n\nA global event occurred in Debt War!"},
    "court_sue_self": {"id": "Gugat diri sendiri? Aneh.", "en": "Suing yourself? Weird."},
    "court_need_fee": {"id": "Butuh {fee} untuk bayar pengacara.", "en": "Need {fee} to pay the lawyer."},
    "court_case_filed": {"id": "🏛️ *Gugatan diajukan!*\n\nKasus #{case_id}\nTerdakwa: @{defendant}\nTuduhan: {charge}\n\nVoting akan berlangsung 1 jam.", "en": "🏛️ *Case filed!*\n\nCase #{case_id}\nDefendant: @{defendant}\nCharge: {charge}\n\nVoting will last 1 hour."},
    "court_case_not_found": {"id": "Kasus tidak ditemukan atau sudah diputus.", "en": "Case not found or already decided."},
    "court_vote_recorded": {"id": "🗳️ Vote direkam! Kamu memilih *{vote}*.", "en": "🗳️ Vote recorded! You voted *{vote}*."},
    "court_verdict_guilty": {"id": "⚖️ *VERDIK: BERSALAH!*\n\nDenda {fine} dibayarkan ke penggugat.", "en": "⚖️ *VERDICT: GUILTY!*\n\nFine of {fine} paid to the plaintiff."},
    "court_verdict_innocent": {"id": "⚖️ *VERDIK: TIDAK BERSALAH!*\n\nTerdakwa dibebaskan.", "en": "⚖️ *VERDICT: NOT GUILTY!*\n\nDefendant acquitted."},
    "invest_label_stock": {"id": "Saham", "en": "Stock"},
    "invest_label_mf": {"id": "Reksadana", "en": "Mutual Fund"},
    "invest_label_bond": {"id": "Obligasi", "en": "Bond"},
    "invest_insufficient": {"id": "Saldo gak cukup. Kamu cuma punya {balance}.", "en": "Insufficient balance. You only have {balance}."},
    "invest_not_found": {"id": "Instrumen gak ditemukan.", "en": "Instrument not found."},
    "invest_bought": {"id": "✅ Dibeli {shares} unit {name} seharga {price}.", "en": "✅ Bought {shares} units of {name} for {price}."},
    "invest_no_holding": {"id": "Kamu gak punya instrumen ini.", "en": "You don't own this instrument."},
    "invest_sold": {"id": "✅ Dijual {shares} unit {name}.\nDiterima: {total} ({pnl})", "en": "✅ Sold {shares} units of {name}.\nReceived: {total} ({pnl})"},
    "disclaimer_casino": {"id": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ *DISCLAIMER*\nFitur casino ini *hanya untuk hiburan* semata.\n• Tidak ada uang asli yang dipertaruhkan\n• Hanya menggunakan mata uang in-game (coins)\n• Semua hasil adalah random/acak\n• *18+* — Jika kamu di bawah 18 tahun, jangan gunakan fitur ini\n• Bermainlah dengan bijak dan bertanggung jawab\n\nDebt War tidak bertanggung jawab atas kerugian yang disebabkan oleh penggunaan fitur ini.", "en": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ *DISCLAIMER*\nThis casino feature is *for entertainment only*.\n• No real money is at stake\n• Uses in-game currency only (coins)\n• All results are random\n• *18+* — If you are under 18, do not use this feature\n• Play wisely and responsibly\n\nDebt War is not responsible for any losses caused by using this feature."},
    "disclaimer_lootbox": {"id": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ *DISCLAIMER*\nLootbox mengandung mekanisme *gacha* (random).\n• Tidak ada jaminan mendapatkan item tertentu\n• Habiskan coins dengan bijak\n• Fitur ini hanya untuk hiburan\n• *18+*\n", "en": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ *DISCLAIMER*\nLootbox contains *gacha* (random) mechanics.\n• No guarantee of getting specific items\n• Spend coins wisely\n• This feature is for entertainment only\n• *18+*\n"},
    "disclaimer_general": {"id": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ Debt War adalah game hiburan semata.\nTidak ada transaksi uang asli di dalam game ini.\nSemua fitur menggunakan mata uang virtual (coins).\nBermainlah dengan bijak. *18+*", "en": "\n\n━━━━━━━━━━━━━━━━━━\n⚠️ Debt War is a game for entertainment purposes only.\nNo real money transactions occur in this game.\nAll features use virtual currency (coins).\nPlay wisely. *18+*"},
    "confirm_yes": {"id": "✅ Ya", "en": "✅ Yes"},
    "confirm_cancel": {"id": "❌ Batal", "en": "❌ Cancel"},
    "shield_blocks_trap": {
        "id": "🛡️ @{target} memiliki *Basic Shield*! Jebakan tidak mempan.",
        "en": "🛡️ @{target} has a *Basic Shield*! Trap is ineffective.",
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
#!/bin/bash
# Production launcher for Debt War bot
# Usage: DEBTWAR_TOKEN=xxx ./run_production.sh

export DEBTWAR_TOKEN="${DEBTWAR_TOKEN}"

cd "$(dirname "$0")"
source venv/bin/activate

# Rotate old log
mkdir -p logs
mv logs/bot.log "logs/bot.$(date +%Y%m%d-%H%M%S).log" 2>/dev/null

# Run with auto-restart on crash
while true; do
    echo "[$(date)] Starting Debt War..."
    python3 main.py
    echo "[$(date)] Bot crashed! Restarting in 5 seconds..."
    sleep 5
done

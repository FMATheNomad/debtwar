import asyncio
import shutil
import logging
from datetime import datetime
from config import DB_FILE

logger = logging.getLogger(__name__)

BACKUP_DIR = "backups"


async def schedule_backup():
    import os
    os.makedirs(BACKUP_DIR, exist_ok=True)
    while True:
        await asyncio.sleep(21600)
        try:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            backup_path = f"{BACKUP_DIR}/debtwar.{timestamp}.db"
            shutil.copy2(DB_FILE, backup_path)
            logger.info(f"Database backed up: {backup_path}")

            backups = sorted(
                [f for f in os.listdir(BACKUP_DIR) if f.endswith(".db")],
                reverse=True,
            )
            while len(backups) > 48:
                os.remove(f"{BACKUP_DIR}/{backups.pop()}")
        except Exception as e:
            logger.error(f"Backup error: {e}")

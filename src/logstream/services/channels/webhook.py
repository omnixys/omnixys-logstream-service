import os
import httpx
from logstream.models.log_entry import LogEntry
from loguru import logger


async def send_webhook_alert(log: LogEntry):
    url = os.getenv("ALERT_WEBHOOK_URL")
    if not url:
        logger.warning("❌ Kein Webhook konfiguriert.")
        return

    payload = log.dict()

    try:
        async with httpx.AsyncClient() as client:
            await client.post(url, json=payload)
            logger.info("📡 Webhook-Alert gesendet.")
    except Exception as e:
        logger.error(f"Fehler beim Webhook-Alert: {e}")

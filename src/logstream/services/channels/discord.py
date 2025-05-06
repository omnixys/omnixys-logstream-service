import os
import httpx
from logstream.models.log_entry import LogEntry
from loguru import logger


async def send_discord_alert(log: LogEntry):
    url = os.getenv("DISCORD_WEBHOOK_URL")
    if not url:
        logger.warning("❌ Kein Discord Webhook konfiguriert.")
        return

    message = {
        "content": f"🔔 **ALERT vom Logging-Service**\n"
        f"🔥 `{log.service}` → **{log.level}**: {log.message}\n"
        f"🧾 Details: `{log.details}`"
    }

    try:
        async with httpx.AsyncClient() as client:
            await client.post(url, json=message)
            logger.info("📤 Discord-Alert gesendet.")
    except Exception as e:
        logger.error(f"Fehler beim Discord-Alert: {e}")

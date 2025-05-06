"""
Zentraler AlertService für mehrere Kanäle:
- E-Mail
- Discord Webhook
- Push/SMS/Webhook

Gesteuert über Umgebungsvariablen (.env).
"""

import os
from logstream.models.log_entry import LogEntry
from logstream.services.channels.discord import send_discord_alert
from logstream.services.channels.email import send_email_alert
from logstream.services.channels.webhook import send_webhook_alert


class AlertService:
    @staticmethod
    async def send_alert(log: LogEntry):
        """Sendet Alerts an alle aktivierten Kanäle."""

        if log.level not in ["ERROR", "AUDIT"]:
            return

        if os.getenv("ALERT_DISCORD_ENABLED", "false").lower() == "true":
            await send_discord_alert(log)

        if os.getenv("ALERT_EMAIL_ENABLED", "false").lower() == "true":
            await send_email_alert(log)

        if os.getenv("ALERT_WEBHOOK_ENABLED", "false").lower() == "true":
            await send_webhook_alert(log)

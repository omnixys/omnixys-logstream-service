import os
from loguru import logger
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from logstream.models.log_entry import LogEntry


async def send_email_alert(log: LogEntry):
    mail_to = os.getenv("ALERT_EMAIL_TO")
    if not mail_to:
        logger.warning("❌ Kein Empfänger für E-Mail konfiguriert.")
        return

    conf = ConnectionConfig(
        MAIL_USERNAME=os.getenv("EMAIL_USER"),
        MAIL_PASSWORD=os.getenv("EMAIL_PASS"),
        MAIL_FROM=os.getenv("EMAIL_FROM"),
        MAIL_PORT=int(os.getenv("EMAIL_PORT", 587)),
        MAIL_SERVER=os.getenv("EMAIL_HOST"),
        MAIL_TLS=True,
        MAIL_SSL=False,
        USE_CREDENTIALS=True,
    )

    message = MessageSchema(
        subject="🚨 Logging-Alert",
        recipients=[mail_to],
        body=f"""
            Service: {log.service}
            Level: {log.level}
            Nachricht: {log.message}
            Details: {log.details}
        """,
        subtype="plain",
    )

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
        logger.info("📧 E-Mail-Alert gesendet.")
    except Exception as e:
        logger.error(f"Fehler beim E-Mail-Alert: {e}")

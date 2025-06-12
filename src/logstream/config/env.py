from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Laden Sie die .env-Datei
load_dotenv(dotenv_path=".env")

class Env(BaseSettings):
    PROJECT_NAME: str = "Logstream Service"

    APP_ENV: str
    APP_DEBUG: str

    EXCEL_EXPORT_ENABLED: str
    EXPORT_FORMAT: str

    KAFKA_URI: str
    TEMPO_URI: str
    KEYS_PATH: str

    MONGODB_URI: str
    MONGODB_DB_NAME: str

    ALERT_DISCORD_ENABLED: str
    ALERT_EMAIL_ENABLED: str
    ALERT_WEBHOOK_ENABLED: str
    DISCORD_WEBHOOK_URL: str

    # E-Mail
    EMAIL_USER: str
    EMAIL_PASS: str
    EMAIL_FROM: str
    EMAIL_HOST: str
    EMAIL_PORT: str
    ALERT_EMAIL_TO: str

    # Webhook
    ALERT_WEBHOOK_URL: str

    class Config:
        env_file = ".env"  # Stellen Sie sicher, dass dies auf Ihre .env-Datei verweist
        env_file_encoding = "utf-8"
        case_sensitive = True

env = Env()

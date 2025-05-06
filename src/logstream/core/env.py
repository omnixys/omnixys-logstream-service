from pydantic_settings import BaseSettings
from pydantic import Field


class AppSettings(BaseSettings):
    APP_ENV: str = Field(..., description="Umgebung: development, production")
    APP_DEBUG: bool = Field(False, description="Debug-Modus aktivieren")

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


class KeycloakSettings(BaseSettings):
    KC_SERVICE_HOST: str
    KC_SERVICE_PORT: int
    KC_SERVICE_REALM: str
    KC_SERVICE_CLIENT_ID: str
    KC_SERVICE_SECRET: str
    CLIENT_SECRET: str

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


class AlertSettings(BaseSettings):
    ALERT_DISCORD_ENABLED: bool = False
    ALERT_EMAIL_ENABLED: bool = False
    ALERT_WEBHOOK_ENABLED: bool = False

    DISCORD_WEBHOOK_URL: str

    EMAIL_USER: str
    EMAIL_PASS: str
    EMAIL_FROM: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    ALERT_EMAIL_TO: str

    ALERT_WEBHOOK_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"

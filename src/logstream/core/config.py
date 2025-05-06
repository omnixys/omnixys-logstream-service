"""
Globale Auth- und Keycloak-Einstellungen.
"""

from pydantic_settings import BaseSettings


class AuthSettings(BaseSettings):
    keycloak_public_key: str  # PEM Format, ohne -----BEGIN/END-----
    keycloak_issuer: str = "https://keycloak.gentlecorp.dev/realms/gentlecorp"
    keycloak_audience: str = "logging-service"

    class Config:
        env_file = ".env"
        env_prefix = "KEYCLOAK_"

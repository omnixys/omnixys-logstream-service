"""
Zentrale Stelle zur Bereitstellung von Service-Instanzen
für Dependency Injection in REST- und GraphQL-Endpunkten.
"""

from fastapi import Depends
from functools import lru_cache
from logstream.core.env import (
    AppSettings,
    KeycloakSettings,
    AlertSettings,
)


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache()
def get_keycloak_settings() -> KeycloakSettings:
    return KeycloakSettings()


@lru_cache()
def get_alert_settings() -> AlertSettings:
    return AlertSettings()

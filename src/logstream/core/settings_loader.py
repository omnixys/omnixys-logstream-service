"""
Zentrale Zugriffsklasse für Settings via .env
Pfad: src/activity/core/settings_loader.py
"""

from functools import lru_cache
from logstream.core.env import (
    AppSettings,
    KeycloakSettings,
    AlertSettings,
)


class SettingsContainer:
    def __init__(self):
        self.app = AppSettings()
        self.keycloak = KeycloakSettings()
        self.alert = AlertSettings()


@lru_cache()
def get_settings() -> SettingsContainer:
    return SettingsContainer()

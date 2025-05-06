"""
Zeigt alle geladenen Konfigurationen aus der .env-Datei tabellarisch an.
Pfad: src/activity/tools/show_config.py
"""

from logstream.core.settings_loader import get_settings
from tabulate import tabulate

settings = get_settings()

data = [
    ("APP_ENV", settings.app.APP_ENV),
    ("APP_DEBUG", settings.app.APP_DEBUG),
    ("MONGODB_URI", settings.mongo.MONGODB_URI),
    ("MONGODB_DB_NAME", settings.mongo.MONGODB_DB_NAME),
    ("KC_SERVICE_HOST", settings.keycloak.KC_SERVICE_HOST),
    ("KC_SERVICE_PORT", settings.keycloak.KC_SERVICE_PORT),
    ("KC_SERVICE_REALM", settings.keycloak.KC_SERVICE_REALM),
    ("KC_SERVICE_CLIENT_ID", settings.keycloak.KC_SERVICE_CLIENT_ID),
    ("KC_SERVICE_SECRET", settings.keycloak.KC_SERVICE_SECRET),
    ("CLIENT_SECRET", settings.keycloak.CLIENT_SECRET),
    ("ALERT_DISCORD_ENABLED", settings.alert.ALERT_DISCORD_ENABLED),
    ("ALERT_EMAIL_ENABLED", settings.alert.ALERT_EMAIL_ENABLED),
    ("ALERT_WEBHOOK_ENABLED", settings.alert.ALERT_WEBHOOK_ENABLED),
    ("DISCORD_WEBHOOK_URL", settings.alert.DISCORD_WEBHOOK_URL),
    ("EMAIL_USER", settings.alert.EMAIL_USER),
    ("EMAIL_FROM", settings.alert.EMAIL_FROM),
    ("EMAIL_HOST", settings.alert.EMAIL_HOST),
    ("EMAIL_PORT", settings.alert.EMAIL_PORT),
    ("ALERT_EMAIL_TO", settings.alert.ALERT_EMAIL_TO),
    ("ALERT_WEBHOOK_URL", settings.alert.ALERT_WEBHOOK_URL),
]

print("\nKonfiguration aus .env geladen:\n")
print(tabulate(data, headers=["Variable", "Wert"], tablefmt="fancy_grid"))


def main():
    print("\nKonfiguration aus .env geladen:\n")
    print(tabulate(data, headers=["Variable", "Wert"], tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()

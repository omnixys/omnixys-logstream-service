"""
REST-Routen mit Keycloak-Authentifizierung und Rollenprüfung.
"""

from fastapi import Depends, Request, APIRouter
from logstream.core.keycloak_service import KeycloakService

router = APIRouter()


@router.get("/secure-logs")
async def get_secure_logs(request: Request):
    """
    Beispielroute mit Zugriffsschutz: Nur Benutzer mit Rolle 'Admin' oder 'auditor' dürfen zugreifen.
    """
    keycloak = KeycloakService(request)
    keycloak.assert_roles(["Admin", "auditor"])

    return {
        "message": "Du hast Zugriff auf geschützte Logs.",
        "user": keycloak.payload.get("preferred_username", "Unbekannt"),
        "roles": keycloak.get_roles(),
    }

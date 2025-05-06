"""
Keycloak-Authentifizierung für den Logging-Service.
Dekodiert und validiert JWTs via python-jose.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from typing import List
from logstream.core.config import AuthSettings


bearer_scheme = HTTPBearer()


def get_settings():
    return AuthSettings()


def decode_jwt(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    settings: AuthSettings = Depends(get_settings),
):
    """Validiert das JWT über Keycloaks Public Key."""
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            key=settings.keycloak_public_key,
            algorithms=["RS256"],
            audience=settings.keycloak_audience,
            issuer=settings.keycloak_issuer,
        )
        return payload
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token ungültig: {e}",
        )


def require_roles(roles: List[str]):
    """Factory-Funktion zur Rollenprüfung."""

    def wrapper(payload=Depends(decode_jwt)):
        user_roles = payload.get("realm_access", {}).get("roles", [])
        if not any(role in user_roles for role in roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Zugriff verweigert – benötigte Rollen: {roles}",
            )
        return payload

    return wrapper

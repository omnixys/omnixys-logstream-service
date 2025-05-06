"""
Definition des LogEntry-Dokuments für den Logging-Service.

Dieses Modell beschreibt strukturierte Logeinträge, die in MongoDB
gespeichert werden und u. a. über GraphQL abgefragt werden können.
"""

from beanie import Document
from datetime import datetime
from enum import Enum
from typing import Optional, Union
from pydantic import Field


class LogLevel(str, Enum):
    """
    Aufzählung der unterstützten Log-Level.
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    AUDIT = "AUDIT"


class LogEntry(Document):
    """
    Datenmodell für einen strukturierten Logeintrag.

    Dieses Dokument wird in MongoDB persistiert und kann über
    GraphQL- und REST-Endpunkte gelesen oder geschrieben werden.
    """

    timestamp: datetime = Field(..., description="Zeitpunkt des Log-Eintrags")
    level: LogLevel = Field(..., description="Schweregrad des Eintrags")
    message: str = Field(..., description="Kurze Beschreibung oder Nachricht")
    source: str = Field(
        ..., description="Herkunft des Eintrags, z. B. 'system' oder Service-Name"
    )
    service: str = Field(..., description="Service-Name, der das Log erzeugt")
    correlation_id: str = Field(
        ..., description="Eindeutige Korrelation zur Nachverfolgung"
    )
    details: Optional[dict[str, Union[str, int]]] = Field(
        default_factory=dict, description="Zusätzliche strukturierte Informationen"
    )

    class Settings:
        name = "logs"  # MongoDB-Collection-Name

    class Config:
        title = "LogEntry"

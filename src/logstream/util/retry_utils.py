"""
Allgemeine Retry-Hilfsfunktionen für Verbindungsaufbau zu externen Diensten.
Pfad: src/activity/utils/retry_utils.py
"""

import asyncio
from loguru import logger
from typing import Callable, Any


async def retry_async(
    func: Callable[[], Any],
    retries: int = 5,
    delay: float = 2.0,
    name: str = "Unbekannt",
) -> Any:
    """
    Führt eine asynchrone Funktion mehrfach aus, falls ein Fehler auftritt.

    :param func: Die aufzurufende Funktion
    :param retries: Anzahl Wiederholungen
    :param delay: Pause zwischen Versuchen (in Sekunden)
    :param name: Name für Logging-Zwecke
    """
    for attempt in range(1, retries + 1):
        try:
            result = await func()
            if attempt > 1:
                logger.success("{} verbunden nach {} Versuch(en).", name, attempt)
            return result
        except Exception as e:
            logger.warning(
                "{}: Versuch {}/{} fehlgeschlagen: {}", name, attempt, retries, e
            )
            if attempt == retries:
                logger.error(
                    "{} konnte nach {} Versuchen nicht verbunden werden.", name, retries
                )
                raise
            await asyncio.sleep(delay)

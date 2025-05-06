"""
REST-API für das Empfangen und Speichern von Logs per POST-Request.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from logstream.core.keycloak_service import KeycloakService
from logstream.models.log_entry import LogEntry
from logstream.core.kafka_producer import kafka_producer
from loguru import logger

router = APIRouter()


@router.post("/logs", status_code=status.HTTP_201_CREATED)
async def create_log(request: Request):
    """
    Nimmt einen Logeintrag entgegen, speichert ihn in MongoDB,
    und sendet ihn an Kafka – gesichert über Keycloak.
    """
    keycloak = KeycloakService(request)
    keycloak.assert_roles(["Admin", "auditor", "service-logger"])

    payload = await request.json()
    try:
        log = LogEntry(**payload)
        await log.insert()
        await kafka_producer.send(log.dict())

        logger.info(f"✅ Log gespeichert & an Kafka gesendet: {log.service}")
        return JSONResponse(
            status_code=201,
            content={"message": "Log gespeichert", "id": str(log.id)},
        )
    except Exception as e:
        logger.error(f"❌ Fehler beim Log-Speichern: {e}")
        return JSONResponse(
            status_code=400,
            content={"error": "Ungültige Logdaten", "details": str(e)},
        )

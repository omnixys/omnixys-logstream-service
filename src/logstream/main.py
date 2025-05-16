"""
Einstiegspunkt für den Logging-Service.
Initialisiert die FastAPI-App und konfiguriert die Lifespan-Logik.
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager
from logstream.banner import banner
from logstream.banner2 import shutdown_banner
from loguru import logger
from logstream.core.kafka_consumer import KafkaConsumerService
from logstream.util.retry_utils import retry_async


kafka_consumer = KafkaConsumerService()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialisiert externe Abhängigkeiten beim Start der Anwendung,
    und sorgt für deren sauberen Shutdown beim Beenden.
    """
    logger.info("⏳ Initialisiere logstream-Service...")
    # Retry-gestützte Initialisierung
    await retry_async(kafka_consumer.start, name="Kafka-Consumer")

    banner(app.routes)
    yield  # Hier laufen die App-Routen
    logger.info("🛑 Logging-Service wird beendet...")
    logger.info("🧹 Beispiel-Logs gelöscht.")
    await kafka_consumer.stop()
    shutdown_banner()


def create_app() -> FastAPI:
    """Erzeugt die FastAPI-Applikation mit Lifespan."""
    app = FastAPI(
        title="Omnixys logstream-Service",
        description="Zentraler Logging-Microservice mit Kafka und Loki-Anbindung",
        version="2025.05.16",
        lifespan=lifespan,
        debug=True,
    )

    return app


app = create_app()

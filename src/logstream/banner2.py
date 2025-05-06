"""
Shutdown-Banner beim Beenden des Servers.
"""

import sys
from datetime import datetime
from getpass import getuser
from socket import gethostname
from loguru import logger


def shutdown_banner() -> None:
    """Zeigt wichtige Informationen beim Server-Stopp an."""
    hostname = gethostname()

    logger.info("\n❌ Server-Stop eingeleitet ({})", datetime.utcnow().isoformat())
    logger.info("User          : {}", getuser())
    logger.info("Hostname      : {}", hostname)
    logger.info("Python-Version: {}.{}.{}", *sys.version_info[:3])
    logger.info("Bye!")

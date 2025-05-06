"""
Modul-Deklaration für das Projekt als Namensraum und CLI-Einstiegspunkt.

Ermöglicht:
- Import als Python-Package: `from logging import ...`
- Ausführung als Skript: `uv run logging`
- Start per Uvicorn/Hypercorn z.B.:

    uvicorn src.logging:app --reload --ssl-keyfile path --ssl-certfile path
"""

from logstream.asgi_server import run
from logstream.main import app

__all__ = ["app", "main"]


def main() -> None:
    """Einstiegspunkt für CLI-Aufrufe via `uv run logging`."""
    run()

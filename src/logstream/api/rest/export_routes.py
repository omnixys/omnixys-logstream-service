"""
REST-Endpunkt zum Bereitstellen von Export-Dateien.
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()
EXPORT_DIR = Path("exports/logs")


@router.get("/export/logs/{filename}", response_class=FileResponse)
async def download_log_file(filename: str):
    filepath = EXPORT_DIR / filename
    return FileResponse(
        path=filepath, filename=filename, media_type="application/octet-stream"
    )

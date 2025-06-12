import os
import httpx
import time


async def push_log_to_loki(
    log_message: str,
    level: str,
    service: str,
    message= str,
    context= str,
    timestamp= str,
    trace_id: str = "",
):
    ts_ns = str(int(time.time() * 1e9))
    payload = {
        "streams": [
            {
                "stream": {
                    "level": level.lower(),
                    "service_name": service,
                    "message": message,
                    "context": context,
                    "timestamp": timestamp,
                    "trace_id": trace_id or "unknown",
                },
                "values": [[ts_ns, log_message]],
            }
        ]
    }
    async with httpx.AsyncClient() as client:
        await client.post(
            os.environ.get("TEMPO_URI", "http://localhost:3100/loki/api/v1/push"),
            json=payload,
        )

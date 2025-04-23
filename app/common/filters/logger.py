import time
import json

from fastapi import Depends, Request, Response

from app.app_dependency import get_logging_service
from app.common.services.logging_service import LoggingService

async def log_filter(
    request: Request, 
    call_next,
):    
    logger = get_logging_service()

    # Read the request body (can only be done once unless we reset it)
    body = await request.body()

    try:
        # Try to parse and pretty-print as one-liner JSON
        body_json = json.loads(body.decode("utf-8"))
        body_str = json.dumps(body_json, separators=(",", ":"))
    except Exception:
        # If it's not JSON, just fallback to plain string
        body_str = body.decode("utf-8")

    logger.info(f"({request.method}) -> {request.url}")
    logger.info(f"(REQ) -- {body_str}")

    # Rebuild the request stream so the endpoint can still read it
    request._receive = lambda: {"type": "http.request", "body": body}

    # Continue with request
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    # Read response body
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk

    # Log the response
    logger.info(f"(RES) -- {response_body.decode('utf-8')}")
    logger.info(f"({request.method}) <- {duration:.4f}s")

    # Rebuild and return the response with the same body
    return Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )
import json
import time
from typing import Callable

from fastapi import Request, Response

from app.app_dependency import get_env_service, get_logging_service

# Assume these are your external services for environment and logging
env = get_env_service()  # Custom service
logger = get_logging_service()  # Custom service


async def log_middleware(request: Request, call_next: Callable):
    # Step 1: Read the request body (can only be done once unless we reset it)
    body = await request.body()

    try:
        # Parse and combine the original request body with URI info
        body_json: dict = json.loads(body.decode("utf-8"))
        body_str = (
            json.dumps(body_json)  # Pretty print for prod vs dev
            if env.settings.ENVIRONMENT == "prd"
            else json.dumps(body_json, indent=4)
        )
    except Exception:
        # If body can't be decoded, log raw body
        body_str = body.decode("utf-8")

    # Log the incoming request
    logger.info(f"(STA) -> ({request.method}) {request.url.path}")
    logger.info(f"(REQ) -- {body_str}")

    # Rebuild the request stream so the endpoint can still read it
    request._receive = lambda: {"type": "http.request", "body": body}

    # Step 2: Continue with the request processing
    start_time = time.time()  # Start time for duration measurement
    response = await call_next(request)
    duration = time.time() - start_time  # Calculate the duration

    # Step 3: Read the response body
    res = b""
    async for chunk in response.body_iterator:
        res += chunk

    try:
        # Combine response body with URI info
        res_json = json.loads(res.decode("utf-8"))
        res_str = (
            json.dumps(res_json)  # Pretty print for prod vs dev
            if env.settings.ENVIRONMENT == "prd"
            else json.dumps(res_json, indent=4)
        )
    except Exception:
        # If response can't be decoded, log raw body
        res_str = res.decode("utf-8")

    # Step 4: Log the outgoing response
    logger.info(f"(RES) -- {res_str}")
    logger.info(f"(END) <- (Done) {request.url.path} in {duration:.4f}s")

    # Step 5: Rebuild and return the response with the same body
    return Response(
        content=res,  # Keep original response body
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
    )

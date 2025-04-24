import json
import time

from fastapi import Request, Response

from app.app_dependency import get_env_service, get_logging_service


async def log_filter(
    request: Request,
    call_next,
):
    env = get_env_service()
    logger = get_logging_service()

    # Read the request body (can only be done once unless we reset it)
    body = await request.body()

    try:
        body_json: dict = {"uri": request.url.path } | json.loads(body.decode("utf-8"))
        body_str = json.dumps(body_json) if env.settings.ENVIRONMENT == "prd" else json.dumps(body_json, indent=4)
    except Exception:
        body_str = body.decode("utf-8")

    logger.info(f"(STA) -> ({request.method}) {request.url}")
    logger.info(f"(REQ) -- {body_str}")

    # Rebuild the request stream so the endpoint can still read it
    request._receive = lambda: {"type": "http.request", "body": body}

    # Continue with request
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    # Read response body
    res = b""
    async for chunk in response.body_iterator:
        res += chunk

    try:
        res_json = json.loads(res.decode("utf-8"))
        res_str = json.dumps(res_json) if env.settings.ENVIRONMENT == "prd" else json.dumps(res_json, indent=4)
    except Exception:
        res_str = res.decode("utf-8")

    # Log the response
    logger.info(f"(RES) -- {res_str}")
    logger.info(f"(END) <- {duration:.4f}s")

    # Rebuild and return the response with the same body
    return Response(
        content=res,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
    )

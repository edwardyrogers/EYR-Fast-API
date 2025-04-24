import json

from typing import Callable

from fastapi import Request, Response


async def model_middleware(request: Request, call_next: Callable):
    # Step 1: Read and parse the original request body
    try:
        original_body = await request.body()
        original_json = json.loads(original_body)
        new_data = original_json.get("payload", {})
        new_body = json.dumps(new_data).encode("utf-8")
    except (json.JSONDecodeError, KeyError, TypeError):
        return Response(
            content=b'{"error": "Invalid JSON payload"}',
            status_code=400,
            media_type="application/json",
        )

    # Step 2: Inject modified body back into request
    async def receive():
        return {"type": "http.request", "body": new_body, "more_body": False}

    request._receive = receive
    request._body = new_body  # In case someone calls request.body() again

    # Step 3: Get response from the next middleware or route
    response = await call_next(request)

    # Step 4: Read the response body and wrap it with original metadata
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk

    try:
        response_data = json.loads(response_body)
        wrapped_response = {
            "meta": original_json.get("meta", {}),
            "payload": response_data,
        }
        modified_content = json.dumps(wrapped_response).encode("utf-8")
    except json.JSONDecodeError:
        # If it's not JSON, just pass through the original response
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )

    # Step 5: Return final wrapped response with updated headers
    headers = dict(response.headers)
    headers.pop("content-length", None)  # Let FastAPI recalculate

    return Response(
        content=modified_content,
        status_code=response.status_code,
        headers=headers,
        media_type="application/json",
    )

import json
import inspect
from typing import Callable, Union, get_args, get_origin

from fastapi import Request, Response
from fastapi.routing import APIRoute
from pydantic import BaseModel


async def model_middleware(request: Request, call_next: Callable):
    # Step 1: Try to parse request body
    try:
        body_bytes = await request.body()
        original_json = json.loads(body_bytes.decode("utf-8"))
        payload = original_json.get("payload", {})
        meta = original_json.get("meta", {})
        new_body_bytes = json.dumps(payload).encode("utf-8")
    except (json.JSONDecodeError, KeyError, TypeError):
        return Response(
            content=json.dumps({"error": "Invalid JSON payload"}),
            status_code=400,
            media_type="application/json",
        )

    # Step 2: Override the request body
    async def receive():
        return {
            "type": "http.request",
            "body": new_body_bytes,
            "more_body": False,
        }

    request._receive = receive
    request._body = new_body_bytes

    # Step 3: Process the request through the route
    response = await call_next(request)
    headers = dict(response.headers)
    headers.pop("content-length", None)  # Let FastAPI recalculate it

    route = request.scope.get("route")
    
    if isinstance(route, APIRoute) and not is_valid_response_model(route.response_model, route.endpoint):
        error_response = {
            "meta": meta,
            "payload": {
                "code": "",
                "message": f"Route {request.url.path} uses an invalid response model: {route.response_model}",
                "stacktrace": None,
            },
        }
        return Response(
            content=json.dumps(error_response).encode("utf-8"),
            status_code=response.status_code,
            headers=headers,
            media_type="application/json",
        )

    # Step 4: Read and wrap the response body
    body_chunks = [chunk async for chunk in response.body_iterator]
    response_body = b"".join(body_chunks)

    try:
        response_data = json.loads(response_body.decode("utf-8"))
        wrapped_response = {
            "meta": meta,
            "payload": response_data,
        }
        return Response(
            content=json.dumps(wrapped_response).encode("utf-8"),
            status_code=response.status_code,
            headers=headers,
            media_type="application/json",
        )
    except json.JSONDecodeError:
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=headers,
            media_type=response.media_type,
        )


def is_valid_response_model(model, endpoint):
    if model is None:
        return False
    if inspect.isclass(model) and issubclass(model, BaseModel):
        return True
    elif get_origin(model) is Union:
        return all(
            inspect.isclass(arg) and issubclass(arg, BaseModel)
            for arg in get_args(model)
        )
    else:
        return False


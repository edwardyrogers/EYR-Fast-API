import inspect
import json
from typing import Callable, Dict

from fastapi import Request, Response
from fastapi.routing import APIRoute
from pydantic import BaseModel

from app.core.exceptions import ApiException


async def model_middleware(request: Request, call_next: Callable):
    # Step 1: Read and parse the original request body
    try:
        original_body: bytes = await request.body()  # `body()` returns bytes
        original_json: Dict = json.loads(
            original_body.decode("utf-8")
        )  # Parsed body as dict
        new_data: Dict = original_json.get("payload", {})  # Extract the 'payload' key
        new_body: bytes = json.dumps(new_data).encode(
            "utf-8"
        )  # Convert the 'payload' into a new body

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        # If the body is invalid, return a 400 error response with an error message
        return Response(
            content=b'{"error": "Invalid JSON payload"}',
            status_code=400,
            media_type="application/json",
        )

    # Step 2: Inject modified body back into request
    async def receive() -> Dict[str, any]:  # Define return type for receive function
        return {
            "type": "http.request",
            "body": new_body,
            "more_body": False,
        }

    request._receive = receive  # Inject the custom receive function
    request._body = new_body  # Set the new body in case it's read again

    # Step 3: Get response from the next middleware or route
    response = await call_next(request)

    headers: Dict[str, str] = dict(response.headers)
    headers.pop("content-length", None)  # Let FastAPI recalculate content-length
    
    route: APIRoute = request.scope.get("route")
     
    if isinstance(route, APIRoute):
        response_model = route.response_model
        if response_model is not None:
            # Check if response_model is NOT a subclass of BaseModel
            if not inspect.isclass(response_model) or not issubclass(response_model, BaseModel):
                wrapped_response: Dict[str, any] = (
                    {  # Create a wrapped response with 'meta' and 'payload'
                        "meta": original_json.get("meta", {}),
                        "payload": {
                            "code": "",
                            "message": f"Route {request.url.path} uses an invalid response model: {response_model}",
                            "stacktrace": None,            
                        },
                    }
                )
                modified_content: bytes = json.dumps(wrapped_response).encode(
                    "utf-8"
                )
                return Response(
                    content=modified_content,
                    status_code=response.status_code,
                    headers=headers,
                    media_type=response.media_type,
                )


    # Step 4: Read the response body and wrap it with original metadata
    response_body: bytes = b""
    async for chunk in response.body_iterator:
        response_body += chunk

    try:
        response_data: Dict = json.loads(
            response_body.decode("utf-8")
        )  # Parse response as JSON
        wrapped_response: Dict[str, any] = (
            {  # Create a wrapped response with 'meta' and 'payload'
                "meta": original_json.get("meta", {}),
                "payload": response_data,
            }
        )
        modified_content: bytes = json.dumps(wrapped_response).encode(
            "utf-8"
        )  # Re-encode as JSON
    except json.JSONDecodeError:
        # If the response is not JSON, pass through the original response body
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=headers,
            media_type=response.media_type,
        )

    return Response(
        content=modified_content,
        status_code=response.status_code,
        headers=headers,
        media_type="application/json",
    )

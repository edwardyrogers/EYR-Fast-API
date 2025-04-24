from fastapi import Request


async def model_filter(request: Request, call_next):
    # Read the request body (can only be done once unless we reset it)
    body = await request.body()

    # Optional: decode body to string
    body.decode("utf-8")

    # Rebuild the request stream so the endpoint can still read it
    request._receive = lambda: {"type": "http.request", "body": body}

    response = await call_next(request)

    return response

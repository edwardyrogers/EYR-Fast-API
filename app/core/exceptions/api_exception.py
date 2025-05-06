import traceback

from fastapi import Request
from fastapi.responses import JSONResponse


class ApiException(Exception):
    def __init__(self, name: str):
        self.name = name


async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=400,
        content={
            "code": "",
            "message": "",
            "stacktrace": traceback.format_exc().split('\n'),
        },
    )

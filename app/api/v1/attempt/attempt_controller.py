from fastapi import APIRouter

from app.api.v1.attempt.attempt_model import AttemptREQ, AttemptRES


router = APIRouter()

@router.post("/test", response_model=AttemptRES)
def register_user(request: AttemptREQ):
    return AttemptRES(
        name = request.name
    )

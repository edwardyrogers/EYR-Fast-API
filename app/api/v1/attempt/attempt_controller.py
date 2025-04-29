from fastapi import APIRouter, Depends

from app.api.v1.attempt.attempt_model import AttemptREQ, AttemptRES
from app.app_dependency import get_env_service
from app.common.services import EnvService

router = APIRouter()


@router.post("/test", response_model=AttemptRES)
def register_user(
    request: AttemptREQ,
    env_service: EnvService = Depends(get_env_service),
):
    return AttemptRES(
        name=env_service.settings.ENVIRONMENT,
    )

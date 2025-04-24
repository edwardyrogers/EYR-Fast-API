from functools import lru_cache

from app.common.services.env import EnvService
from app.common.services.logging import LoggingService


@lru_cache()
def get_env_service() -> EnvService:
    return EnvService()


@lru_cache()
def get_logging_service() -> LoggingService:
    settings = get_env_service().settings

    return LoggingService(
        name=settings.PROJECT_NAME,
        is_debug=settings.DEBUG,
    )

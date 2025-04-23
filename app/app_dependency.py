from functools import lru_cache
from app.common.services.env_service import EnvService
from app.common.services.logging_service import LoggingService


@lru_cache()
def get_logging_service() -> LoggingService:
    return LoggingService()

@lru_cache()
def get_env_service() -> EnvService:
    return EnvService()
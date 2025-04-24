from fastapi import FastAPI

from app.api.v1 import api_router
from app.app_dependency import get_logging_service
from app.common.filters import logger, modeller
from app.config.env_config import Settings


def create_app(settings: Settings) -> FastAPI:
    logging_service = get_logging_service()

    logging_service.info(f"ENVIRONMENT = {settings.ENVIRONMENT}")

    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
    )

    # Register middleware
    app.middleware("http")(modeller.model_filter)
    app.middleware("http")(logger.log_filter)

    # Register routers
    app.include_router(api_router.router, prefix="/api/v1")

    return app

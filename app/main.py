from fastapi import FastAPI
from app.config.settings import encironment
from app.api.v1 import api_router

app = FastAPI(title=encironment.PROJECT_NAME)

app.include_router(api_router.router, prefix="/api/v1")

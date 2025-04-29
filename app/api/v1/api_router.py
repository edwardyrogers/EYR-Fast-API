from fastapi import APIRouter

from app.api.v1.attempt import router as attempt_router

router = APIRouter()
router.include_router(attempt_router, prefix="/attempt")

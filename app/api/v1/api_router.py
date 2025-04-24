from fastapi import APIRouter

from app.api.v1.attempt import attempt_controller

router = APIRouter()
router.include_router(attempt_controller.router, prefix="/attempt")

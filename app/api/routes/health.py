from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "debug_mode": settings.DEBUG
    }
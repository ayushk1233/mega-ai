from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": f"{settings.APP_NAME} backend is running"
    }
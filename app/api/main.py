from fastapi import FastAPI

from app.api.v1.api import api_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Production-Grade Multi-Agent LLM Orchestration System",
    version=settings.APP_VERSION
)

app.include_router(api_router)
from fastapi import FastAPI

from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="Production-Grade Multi-Agent LLM Orchestration System",
    version=settings.APP_VERSION
)


@app.get("/")
async def root():
    return {
        "message": f"{settings.APP_NAME} backend is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "debug_mode": settings.DEBUG
    }
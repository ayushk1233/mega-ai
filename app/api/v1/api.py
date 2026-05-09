from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.query import router as query_router
from app.api.routes.context import router as context_router
from app.api.routes.orchestrator import router as orchestrator_router
from app.api.routes.metrics import (
    router as metrics_router
)

from app.api.routes.stream import (
    router as stream_router
)


api_router = APIRouter()

api_router.include_router(
    orchestrator_router,
    tags=["Orchestrator"]
)
api_router.include_router(stream_router)

api_router.include_router(metrics_router)

api_router.include_router(query_router, tags=["Root"])
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(context_router, tags=["Context"])
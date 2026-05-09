from fastapi import APIRouter

from app.orchestrator.engine import Orchestrator

router = APIRouter()


@router.post("/orchestrate")
async def orchestrate(query: str):

    orchestrator = Orchestrator()

    result = orchestrator.run(query)

    return result
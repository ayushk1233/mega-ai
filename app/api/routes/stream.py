import json
import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.orchestrator.engine import (
    Orchestrator
)

router = APIRouter()

orchestrator = Orchestrator()


async def event_generator(query: str):

    phases = [
        "decomposition",
        "retrieval",
        "synthesis",
        "critique"
    ]

    for phase in phases:

        status_event = json.dumps({
            "type": "status",
            "message": f"Running {phase} agent..."
        })
        yield f"data: {status_event}\n\n"

        await asyncio.sleep(1)

    context = orchestrator.run(query)

    final_event = json.dumps({
        "type": "final",
        "data": context.model_dump()
    })
    yield f"data: {final_event}\n\n"


@router.get("/stream")
async def stream(query: str):

    return StreamingResponse(
        event_generator(query),
        media_type="text/event-stream"
    )
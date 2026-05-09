import json
import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.orchestrator.engine import (
    Orchestrator
)
from app.orchestrator.event_stream import (
    event_queue
)

router = APIRouter()

orchestrator = Orchestrator()


async def event_generator(query: str):

    import threading

    result_container = {}

    def run_orchestrator():

        context = orchestrator.run(query)

        result_container["context"] = (
            context.model_dump()
        )

    thread = threading.Thread(
        target=run_orchestrator
    )

    thread.start()

    while thread.is_alive():

        while not event_queue.empty():

            event = event_queue.get()

            yield f"data: {json.dumps(event)}\n\n"

        await asyncio.sleep(0.1)

    final_event = json.dumps({
        "type": "final",
        "data": result_container["context"]
    })
    yield f"data: {final_event}\n\n"


@router.get("/stream")
async def stream(query: str):

    return StreamingResponse(
        event_generator(query),
        media_type="text/event-stream"
    )
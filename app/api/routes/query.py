import uuid
from app.observability.events import EventType
from app.observability.logger import log_event
from app.observability.schemas import LogEvent
from app.workers.tasks import process_query

from fastapi import APIRouter

from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter()


@router.get("/")
async def root():
    return {
        "message": "Mega AI backend is running"
    }


@router.post(
    "/query",
    response_model=QueryResponse
)
async def submit_query(payload: QueryRequest):
    job_id = str(uuid.uuid4())
    log_event(
        LogEvent(
            event_type=EventType.JOB_CREATED,
            message="New orchestration job created",
            job_id=job_id
        )
    )
    process_query.delay(job_id, payload.query)
    return QueryResponse(
        job_id=str(uuid.uuid4()),
        status="accepted",
        query=payload.query
    )

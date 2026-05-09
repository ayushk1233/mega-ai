import uuid

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
    return QueryResponse(
        job_id=str(uuid.uuid4()),
        status="accepted",
        query=payload.query
    )
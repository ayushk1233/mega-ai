from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="User query for the orchestration system"
    )


class QueryResponse(BaseModel):
    job_id: str
    status: str
    query: str
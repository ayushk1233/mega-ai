from typing import Dict, List
from uuid import uuid4

from pydantic import BaseModel, Field

from app.memory.enums import JobStatus
from app.memory.models import (
    AgentOutput,
    ProvenanceEntry,
    TokenUsage,
    ToolCallLog
)


class SharedContext(BaseModel):
    job_id: str = Field(default_factory=lambda: str(uuid4()))

    user_query: str

    status: JobStatus = JobStatus.PENDING

    agent_outputs: Dict[str, AgentOutput] = {}

    provenance: List[ProvenanceEntry] = []

    tool_logs: List[ToolCallLog] = []

    token_usage: Dict[str, TokenUsage] = {}

    session_id: str = "default_session"

    conversation_history: list = []
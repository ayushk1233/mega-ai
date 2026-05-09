from pydantic import BaseModel
from typing import List, Optional

from app.memory.enums import AgentType, ToolStatus


class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ProvenanceEntry(BaseModel):
    sentence: str
    source_agent: AgentType
    source_chunks: List[str] = []


class ToolCallLog(BaseModel):
    tool_name: str
    status: ToolStatus
    latency_ms: int
    retry_count: int = 0


class AgentOutput(BaseModel):
    agent: AgentType
    output: str
    confidence: Optional[float] = None
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.observability.events import EventType


class LogEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    event_type: EventType

    message: str

    job_id: Optional[str] = None

    latency_ms: Optional[int] = None
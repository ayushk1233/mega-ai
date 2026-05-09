from enum import Enum


class EventType(str, Enum):
    API_REQUEST = "api_request"
    AGENT_STARTED = "agent_started"
    AGENT_COMPLETED = "agent_completed"
    TOOL_CALLED = "tool_called"
    TOOL_FAILED = "tool_failed"
    JOB_CREATED = "job_created"
    JOB_COMPLETED = "job_completed"
    ERROR = "error"
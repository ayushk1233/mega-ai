import time

from app.memory.context import SharedContext
from app.memory.models import AgentOutput
from app.memory.enums import AgentType

from app.orchestrator.pipeline import PIPELINE_STEPS
from app.orchestrator.state_manager import (
    mark_completed,
    mark_running
)

from app.observability.events import EventType
from app.observability.logger import log_event
from app.observability.schemas import LogEvent
from app.agents.registry import AGENT_REGISTRY


class Orchestrator:

    def run(self, query: str) -> SharedContext:

        context = SharedContext(user_query=query)

        mark_running(context)

        log_event(
            LogEvent(
                event_type=EventType.AGENT_STARTED,
                message="Orchestration started",
                job_id=context.job_id
            )
        )

        for step in PIPELINE_STEPS:

            time.sleep(1)

            agent = AGENT_REGISTRY[step]

            context = agent.run(context)

            log_event(
                LogEvent(
                    event_type=EventType.AGENT_COMPLETED,
                    message=f"{step} completed",
                    job_id=context.job_id
                )
            )

        mark_completed(context)

        log_event(
            LogEvent(
                event_type=EventType.JOB_COMPLETED,
                message="Orchestration completed",
                job_id=context.job_id
            )
        )

        return context
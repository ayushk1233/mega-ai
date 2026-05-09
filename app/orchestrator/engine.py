import time

from app.memory.context import SharedContext

from app.orchestrator.pipeline import PIPELINE_STEPS
from app.orchestrator.state_manager import (
    mark_completed,
    mark_running
)

from app.observability.events import EventType
from app.observability.logger import log_event
from app.observability.schemas import LogEvent
from app.observability.telemetry import (
    TelemetryCollector
)

from app.agents.registry import AGENT_REGISTRY

from app.memory.memory_manager import (
    MemoryManager
)


class Orchestrator:

    def run(self, query: str) -> SharedContext:

        context = SharedContext(
            user_query=query
        )

        memory_manager = MemoryManager()

        telemetry = TelemetryCollector()

        context.conversation_history = (
            memory_manager.get_session_history(
                context.session_id
            )
        )

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

            start_time = time.time()

            context = agent.run(context)

            latency = time.time() - start_time

            token_estimate = len(
                str(
                    context.agent_outputs[
                        step
                    ].output
                ).split()
            )

            telemetry.track_agent(
                agent_name=step,
                latency=latency,
                token_estimate=token_estimate
            )

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

        final_response = context.agent_outputs[
            "synthesis"
        ].output

        memory_manager.append_conversation(
            session_id=context.session_id,
            user_query=context.user_query,
            response=final_response
        )

        telemetry.persist()

        return context
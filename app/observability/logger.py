import structlog

from app.observability.schemas import LogEvent

logger = structlog.get_logger()


def log_event(event: LogEvent):
    logger.info(
        event.event_type.value,
        timestamp=str(event.timestamp),
        message=event.message,
        job_id=event.job_id,
        latency_ms=event.latency_ms
    )
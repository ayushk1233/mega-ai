from app.memory.context import SharedContext
from app.memory.enums import JobStatus


def mark_running(context: SharedContext):
    context.status = JobStatus.RUNNING


def mark_completed(context: SharedContext):
    context.status = JobStatus.COMPLETED


def mark_failed(context: SharedContext):
    context.status = JobStatus.FAILED
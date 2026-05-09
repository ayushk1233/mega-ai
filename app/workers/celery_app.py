from celery import Celery

from app.config.settings import settings

celery_app = Celery(
    "mega_ai",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["app.workers.tasks"]
)
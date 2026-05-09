import time

from app.workers.celery_app import celery_app


@celery_app.task
def process_query(job_id: str, query: str):

    print(f"[WORKER] Processing job {job_id}")

    time.sleep(5)

    return {
        "job_id": job_id,
        "query": query,
        "status": "completed"
    }
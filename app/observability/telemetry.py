import time

from app.observability.metrics_store import (
    MetricsStore
)


store = MetricsStore()


class TelemetryCollector:

    def __init__(self):

        self.metrics = []

    def track_agent(
        self,
        agent_name: str,
        latency: float,
        token_estimate: int
    ):

        metric = {
            "agent": agent_name,
            "latency_seconds": round(latency, 2),
            "token_estimate": token_estimate
        }

        self.metrics.append(metric)

    def persist(self):

        existing = store.load_metrics()

        existing.extend(self.metrics)

        store.save_metrics(existing)
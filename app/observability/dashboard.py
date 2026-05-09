from app.observability.metrics_store import (
    MetricsStore
)


store = MetricsStore()


def get_metrics():

    return store.load_metrics()
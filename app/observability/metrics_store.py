import json
from pathlib import Path


METRICS_PATH = Path(
    "app/observability/metrics.json"
)


class MetricsStore:

    def __init__(self):

        if not METRICS_PATH.exists():

            with open(METRICS_PATH, "w") as file:
                json.dump([], file)

    def load_metrics(self):

        with open(METRICS_PATH, "r") as file:
            return json.load(file)

    def save_metrics(self, metrics):

        with open(METRICS_PATH, "w") as file:
            json.dump(metrics, file, indent=2)
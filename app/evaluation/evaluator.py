import time

from app.orchestrator.engine import Orchestrator

from app.evaluation.metrics import (
    keyword_match_score,
    groundedness_score
)


class Evaluator:

    def __init__(self):

        self.orchestrator = Orchestrator()

    def evaluate(self, benchmark):

        start_time = time.time()

        result = self.orchestrator.run(
            benchmark["query"]
        )

        latency = time.time() - start_time

        synthesis_output = result.agent_outputs[
            "synthesis"
        ].output

        keyword_score = keyword_match_score(
            synthesis_output,
            benchmark["expected_keywords"]
        )

        provenance_chunks = [
            provenance.evidence
            for provenance in result.provenance
        ]

        grounding_score = groundedness_score(
            synthesis_output,
            provenance_chunks
        )

        return {
            "query": benchmark["query"],
            "latency_seconds": round(latency, 2),
            "keyword_score": round(keyword_score, 2),
            "grounding_score": round(grounding_score, 2)
        }
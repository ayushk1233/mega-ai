from app.llm.client import (
    generate_text_response
)


DISTILL_PROMPT = """
You are an AI retrieval compressor.

Compress the following external evidence
into concise, high-signal intelligence.

Focus only on:
- key innovations
- factual developments
- technical advancements
- strategic insights

Remove:
- repetition
- filler
- advertisements
- irrelevant commentary

External Evidence:
{evidence}

Return concise distilled intelligence.
"""


class EvidenceDistiller:

    def distill(
        self,
        evidence: str
    ):

        prompt = DISTILL_PROMPT.format(
            evidence=evidence
        )

        response = generate_text_response(
            prompt
        )

        return response
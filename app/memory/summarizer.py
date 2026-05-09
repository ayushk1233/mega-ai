from app.llm.client import (
    generate_text_response
)


SUMMARY_PROMPT = """
Summarize the following conversation
into a short contextual memory.

Conversation:
{conversation}

Return concise memory summary.
"""


class MemorySummarizer:

    def summarize(
        self,
        conversation: list
    ):

        prompt = SUMMARY_PROMPT.format(
            conversation=conversation
        )

        response = generate_text_response(prompt)

        return response
from app.agents.base import BaseAgent

from app.llm.client import generate_response
from app.llm.prompts import CRITIQUE_PROMPT

from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput
from app.llm.schemas import (
    CritiqueSchema
)

class CritiqueAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        retrieval_output = context.agent_outputs[
            "retrieval"
        ].output

        synthesis_output = context.agent_outputs[
            "synthesis"
        ].output

        prompt = CRITIQUE_PROMPT.format(
            evidence=retrieval_output,
            answer=synthesis_output
        )

        critique = generate_response(prompt)
        validated = CritiqueSchema(
            **critique
        )

        context.agent_outputs["critique"] = AgentOutput(
            agent=AgentType.CRITIQUE,
            output=validated.model_dump(),
            confidence=0.90
        )

        return context
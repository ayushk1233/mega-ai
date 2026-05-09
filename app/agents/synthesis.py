from app.agents.base import BaseAgent

from app.llm.client import generate_response
from app.llm.prompts import SYNTHESIS_PROMPT

from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput


class SynthesisAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        retrieval_output = context.agent_outputs[
            "retrieval"
        ].output

        prompt = SYNTHESIS_PROMPT.format(
            evidence=retrieval_output
        )

        response = generate_response(prompt)

        context.agent_outputs["synthesis"] = AgentOutput(
            agent=AgentType.SYNTHESIS,
            output=response,
            confidence=0.94
        )

        return context
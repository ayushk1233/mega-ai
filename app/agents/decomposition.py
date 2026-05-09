from app.agents.base import BaseAgent
from app.llm.client import generate_response
from app.llm.prompts import DECOMPOSITION_PROMPT

from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput


class DecompositionAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        prompt = DECOMPOSITION_PROMPT.format(
            query=context.user_query
        )

        response = generate_response(prompt)

        context.agent_outputs["decomposition"] = AgentOutput(
            agent=AgentType.DECOMPOSITION,
            output=response,
            confidence=0.92
        )

        return context
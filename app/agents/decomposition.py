from app.agents.base import BaseAgent
from app.llm.client import generate_response
from app.llm.prompts import DECOMPOSITION_PROMPT

from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput
from app.llm.schemas import (
    DecompositionSchema
)


class DecompositionAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        prompt = DECOMPOSITION_PROMPT.format(
            history=context.conversation_history,
            query=context.user_query
        )

        response = generate_response(prompt)
        validated = DecompositionSchema(
            **response
        )

        context.agent_outputs["decomposition"] = AgentOutput(
            agent=AgentType.DECOMPOSITION,
            output=validated.model_dump(),
            confidence=0.92
        )

        return context
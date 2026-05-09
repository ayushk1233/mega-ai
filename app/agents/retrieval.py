from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput


class RetrievalAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        retrieval_result = """
Tesla focuses on high-energy-density battery systems and vertical integration.

BYD focuses on Blade Battery safety architecture and manufacturing scale.
"""

        context.agent_outputs["retrieval"] = AgentOutput(
            agent=AgentType.RETRIEVAL,
            output=retrieval_result,
            confidence=0.88
        )

        return context
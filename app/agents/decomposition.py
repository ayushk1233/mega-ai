from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput


class DecompositionAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        query = context.user_query

        tasks = [
            f"Analyze core topic of: {query}",
            "Identify comparison dimensions",
            "Prepare retrieval objectives"
        ]

        context.agent_outputs["decomposition"] = AgentOutput(
            agent=AgentType.DECOMPOSITION,
            output="\n".join(tasks),
            confidence=0.91
        )

        return context
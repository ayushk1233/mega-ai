from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput

from app.rag.retriever import Retriever

retriever = Retriever()


class RetrievalAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        results = retriever.retrieve(
            context.user_query
        )

        retrieval_result = "\n".join(results)

        context.agent_outputs["retrieval"] = AgentOutput(
            agent=AgentType.RETRIEVAL,
            output=retrieval_result,
            confidence=0.89
        )

        return context
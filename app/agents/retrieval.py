from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput
from app.memory.models import ProvenanceEntry

from app.rag.retriever import Retriever

retriever = Retriever()


class RetrievalAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        results = retriever.retrieve(
            context.user_query
        )

        for chunk in results:
            context.provenance.append(
                ProvenanceEntry(
                    sentence=chunk["text"],
                    source_agent=AgentType.RETRIEVAL,
                    source_chunk_ids=[
                        chunk["chunk_id"]
                    ],
                    evidence=chunk["text"]
                )
            )

        retrieval_result = "\n".join(
            chunk["text"] for chunk in results
        )

        context.agent_outputs["retrieval"] = AgentOutput(
            agent=AgentType.RETRIEVAL,
            output=retrieval_result,
            confidence=0.88
        )

        return context
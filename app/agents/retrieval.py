from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput
from app.memory.models import ProvenanceEntry

from app.rag.retriever import Retriever
from app.tools.executor import (
    ToolExecutor
)
from app.rag.reranker import (
    Reranker
)
from app.tools.router import (
    ToolRouter
)

retriever = Retriever()
tool_executor = ToolExecutor()
reranker = Reranker()
tool_router = ToolRouter()

class RetrievalAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        results = retriever.retrieve(
            context.user_query
        )

        results = reranker.rerank(
            context.user_query,
            results
        )

        results = results[:3]


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

        

        web_context = ""

        should_search = (
            tool_router.should_use_web_search(
                context.user_query
            )
        )

        if should_search:

            web_results = tool_executor.execute(
                "web_search",
                context.user_query
            )

            web_context = "\n".join(
                [
                    result["body"]
                    for result in web_results
                ]
            )

        retrieval_result = "\n".join(
            [
                chunk["text"]
                 for chunk in results
            ]
        )

        if web_context:

            retrieval_result += (
                "\n\nExternal Intelligence:\n"
                + web_context
            )

        context.agent_outputs["retrieval"] = AgentOutput(
            agent=AgentType.RETRIEVAL,
            output=retrieval_result,
            confidence=0.88
        )

        return context
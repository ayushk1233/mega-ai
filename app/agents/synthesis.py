from app.agents.base import BaseAgent
from app.memory.context import SharedContext
from app.memory.enums import AgentType
from app.memory.models import AgentOutput


class SynthesisAgent(BaseAgent):

    def run(self, context: SharedContext) -> SharedContext:

        retrieval_output = context.agent_outputs[
            "retrieval"
        ].output

        final_answer = f"""
Final Analysis:

{retrieval_output}

Tesla prioritizes performance and vertical integration.

BYD prioritizes manufacturing scale and battery safety.
"""

        context.agent_outputs["synthesis"] = AgentOutput(
            agent=AgentType.SYNTHESIS,
            output=final_answer,
            confidence=0.93
        )

        return context
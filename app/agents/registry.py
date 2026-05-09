from app.agents.decomposition import DecompositionAgent
from app.agents.retrieval import RetrievalAgent
from app.agents.synthesis import SynthesisAgent


AGENT_REGISTRY = {
    "decomposition": DecompositionAgent(),
    "retrieval": RetrievalAgent(),
    "synthesis": SynthesisAgent()
}
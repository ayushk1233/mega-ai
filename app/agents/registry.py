from app.agents.decomposition import DecompositionAgent
from app.agents.retrieval import RetrievalAgent
from app.agents.synthesis import SynthesisAgent
from app.agents.critique import CritiqueAgent


AGENT_REGISTRY = {
    "decomposition": DecompositionAgent(),
    "retrieval": RetrievalAgent(),
    "synthesis": SynthesisAgent(),
    "critique": CritiqueAgent()
}
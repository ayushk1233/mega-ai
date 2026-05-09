from pydantic import BaseModel

from typing import List


class DecompositionSchema(BaseModel):

    analysis_objectives: List[str]

    retrieval_goals: List[str]

    comparison_dimensions: List[str]


class SynthesisSchema(BaseModel):

    final_answer: str

    key_insights: List[str]

    comparison_summary: str


class CritiqueSchema(BaseModel):

    grounding_assessment: str

    hallucination_risks: str

    confidence_analysis: str

    suggested_improvements: List[str]
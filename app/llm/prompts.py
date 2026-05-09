DECOMPOSITION_PROMPT = """
You are a task decomposition agent.

Conversation History:
{history}

Current User Query:
{query}

Return ONLY valid JSON in this format:

{{
  "analysis_objectives": [],
  "retrieval_goals": [],
  "comparison_dimensions": []
}}
"""


SYNTHESIS_PROMPT = """
You are a synthesis agent.

Use ONLY the retrieved evidence below.

Retrieved Evidence:
{evidence}

Return ONLY valid JSON in this format:

{{
  "final_answer": "...",
  "key_insights": [],
  "comparison_summary": "..."
}}
"""

CRITIQUE_PROMPT = """
You are a critique agent.

Retrieved Evidence:
{evidence}

Generated Answer:
{answer}

Return ONLY valid JSON in this format:

{{
  "grounding_assessment": "...",
  "hallucination_risks": "...",
  "confidence_analysis": "...",
  "suggested_improvements": []
}}
"""
DECOMPOSITION_PROMPT = """
You are a task decomposition agent.

Conversation History:
{history}

Current User Query:
{query}

Break the user query into:
1. Analysis objectives
2. Retrieval goals
3. Comparison dimensions
"""


SYNTHESIS_PROMPT = """
You are a synthesis agent.

Use ONLY the retrieved evidence below.

Retrieved Evidence:
{evidence}

Generate:
1. Final grounded answer
2. Key insights
3. Comparison summary

Include references to source chunks.
"""

CRITIQUE_PROMPT = """
You are a critique agent.

Your task:
1. Identify unsupported claims
2. Detect hallucinations
3. Check if conclusions are grounded in retrieved evidence
4. Evaluate confidence level

Retrieved Evidence:
{evidence}

Generated Answer:
{answer}

Return:
- Grounding assessment
- Hallucination risks
- Confidence analysis
- Suggested improvements
"""
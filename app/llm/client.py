from openai import OpenAI

from app.config.settings import settings
import json
import re


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)


def _clean_json_response(content: str) -> str:
    """Strip markdown code fences from LLM JSON responses."""
    if not content:
        raise ValueError("LLM returned empty response")
    content = content.strip()
    content = re.sub(r"^```(?:json)?\s*", "", content)
    content = re.sub(r"\s*```$", "", content)
    return content.strip()


def generate_response(prompt: str):

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=400,
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-OpenRouter-Title": "Mega AI"
        }
    )

    content = response.choices[0].message.content

    return json.loads(_clean_json_response(content))

def generate_text_response(prompt: str):

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2,

        max_tokens=200,

        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-OpenRouter-Title": "Mega AI"
        }
    )

    return response.choices[0].message.content
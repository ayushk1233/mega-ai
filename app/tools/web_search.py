from tavily import TavilyClient

from app.tools.base import BaseTool
from app.config.settings import settings


client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


class WebSearchTool(BaseTool):

    name = "web_search"

    def run(self, query: str):

        try:

            response = client.search(
                query=query,
                search_depth="advanced",
                max_results=5
            )

            results = []

            for item in response["results"]:

                results.append(
                    {
                        "title": item.get(
                            "title",
                            ""
                        ),
                        "body": item.get(
                            "content",
                            ""
                        ),
                        "link": item.get(
                            "url",
                            ""
                        )
                    }
                )

            return results

        except Exception:

            return []
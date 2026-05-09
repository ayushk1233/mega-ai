from duckduckgo_search import DDGS

from app.tools.base import BaseTool


class WebSearchTool(BaseTool):

    name = "web_search"

    def run(self, query: str):

        results = []

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=3
            )

            for result in search_results:

                results.append(
                    {
                        "title": result["title"],
                        "body": result["body"],
                        "link": result["href"]
                    }
                )

        return results
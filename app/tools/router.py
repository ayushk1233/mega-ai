class ToolRouter:

    def should_use_web_search(
        self,
        query: str
    ) -> bool:

        query = query.lower()

        web_keywords = [
            "latest",
            "news",
            "today",
            "recent",
            "current",
            "innovation",
            "update",
            "trend"
        ]

        for keyword in web_keywords:

            if keyword in query:

                return True

        return False
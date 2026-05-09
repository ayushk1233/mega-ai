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

    def prioritize_external_sources(
        self,
        query: str
    ) -> bool:

        query = query.lower()

        freshness_keywords = [
            "latest",
            "recent",
            "today",
            "current",
            "new",
            "innovation",
            "update",
            "trend",
            "2025",
            "2026"
        ]

        for keyword in freshness_keywords:

            if keyword in query:

                return True

        return False
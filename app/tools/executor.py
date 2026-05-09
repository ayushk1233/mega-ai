from app.tools.registry import (
    TOOL_REGISTRY
)


class ToolExecutor:

    def execute(
        self,
        tool_name: str,
        query: str
    ):

        tool = TOOL_REGISTRY[tool_name]

        return tool.run(query)
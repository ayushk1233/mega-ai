from abc import ABC, abstractmethod

from app.memory.context import SharedContext


class BaseAgent(ABC):

    @abstractmethod
    def run(self, context: SharedContext) -> SharedContext:
        pass
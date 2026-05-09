from app.memory.conversation_store import (
    ConversationStore
)


store = ConversationStore()


class MemoryManager:

    def get_session_history(
        self,
        session_id: str
    ):

        memory = store.load_memory()

        history = memory.get(session_id, [])

        return history[-2:]

    def append_conversation(
        self,
        session_id: str,
        user_query: str,
        response: str
    ):

        memory = store.load_memory()

        if session_id not in memory:
            memory[session_id] = []

        memory[session_id].append(
            {
                "query": user_query,
                "response": response
            }
        )

        store.save_memory(memory)
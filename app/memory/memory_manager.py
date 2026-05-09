from app.memory.conversation_store import (
    ConversationStore
)

from app.memory.summarizer import (
    MemorySummarizer
)


store = ConversationStore() 

summarizer = MemorySummarizer()


class MemoryManager:

    def get_session_history(
        self,
        session_id: str
    ):

        memory = store.load_memory()

        history = memory.get(session_id, [])

        compressed_history = []

        for item in history[-3:]:

            compressed_history.append(
                item.get("summary", "")
            )

        return compressed_history

    def append_conversation(
        self,
        session_id: str,
        user_query: str,
        response: str
    ):

        memory = store.load_memory()

        if session_id not in memory:
            memory[session_id] = []

        conversation_entry = {"query": user_query, "response": response}

        summary = summarizer.summarize(
            [conversation_entry]
        )

        memory[session_id].append(
            {
                "summary": summary
            }
        )

        store.save_memory(memory)
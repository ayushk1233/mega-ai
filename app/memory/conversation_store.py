import json
from pathlib import Path


MEMORY_PATH = Path(
    "app/memory/conversations.json"
)


class ConversationStore:

    def __init__(self):

        if not MEMORY_PATH.exists():

            with open(MEMORY_PATH, "w") as file:
                json.dump({}, file)

    def load_memory(self):

        with open(MEMORY_PATH, "r") as file:
            return json.load(file)

    def save_memory(self, data):

        with open(MEMORY_PATH, "w") as file:
            json.dump(data, file, indent=2)
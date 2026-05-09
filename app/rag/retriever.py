from pathlib import Path

from app.rag.chunker import chunk_text
from app.rag.embedder import embed_text
from app.rag.vector_store import VectorStore



DOCUMENT_PATH = Path(
    "app/rag/documents/battery_report.txt"
)


class Retriever:

    def __init__(self):

        with open(DOCUMENT_PATH, "r") as file:
            text = file.read()

        self.chunks = chunk_text(text)

        embeddings = embed_text(
            [chunk["text"] for chunk in self.chunks]
        )

        dimension = len(embeddings[0])

        self.vector_store = VectorStore(dimension)

        self.vector_store.add_embeddings(
            embeddings,
            self.chunks
        )

    def retrieve(self, query: str):

        query_embedding = embed_text([query])[0]

        return self.vector_store.search(
            query_embedding
        )
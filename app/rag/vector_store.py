import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatL2(dimension)

        self.text_chunks = []

    def add_embeddings(self, embeddings, chunks):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        self.index.add(embeddings)

        self.text_chunks.extend(chunks)

    def search(self, embedding, top_k=2):

        embedding = np.array(
            [embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(
                self.text_chunks[idx]
            )

        return results
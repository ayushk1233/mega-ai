import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatL2(dimension)

        self.chunks = []

    def add_embeddings(self, embeddings, chunks):

        embeddings = np.array(
            embeddings
        ).astype("float32")

        self.index.add(embeddings)

        self.chunks.extend(chunks)

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
                self.chunks[idx]
            )

        return results
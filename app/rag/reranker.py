from sklearn.metrics.pairwise import (
    cosine_similarity
)

from app.rag.embedder import embed_text


class Reranker:

    def rerank(
        self,
        query: str,
        chunks: list
    ):

        query_embedding = embed_text(
            [query]
        )

        chunk_texts = [
            chunk["text"]
            for chunk in chunks
        ]

        chunk_embeddings = embed_text(
            chunk_texts
        )

        similarities = cosine_similarity(
            query_embedding,
            chunk_embeddings
        )[0]

        ranked = sorted(
            zip(chunks, similarities),
            key=lambda x: x[1],
            reverse=True
        )

        reranked_chunks = [
            item[0]
            for item in ranked
        ]

        return reranked_chunks
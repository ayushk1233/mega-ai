from typing import List


def chunk_text(
    text: str,
    chunk_size: int = 3,
    overlap: int = 1
):

    sentences = text.split(".")

    cleaned = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    chunks = []

    step = chunk_size - overlap

    chunk_id = 1

    for i in range(
        0,
        len(cleaned),
        step
    ):

        sentence_group = cleaned[
            i:i + chunk_size
        ]

        if sentence_group:

            chunk = {
                "chunk_id": f"chunk_{chunk_id}",
                "text": ". ".join(sentence_group)
            }

            chunks.append(chunk)

            chunk_id += 1

    return chunks
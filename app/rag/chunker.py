def chunk_text(text: str, chunk_size: int = 120):

    chunks = []

    chunk_id = 1

    for i in range(0, len(text), chunk_size):

        chunk = {
            "chunk_id": f"chunk_{chunk_id}",
            "text": text[i:i + chunk_size]
        }

        chunks.append(chunk)

        chunk_id += 1

    return chunks
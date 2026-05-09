def keyword_match_score(
    output: str,
    expected_keywords: list
):

    output = output.lower()

    matches = 0

    for keyword in expected_keywords:

        if keyword.lower() in output:
            matches += 1

    return matches / len(expected_keywords)


def groundedness_score(
    synthesis: str,
    provenance_chunks: list
):

    synthesis = synthesis.lower()

    matches = 0

    for chunk in provenance_chunks:

        if chunk.lower() in synthesis:
            matches += 1

    if len(provenance_chunks) == 0:
        return 0

    return matches / len(provenance_chunks)
import numpy as np

def hybrid_rank(
    semantic_scores,
    semantic_indices,
    tfidf_scores,
    tfidf_indices,
    alpha=0.6,
    beta=0.4
):

    combined_scores = {}

    for score, idx in zip(semantic_scores, semantic_indices):
        semantic_similarity = 1 / (1 + score)

        if idx not in combined_scores:
            combined_scores[idx] = 0

        combined_scores[idx] += alpha * semantic_similarity

    for idx in tfidf_indices:
        if idx not in combined_scores:
            combined_scores[idx] = 0

        combined_scores[idx] += beta * tfidf_scores[idx]

    ranked = sorted(
        combined_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked
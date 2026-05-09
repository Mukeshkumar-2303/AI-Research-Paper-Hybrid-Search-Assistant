from app.services.embeddings import generate_embeddings
from app.services.vector_store import FAISSVectorStore
from app.services.tfidf_store import TFIDFStore
from app.services.hybrid_search import hybrid_rank


class RetrievalAgent:

    def __init__(self, chunks):

        self.chunks = chunks

        # Generate embeddings once
        embeddings = generate_embeddings(chunks)

        self.vector_store = FAISSVectorStore(
            dimension=len(embeddings[0])
        )

        self.vector_store.add_embeddings(embeddings)

        self.tfidf_store = TFIDFStore()
        self.tfidf_store.fit(chunks)

    def retrieve(self, query, top_k=8):

        
        # 1. Query embedding
      
        query_embedding = generate_embeddings([query])[0]

        
        # 2. Semantic search (FAISS)
      
        semantic_scores, semantic_indices = self.vector_store.search(
            query_embedding,
            k=top_k
        )

        
        # 3. TF-IDF search
       
        tfidf_scores, tfidf_indices = self.tfidf_store.search(
            query,
            k=top_k
        )

        
        # 4. Hybrid ranking
      
        ranked = hybrid_rank(
            semantic_scores,
            semantic_indices,
            tfidf_scores,
            tfidf_indices
        )

        
        # 5. Build results FIRST
        
        results = []

        for idx, score in ranked[:top_k]:
            chunk_text = self.chunks[idx]

            # Filter noise chunks
            if len(chunk_text) < 80:
                continue

            results.append({
                "chunk": chunk_text,
                "score": float(score)
            })

        
        # 6. Final safety fallback
        
        if not results:
            return [{
                "chunk": "No relevant context found in document.",
                "score": 0.0
            }]

        return results
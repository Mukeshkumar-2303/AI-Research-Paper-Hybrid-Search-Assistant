from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFStore:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.matrix = None

    def fit(self, chunks):
        self.matrix = self.vectorizer.fit_transform(chunks)

    def search(self, query, k=5):
        query_vec = self.vectorizer.transform([query])

        similarities = cosine_similarity(query_vec, self.matrix).flatten()

        top_indices = similarities.argsort()[-k:][::-1]

        return similarities, top_indices
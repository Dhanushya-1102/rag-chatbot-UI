import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGChatbot:
    def __init__(self, file_path):

        # ✔ LOAD DATA (FIX 1 location)
        with open(file_path, "r", encoding="utf-8") as f:
            self.documents = [line.strip() for line in f.readlines() if line.strip()]

        # ✔ VECTORIZE DATA (FIX 2 location)
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(self.documents)

    # ✔ MAIN SEARCH FUNCTION (FIX 3 + FIX 4 here)
    def get_answer(self, query):

        query_vec = self.vectorizer.transform([query])

        scores = cosine_similarity(query_vec, self.doc_vectors)[0]

        best_idx = scores.argmax()
        best_score = scores[best_idx]

        # 🔥 FIX: confidence check (prevents wrong answers)
        if best_score < 0.2:
            return "I don't know the answer."

        return self.documents[best_idx]
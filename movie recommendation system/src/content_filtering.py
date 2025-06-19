import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:
    def __init__(self):
        # Setup path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        movie_path = os.path.join(base_dir, '..', 'data', 'ml-latest-small', 'movies.csv')
        tags_path = os.path.join(base_dir, '..', 'data', 'ml-latest-small', 'tags.csv')

        # Load data
        self.movies = pd.read_csv(movie_path)
        tags = pd.read_csv(tags_path)

        # Merge tag info
        tags_grouped = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
        self.movies = pd.merge(self.movies, tags_grouped, on='movieId', how='left')

        # Create combined text
        self.movies['combined'] = (
            self.movies['title'].fillna('') + ' ' +
            self.movies['genres'].fillna('') + ' ' +
            self.movies['tag'].fillna('')
        )

        # TF-IDF vectorization
        self.tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.tfidf.fit_transform(self.movies['combined'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    def recommend(self, movie_title, top_n=5):
        idx = self.movies[self.movies['title'].str.lower() == movie_title.lower()].index
        if len(idx) == 0:
            return f"❌ Movie '{movie_title}' not found."

        idx = idx[0]
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        top_indices = [i[0] for i in sim_scores[1:top_n + 1]]

        return self.movies['title'].iloc[top_indices].tolist()

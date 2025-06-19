from src.content_filtering import ContentBasedRecommender
from src.collaborative_filtering import CollaborativeRecommender
import pandas as pd
import os

class HybridRecommender:
    def __init__(self):
        self.content_model = ContentBasedRecommender()
        self.collab_model = CollaborativeRecommender()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        movies_path = os.path.join(base_dir, '..', 'data', 'ml-latest-small', 'movies.csv')
        self.movies_df = pd.read_csv(movies_path)

    def has_user_rated(self, user_id):
        """
        Check if the given user ID has rated any movie.
        Used to detect cold-start users.
        """
        return int(user_id) in self.collab_model.ratings_df['userId'].unique()

    def recommend(self, user_id, movie_title, top_n=5, weight_content=0.3, weight_collab=0.7):
        # Content-based candidates
        content_titles = self.content_model.recommend(movie_title, top_n=50)
        if isinstance(content_titles, str):
            return content_titles  # movie not found

        # Collaborative scores for this user
        collab_scores = {}
        collab_ids = self.collab_model.recommend_for_user(user_id, n=100)

        for movie_id in collab_ids:
            title = self.movies_df[self.movies_df['movieId'] == movie_id]['title'].values
            if len(title) > 0:
                collab_scores[title[0]] = 1  # basic weight (will be mixed with content score)

        # Score all content-based titles
        final_scores = {}

        for rank, title in enumerate(content_titles):
            content_score = (len(content_titles) - rank) / len(content_titles)  # normalize from 1 to 0
            collab_score = collab_scores.get(title, 0)
            final_score = (weight_content * content_score) + (weight_collab * collab_score)
            final_scores[title] = final_score

        # Sort and return top N
        sorted_titles = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
        return [title for title, _ in sorted_titles[:top_n]]

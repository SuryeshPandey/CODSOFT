import os
import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

class CollaborativeRecommender:
    """
    Collaborative Filtering Recommender using SVD (Matrix Factorization)
    """

    def __init__(self):
        # Path to ratings.csv
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ratings_path = os.path.join(base_dir, '..', 'data', 'ml-latest-small', 'ratings.csv')

        # Load data
        self.ratings_df = pd.read_csv(ratings_path)

        # Surprise Reader & Dataset
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(self.ratings_df[['userId', 'movieId', 'rating']], reader)

        # Train-test split
        trainset, _ = train_test_split(data, test_size=0.2, random_state=42)

        # SVD Collaborative Filtering
        self.model = SVD()
        self.model.fit(trainset)

    def recommend_for_user(self, user_id, n=10):
        """
        Recommends top N movies for a given user using collaborative filtering.
        """
        try:
            user_id = int(user_id)
            all_movie_ids = self.ratings_df['movieId'].unique()
            rated_movies = self.ratings_df[self.ratings_df['userId'] == user_id]['movieId'].values
            unrated_movies = [mid for mid in all_movie_ids if mid not in rated_movies]

            predictions = [self.model.predict(user_id, mid) for mid in unrated_movies]
            predictions.sort(key=lambda x: x.est, reverse=True)

            top_movie_ids = [int(pred.iid) for pred in predictions[:n]]
            return top_movie_ids
        except Exception as e:
            print(f"⚠️ Error generating recommendations for user {user_id}: {e}")
            return []

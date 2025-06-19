import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Ensure project root is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.hybrid_recommender import HybridRecommender
from src.database import init_db, save_to_db
from src.utils import get_poster_and_description  # updated function

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# Initialize recommender and database
recommender = HybridRecommender()
init_db()

# UI
st.title("🎬 Movie Recommendation System")
st.markdown("Hybrid model using both **content-based** and **collaborative filtering**.")

# Load movie list
movie_list = recommender.movies_df['title'].sort_values().tolist()

# Sidebar Inputs
st.sidebar.header("🔧 Settings")
user_id = st.sidebar.number_input("User ID", min_value=1, max_value=100, value=1, step=1)
weight_collab = st.sidebar.slider("Collaborative Filtering Weight", 0.0, 1.0, 0.7, step=0.05)
weight_content = 1.0 - weight_collab
top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# Main Input
selected_movie = st.selectbox("Choose a Movie:", movie_list)

# Button
if st.button("Recommend"):
    # Cold Start Check
    if not recommender.has_user_rated(user_id):
        st.warning("⚠️ Cold Start: No rating history found for this user. Showing popular movies instead.")
        
        ratings_df = pd.read_csv("data/ml-latest-small/ratings.csv")
        movies_df = pd.read_csv("data/ml-latest-small/movies.csv")
        popular_movies = (
            ratings_df['movieId'].value_counts()
            .head(top_n)
            .rename_axis('movieId')
            .reset_index(name='num_ratings')
        )
        results = pd.merge(popular_movies, movies_df, on='movieId')['title'].tolist()
    else:
        results = recommender.recommend(
            user_id=user_id,
            movie_title=selected_movie,
            top_n=top_n,
            weight_content=weight_content,
            weight_collab=weight_collab
        )

    if isinstance(results, str):
        st.error(results)
    else:
        st.subheader("🎯 Recommended Movies:")

        for i in range(0, len(results), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(results):
                    with cols[j]:
                        title = results[i + j]
                        st.markdown(f"**{i + j + 1}. {title}**")
                        poster_url, overview = get_poster_and_description(title)

                        if poster_url:
                            st.image(poster_url, width=200)
                        else:
                            st.caption("📎 Poster not available")

                        if overview:
                            st.caption(f"📝 {overview[:200]}...")
                        else:
                            st.caption("No description available")

        # Save to SQLite
        save_to_db(user_id, selected_movie, results)

        # Download CSV
        df_recs = pd.DataFrame(results, columns=["Recommended Movie"])
        csv = df_recs.to_csv(index=False)
        st.download_button(
            label="📥 Download Recommendations as CSV",
            data=csv,
            file_name=f"recommendations_user_{user_id}.csv",
            mime='text/csv'
        )

        # Visualize Top 10 Most Rated Movies
        st.subheader("📊 Top 10 Most Rated Movies in the Dataset")
        ratings_df = pd.read_csv("data/ml-latest-small/ratings.csv")
        movies_df = pd.read_csv("data/ml-latest-small/movies.csv")
        rating_counts = ratings_df['movieId'].value_counts().rename_axis('movieId').reset_index(name='num_ratings')
        top_movies = pd.merge(rating_counts, movies_df, on='movieId')
        top_10 = top_movies.head(10)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.barh(top_10['title'][::-1], top_10['num_ratings'][::-1], color='skyblue')
        ax.set_xlabel("Number of Ratings")
        ax.set_title("Top 10 Most Rated Movies")
        st.pyplot(fig)

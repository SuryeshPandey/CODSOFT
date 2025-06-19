# 🎬 Hybrid Movie Recommendation System

A smart, scalable, and visually-rich movie recommender system built using a **hybrid approach** — combining the strengths of **collaborative filtering** and **content-based filtering**, with fallback handling for cold-start users and real-time user control.

---

## 🔧 Built With

- **Python 3.11**
- **Streamlit** (frontend)
- **Pandas, NumPy** (data manipulation)
- **scikit-learn** & **Surprise** (ML models - SVD for collaborative filtering)
- **TMDb API** (movie posters & descriptions)
- **Matplotlib** (data visualization)
- **SQLite** (user history database)

---

## 🎯 Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| ✅ **Hybrid Recommendations** | Combines collaborative + content-based filtering using adjustable weights |
| 🔀 **Cold Start Fallback**     | New users without ratings are handled using only content-based filtering   |
| 🖼️ **Posters & Overviews**     | Dynamically fetched via TMDb API for each recommended movie                |
| 🎛️ **Interactive Controls**   | Users can adjust weights and number of results in real time                |
| 🧠 **SVD for Collaborative**   | Uses latent features via Surprise’s SVD for behavioral matching            |
| 📊 **Top Rated Chart**         | Bar chart of the most rated movies from the dataset                        |
| 💾 **Downloadable Results**    | Recommendations can be downloaded as a CSV                                 |
| 🗃️ **SQLite History Logging**  | Saves past recommendations per user                                        |
| 📐 **Responsive Layout**       | Clean design showing 2 movie cards per row                                 |
| ⚠️ **Robust Error Handling**   | Covers missing posters, invalid inputs, and edge cases                     |

---

## 🧠 How It Works

1. **User selects a movie** + **user ID**.
2. The system checks if the user has prior rating history:
   - ✅ Yes → Use SVD collaborative filtering for recommendations.
   - ❌ No → Use only content-based filtering (Cold Start).
3. Final results are ranked by a **hybrid score** =  
   `weight_content * content_score + weight_collab * collab_score`
4. Posters & overviews are fetched using TMDb API.
5. Results displayed with option to download or store in database.

---

## 📊 Sample Visualization

- Bar chart showing **Top 10 Most Rated Movies**
- Arranged in descending order of total number of user ratings

---

## 📁 Project Structure

```
recommendation_system_codsoft/
├── app/
│ └── app.py # Streamlit app
├── data/
│ └── ml-latest-small/ # MovieLens dataset (ratings.csv, movies.csv)
├── src/
│ ├── content_filtering.py # Content-based recommender
│ ├── collaborative_filtering.py # SVD model
│ ├── hybrid_recommender.py # Combines both models + cold start
│ ├── utils.py # API calls to TMDb
│ └── database.py # SQLite DB logic
├── .venv/ # Virtual environment
└── requirements.txt
```

---

## 🚀 Setup & Run

```bash
# Clone the repo
git clone https://github.com/your-username/recommendation_system_codsoft.git
cd recommendation_system_codsoft

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your TMDb API key in `utils.py`
TMDB_API_KEY = "your_tmdb_api_key_here"

# Run Streamlit App
streamlit run app/app.py
```
---
## 📌 Dataset Used

**[MovieLens Latest Small Dataset (ml-latest-small)](https://grouplens.org/datasets/movielens/)**  
Contains 100,000 ratings and 9,000+ movies.  
Excellent for prototyping recommendation algorithms.

---

## 🌐 TMDb API

We use **[The Movie Database (TMDb) API](https://www.themoviedb.org/settings/api)** to fetch:

- 🎞️ Movie Posters  
- 📝 Descriptions/Overviews  

You can get your own API key by signing up at the link above.

---

## 💡 Future Enhancements

- 🔐 User login with actual rating submission  
- 🎯 Real-time feedback loops to update predictions  
- 🧠 Deep NLP-based content similarity (using movie plots or reviews)  
- 📈 Analytics dashboard for user behavior insights  

---

## 👤 Author

**Suryesh Pandey**  
_B.Sc. (Computing) — Bennett University_

- 🔗 [LinkedIn](https://www.linkedin.com/in/suryesh-pandey-61b7a2291)  


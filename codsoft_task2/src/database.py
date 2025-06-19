import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("recommendations.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    input_movie TEXT,
                    recommended_movie TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def save_to_db(user_id, input_movie, recommendations):
    conn = sqlite3.connect("recommendations.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for movie in recommendations:
        c.execute("INSERT INTO history (user_id, input_movie, recommended_movie, timestamp) VALUES (?, ?, ?, ?)",
                  (user_id, input_movie, movie, timestamp))
    conn.commit()
    conn.close()

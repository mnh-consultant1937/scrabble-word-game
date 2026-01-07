# db.py
import sqlite3

DB_NAME = "scrabble.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        score INTEGER,
        played_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

# User Management Functions
# db.py (continue)

def get_or_create_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
    else:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid

    conn.close()
    return user_id



# Score Persistence
def save_score(user_id, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (user_id, score) VALUES (?, ?)",
        (user_id, score)
    )

    conn.commit()
    conn.close()

# Fetch Leaderboard (Optional but Powerful)
def get_top_scores(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT users.username, scores.score, scores.played_at
    FROM scores
    JOIN users ON users.id = scores.user_id
    ORDER BY scores.score DESC
    LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return results
















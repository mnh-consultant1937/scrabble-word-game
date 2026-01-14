import sqlite3
from datetime import datetime

DB_NAME = "scrabble.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            score INTEGER,
            played_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_round(word, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO rounds (word, score, played_at)
        VALUES (?, ?, ?)
    """, (word, score, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_game_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*), SUM(score), MAX(score)
        FROM rounds
    """)

    rounds, total, best = cursor.fetchone()
    conn.close()

    return {
        "rounds": rounds or 0,
        "total_score": total or 0,
        "best_score": best or 0
    }

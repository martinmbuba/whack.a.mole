import sqlite3

DB_PATH = "whackamole.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS players (
            name TEXT PRIMARY KEY,
            score INTEGER DEFAULT 0,
            highscore INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def get_player(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT score, highscore FROM players WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    return result

def add_or_update_player(name, score, highscore):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO players (name, score, highscore)
        VALUES (?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            score=excluded.score,
            highscore=excluded.highscore
    """, (name, score, highscore))
    conn.commit()
    conn.close()
import sqlite3

DB_PATH = "whackamole.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS players (
            name TEXT PRIMARY KEY,
            highscore INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def get_player(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT highscore FROM players WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    return result

def add_or_update_player(name, highscore):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO players (name, highscore)
        VALUES (?, ?)
        ON CONFLICT(name) DO UPDATE SET
            highscore=excluded.highscore
    """, (name, highscore))
    conn.commit()
    conn.close()
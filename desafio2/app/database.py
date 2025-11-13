import sqlite3
import os

DB_PATH = "/data/meubanco.db"

os.makedirs("/data", exist_ok=True)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")

cursor.execute("INSERT INTO usuarios (nome) VALUES ('Felipe');")
conn.commit()

cursor.execute("SELECT * FROM usuarios;")
for row in cursor.fetchall():
    print("Usuário:", row)

conn.close()

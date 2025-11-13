from flask import Flask
import psycopg2
import redis
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "meubanco")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
CACHE_HOST = os.getenv("CACHE_HOST", "cache")

def wait_for_services():
    # tenta conectar ao banco e cache até 10 vezes
    for i in range(10):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            conn.close()
            r = redis.Redis(host=CACHE_HOST, port=6379)
            r.ping()
            print("Serviços disponíveis!")
            return True
        except Exception as e:
            print(f"Tentando novamente ({i+1}/10)... {e}")
            time.sleep(3)
    return False

@app.route("/")
def index():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS acessos (id SERIAL PRIMARY KEY, msg TEXT)")
    cur.execute("INSERT INTO acessos (msg) VALUES ('Novo acesso à aplicação')")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM acessos;")
    total = cur.fetchone()[0]
    conn.close()

    r = redis.Redis(host=CACHE_HOST, port=6379)
    r.incr("visitas")
    visitas = int(r.get("visitas"))
    return f"Banco PostgreSQL tem {total} registros. Redis conta {visitas} visitas.\n"

if __name__ == "__main__":
    print("Aguardando serviços...")
    if wait_for_services():
        print("Iniciando servidor Flask...")
        app.run(host="0.0.0.0", port=8080)
    else:
        print("Serviços indisponíveis. Encerrando.")

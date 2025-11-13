from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Servidor Flask ativo! Hora atual: {now}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

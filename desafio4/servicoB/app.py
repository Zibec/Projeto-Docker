from flask import Flask
import requests

app = Flask(__name__)

@app.get("/")
def home():
    try:
        response = requests.get("http://servicoA:5001/usuarios")
        usuarios = response.json()

        html = "<h1>Usuários cadastrados</h1><ul>"
        for u in usuarios:
            html += f"<li>{u['nome']}</li>"
        html += "</ul>"

        return html

    except Exception as e:
        return f"Erro ao comunicar com o Serviço A: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/usuarios")
def listar_usuarios():
    dados = [
        {"id": 1, "nome": "Felipe"},
        {"id": 2, "nome": "Laura"},
        {"id": 3, "nome": "Matias"}
    ]
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

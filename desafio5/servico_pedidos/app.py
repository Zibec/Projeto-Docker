from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/pedidos")
def listar_pedidos():
    dados = [
        {"id": 101, "usuario_id": 1, "produto": "Monitor"},
        {"id": 102, "usuario_id": 2, "produto": "Teclado"},
        {"id": 103, "usuario_id": 1, "produto": "Mouse"}
    ]
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

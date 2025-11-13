from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/usuarios")
def lista_usuarios():
    usuarios = [
        {"id": 1, "nome": "Felipe"},
        {"id": 2, "nome": "Laura"},
        {"id": 3, "nome": "Matias"}
    ]
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

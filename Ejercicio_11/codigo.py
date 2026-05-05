from flask import Flask, Response, render_template_string, jsonify
import cv2
from pyzbar import pyzbar

app = Flask(__name__)

ultimo_codigo = ""

cap = cv2.VideoCapture(0)  # ← usa el mismo que SÍ funcionó en tu test

def generar_frames():
    global ultimo_codigo

    while True:
        success, frame = cap.read()

        if not success:
            continue  # ← importante, no romper el stream

        # Detectar códigos
        codigos = pyzbar.decode(frame)

        for codigo in codigos:
            x, y, w, h = codigo.rect

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            datos = codigo.data.decode("utf-8")
            tipo = codigo.type

            texto = f"{datos} ({tipo})"
            ultimo_codigo = texto

            cv2.putText(frame, texto, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

        # 🔥 convertir correctamente a JPEG
        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lector de Código</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #f4f4f4;
            }
            img {
                margin-top: 20px;
                border-radius: 10px;
            }
            #codigo {
                font-size: 24px;
                margin-top: 15px;
                color: green;
                font-weight: bold;
            }
            button {
                margin-top: 10px;
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                border-radius: 5px;
                background: #4CAF50;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Lector de Código de Barras</h1>

        <img src="/video" width="500">

        <div id="codigo">Esperando código...</div>

        <!-- 🔥 BOTÓN NUEVO -->
        <button onclick="copiarTexto()">Copiar código</button>

        <script>
            function copiarTexto() {
                let texto = document.getElementById("codigo").innerText;

                if (texto === "Esperando código...") {
                    alert("No hay código para copiar");
                    return;
                }

                navigator.clipboard.writeText(texto)
                .then(() => {
                    alert("Código copiado ✅");
                })
                .catch(() => {
                    alert("Error al copiar ❌");
                });
            }

            setInterval(() => {
                fetch('/codigo')
                .then(r => r.json())
                .then(data => {
                    document.getElementById('codigo').innerText =
                        data.codigo || "Esperando código...";
                });
            }, 500);
        </script>
    </body>
    </html>
    """)


@app.route('/video')
def video():
    return Response(generar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/codigo')
def codigo():
    return jsonify({"codigo": ultimo_codigo})


if __name__ == "__main__":
    app.run(debug=True)

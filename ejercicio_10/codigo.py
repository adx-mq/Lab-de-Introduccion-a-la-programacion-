from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

USUARIO = "admin"
CONTRASENA = "admin2026"

# ---------------- LOGIN ----------------
LOGIN_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Login</title>
<style>
body{font-family:Arial;background:#f3f4f6;display:flex;justify-content:center;align-items:center;height:100vh;}
.card{background:white;padding:30px;border-radius:12px;width:320px;box-shadow:0 10px 25px rgba(0,0,0,0.1);}
input{width:100%;padding:10px;margin:10px 0;border-radius:8px;border:1px solid #ccc;}
button{width:100%;padding:10px;background:#2563eb;color:white;border:none;border-radius:8px;}
.error{color:red;text-align:center;}
</style>
</head>
<body>

{% if session.get("autenticado") %}
    <script>window.location.href="/menu";</script>
{% endif %}

<form class="card" method="post">
    <h2>Login</h2>
    <input type="text" name="usuario" placeholder="Usuario" required>
    <input type="password" name="contrasena" placeholder="Contraseña" required>
    <button>Ingresar</button>
    {% if error %}<p class="error">{{error}}</p>{% endif %}
</form>

</body>
</html>
"""

# ---------------- MENU ----------------
MENU_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Menú</title>
<style>
body{background:#111;color:white;font-family:Arial;}
.header{display:flex;justify-content:space-between;padding:20px;}
.logout{color:red;font-size:22px;text-decoration:none;}
.container{display:flex;justify-content:center;gap:30px;margin-top:50px;}
.card{background:#1f1f1f;padding:30px;border-radius:15px;width:200px;text-align:center;box-shadow:0 0 10px black;transition:0.3s;}
.card:hover{transform:scale(1.05);}
a{text-decoration:none;color:white;}
</style>
</head>
<body>

<div class="header">
<h2>Menú Principal</h2>
<a href="/logout" class="logout">❌</a>
</div>

<div class="container">
<div class="card"><a href="/numeros">Clasificar Número</a></div>
<div class="card"><a href="/edad">Edad y Permisos</a></div>
<div class="card"><a href="/tarifa">Calcular Tarifa</a></div>
</div>

</body>
</html>
"""

# ---------------- NUMEROS ----------------
NUMEROS_HTML = """
<h2>Clasificar Número</h2>
<form method="post">
<input type="number" name="numero" required>
<button>Clasificar</button>
</form>
<p>{{resultado}}</p>
<a href="/menu">Volver</a>
"""

# ---------------- EDAD + PERMISOS ----------------
EDAD_HTML = """
<h2>Categoría de Edad y Permisos</h2>
<form method="post">
<input type="number" name="edad" required>
<button>Evaluar</button>
</form>
<p>{{resultado}}</p>
<a href="/menu">Volver</a>
"""

# ---------------- TARIFA ----------------
TARIFA_HTML = """
<h2>Calcular Tarifa</h2>
<form method="post">
<input type="number" name="edad" required>
<button>Calcular</button>
</form>
<p>{{resultado}}</p>
<a href="/menu">Volver</a>
"""

# ---------------- RUTAS ----------------

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        if usuario == USUARIO and contrasena == CONTRASENA:
            session["autenticado"] = True
            return redirect(url_for("menu"))

        return render_template_string(LOGIN_HTML, error="Datos incorrectos")

    return render_template_string(LOGIN_HTML, error=None)


@app.route("/menu")
def menu():
    if not session.get("autenticado"):
        return redirect(url_for("login"))
    return render_template_string(MENU_HTML)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# --------- NUMEROS ----------
@app.route("/numeros", methods=["GET", "POST"])
def numeros():
    if not session.get("autenticado"):
        return redirect(url_for("login"))

    resultado = ""
    if request.method == "POST":
        n = int(request.form["numero"])

        if n > 0:
            resultado = "Número positivo"
        elif n < 0:
            resultado = "Número negativo"
        else:
            resultado = "Es cero"

    return render_template_string(NUMEROS_HTML, resultado=resultado)


# --------- EDAD Y PERMISOS ----------
@app.route("/edad", methods=["GET", "POST"])
def edad():
    if not session.get("autenticado"):
        return redirect(url_for("login"))

    resultado = ""
    if request.method == "POST":
        e = int(request.form["edad"])

        if e < 12:
            resultado = "Niño - Sin permisos"
        elif e < 18:
            resultado = "Adolescente - Permisos limitados"
        elif e < 60:
            resultado = "Adulto - Acceso completo"
        else:
            resultado = "Adulto mayor - Acceso especial"

    return render_template_string(EDAD_HTML, resultado=resultado)


# --------- TARIFA ----------
@app.route("/tarifa", methods=["GET", "POST"])
def tarifa():
    if not session.get("autenticado"):
        return redirect(url_for("login"))

    resultado = ""
    if request.method == "POST":
        e = int(request.form["edad"])

        if e < 12:
            resultado = "Tarifa: $50"
        elif e < 60:
            resultado = "Tarifa: $100"
        else:
            resultado = "Tarifa: $70"

    return render_template_string(TARIFA_HTML, resultado=resultado)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)


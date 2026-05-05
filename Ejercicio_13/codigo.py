from flask import Flask,request,jsonify,render_template_string
import sqlite3

app=Flask(__name__)

# ---------------------
# BASE DE DATOS
# ---------------------
def crear_bd():
    con=sqlite3.connect("excel_csu.db")
    cur=con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS productos(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      id_proveedor TEXT,
      nombre_producto TEXT,
      codigo_barras TEXT,
      cantidad INTEGER
    )
    """)

    con.commit()
    con.close()

crear_bd()


# ---------------------
# GUARDAR
# ---------------------
@app.route("/guardar",methods=["POST"])
def guardar():

    data=request.get_json()

    con=sqlite3.connect("excel_csu.db")
    cur=con.cursor()

    cur.execute("""
    INSERT INTO productos
    (
      id_proveedor,
      nombre_producto,
      codigo_barras,
      cantidad
    )
    VALUES(?,?,?,?)
    """,
    (
      data["proveedor"],
      data["nombre"],
      data["codigo"],
      data["cantidad"]
    ))

    con.commit()
    con.close()

    return jsonify({"ok":True})


# ---------------------
# PAGINA
# ---------------------
@app.route("/")
def inicio():

    con=sqlite3.connect("excel_csu.db")
    cur=con.cursor()

    cur.execute("SELECT * FROM productos")
    productos=cur.fetchall()
    con.close()

    pagina="""
<!DOCTYPE html>
<html>
<head>
<title>Escáner Inventario</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>

<style>

body{
font-family:'Segoe UI',sans-serif;
background:linear-gradient(135deg,#74ebd5,#ACB6E5);
margin:0;
padding:0;
}

.caja{
width:900px;
margin:auto;
margin-top:30px;
background:white;
padding:30px;
border-radius:25px;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
}

h2{
text-align:center;
color:#333;
}

input{
width:95%;
padding:12px;
margin:8px;
border-radius:10px;
border:1px solid #ccc;
transition:0.3s;
}

input:focus{
border-color:#4CAF50;
outline:none;
box-shadow:0 0 5px #4CAF50;
}

button{
background:linear-gradient(45deg,#4CAF50,#2E7D32);
color:white;
padding:12px 20px;
border:none;
border-radius:12px;
margin:10px;
cursor:pointer;
font-weight:bold;
transition:0.3s;
}

button:hover{
transform:scale(1.05);
background:linear-gradient(45deg,#66bb6a,#1b5e20);
}

#scanner{
width:450px;
height:300px;
border:4px dashed #4CAF50;
border-radius:15px;
overflow:hidden;
margin:auto;
display:flex;
align-items:center;
justify-content:center;
color:#888;
}

table{
width:100%;
margin-top:25px;
border-collapse:collapse;
overflow:hidden;
border-radius:15px;
}

th,td{
padding:12px;
text-align:center;
}

th{
background:#4CAF50;
color:white;
}

tr:nth-child(even){
background:#f2f2f2;
}

tr:hover{
background:#e0f2f1;
}

p{
text-align:center;
color:#666;
font-size:14px;
}

</style>
</head>

<body>

<div class="caja">

<h2>📦 Captura de Productos</h2>

<input id="proveedor"
placeholder="ID proveedor">

<input id="nombre"
placeholder="Nombre producto">

<input id="codigo"
placeholder="Código barras">

<button onclick="iniciarScanner()">
📷 Escanear Código
</button>

<div id="scanner">Cámara lista para escanear</div>

<br>

<input
id="cantidad"
type="number"
placeholder="Cantidad"
onchange="guardarAuto()">

<p>
Se guarda automáticamente al ingresar la cantidad
</p>


<h2>📊 Productos Guardados</h2>

<table>

<tr>
<th>Proveedor</th>
<th>Producto</th>
<th>Código</th>
<th>Cantidad</th>
</tr>

{% for p in productos %}
<tr>
<td>{{p[1]}}</td>
<td>{{p[2]}}</td>
<td>{{p[3]}}</td>
<td>{{p[4]}}</td>
</tr>
{% endfor %}

</table>

</div>


<script>

function iniciarScanner(){

Quagga.init({
inputStream:{
name:"Live",
type:"LiveStream",
target:document.querySelector("#scanner"),
constraints:{
facingMode:"environment"
}
},

decoder:{
readers:[
"ean_reader",
"ean_8_reader",
"code_128_reader"
]
}

},
function(err){

if(err){
console.log(err);
return;
}

Quagga.start();

});


Quagga.onDetected(function(data){

let codigo=
data.codeResult.code;

document.getElementById(
"codigo"
).value=codigo;

alert(
"Código leído: "+codigo
);

Quagga.stop();

});

}



function guardarAuto(){

let datos={

proveedor:
document.getElementById(
"proveedor"
).value,

nombre:
document.getElementById(
"nombre"
).value,

codigo:
document.getElementById(
"codigo"
).value,

cantidad:
document.getElementById(
"cantidad"
).value

};


if(
datos.proveedor &&
datos.nombre &&
datos.codigo &&
datos.cantidad
){

fetch("/guardar",{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:JSON.stringify(datos)
})
.then(r=>r.json())
.then(x=>{
alert("Guardado");
location.reload();
});

}

}

</script>

</body>
</html>
"""

    return render_template_string(
        pagina,
        productos=productos
    )


if __name__=="__main__":
    app.run(debug=True)

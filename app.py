from flask import Flask,render_template

app = Flask(__name__) #declaramos una app flask __name__ es app.py

@app.route("/") #@decorador agrega funcionalidades. route es una funcionalidad. "/"en esa direccion corre el cod
def hello_world():
    nombre_apellido = "Emanuel Diaz"
    lista = ["carlos","pepe","raul"]
    return render_template("index.html",nombre = nombre_apellido, nombres= lista)

"""@app.route("/bienvenido")#todo lo que se escriba despues de la barra sera una variable
def welcome():
    return "<h2>PRIMERA APIIIIIIII VENTANA DE INICIO</h2>"

@app.route("/bienvenido/<nombre>")
def welcome_name(nombre):
    return f"<h2>BIENVENIDO {nombre} </h2>"

@app.route("/suma/<a>/<b>")
def suma(a,b):
    try:
        result = int(a) + int(b)
        return f"<h1> Result is {result}"
    except:
        return {"Mensaje":"NO PUEDO REALIZAR LA OPERACION"}
    
    """
    
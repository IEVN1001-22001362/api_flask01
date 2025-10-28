from flask import Flask, render_template, request
import math
app= Flask (__name__)

@app.route('/')
def home():
    return "Hello, world!"

@app.route("/index")
def index():
    titulo="IEVN1001"
    listado=["Python", "Flask", "HTML", "CSS", "JavaSscript"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route("/aporb")
def apor():
     return render_template('aporb.html')

@app.route("/resultado", methods=['POST'])
def resulatado():
    n1=request.form.get("a")
    n2=request.form.get("b")
    return "La multiplicación de {} y {} es {}".format(n1,n2, int(n1)*int(n2))




@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    resultado = ""
    # 1.para no preguntar si es metodode GET o POST.
    x1 = float(request.values.get("x1", 0.0))
    y1 = float(request.values.get("y1", 0.0))
    x2 = float(request.values.get("x2", 0.0))
    y2 = float(request.values.get("y2", 0.0))

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    resultado = f"La distancia entre los puntos es {distancia:.2f}"
    
  
    return render_template("distancia.html", resultado=resultado)

@app.route("/figuras",  methods=['GET','POST'] )
def figuras():
     return render_template("figuras.html")


@app.route("/hola")
def func():
    return "<h1>¡Hola!</h1>"

@app.route("/adios/<string:user>")
def user(user):
    return "<h1>¡Hola, {} Loba!</h1>".format(user)

@app.route("/square/<int:num>")
def square(num):
    return "<h1>¡The square of {} is {}.</h1>".format(num, num**2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return "<h1>"+ " ".join([text] * times) + "</h1>"

@app.route('/suma/<float:a>/<float:b>')
def suma(a, b):
    return "<h1>¡The suma of {} and {} is {}.</h1>".format(a, b, a+b)



if __name__ == '__main__':
    app.run(debug=True)
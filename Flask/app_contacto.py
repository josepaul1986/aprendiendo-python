import json
from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello(nombre = "invitado"):
    try:
        data = json.loads(request.cookies.get('data'))
    except TypeError:
        data = {}
    else:
        nombre = data.get('nombre')
    contexto = {'name':nombre}
    return render_template("template2.html", **contexto)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1=0,num2=0):
    contexto = {'num1':num1, 'num2':num2}
    return render_template("template1.html", **contexto)

@app.route("/contacto")
def contacto():
    return render_template("template_contacto.html")

@app.route("/enviar", methods=['POST'])
def enviar():
    response = redirect(url_for('hello'))
    response.set_cookie(json.dumps(dict(request.form.items())))
    response.set_cookie('data',json.dumps(dict(request.form.items())))
    response.set_cookie('session','session_undefined_value')
    ##return "Exito"
    return response

if __name__ == "__main__":
    app.run(debug=True)
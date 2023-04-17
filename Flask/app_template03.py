from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<nombre>")
def hello(nombre = "invitado"):
    contexto = {'name':nombre}
    return render_template("template4.html", **contexto)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1=0,num2=0):
    contexto = {'num1':num1, 'num2':num2}
    return render_template("template3.html", **contexto)

if __name__ == "__main__":
    app.run(debug=True)
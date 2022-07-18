from flask import Flask, request

app = Flask(__name__)


@app.route("/")
@app.route("/<nombre>")
def hello(nombre = "invitado"):
    return "Hola {}".format(nombre)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1=0,num2=0):
    return "El resultado: {} más {} es igual a {}".format(num1, num2, num1 + num2)


if __name__ == "__main__":
    app.run(debug=True)
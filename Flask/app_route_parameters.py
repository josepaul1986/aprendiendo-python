from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello(nombre = "invitado"):
    nombre = request.args.get('nombre', nombre)
    return "Hola {}".format(nombre)


@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1=0,num2=0):
    return "{} más {} es igual a {}".format(num1, num2, num1 + num2)


if __name__ == "__main__":
    app.run(debug=True)
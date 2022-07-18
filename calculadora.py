def operacion(operador, numero1, numero2):
    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2
    elif operador == "*":
        return numero1 * numero2
    else: 
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            return "Division por cero es infinito."
        else:
            return resultado

continuar = "s"

while (continuar == "s" or continuar == "si"):
    op = input("Ingrese el simbolo de la operacion (+,-,*,/):")

    if op not in ["+","-","*","/"]:
        print("Operacion no existente.")
        continue

    try:
        num1 = int(input('Ingrese el primer numero para operar: '))
        num2 = int(input('Ingrese el segundo numero para operar: '))
    except ValueError:
        print("No ingreso un numero valido")
    else:
        print("El resultado es: {0}".format(operacion(op,num1,num2)))
    continuar = input("Deseas continuar [Si/No]?")
    continuar = continuar.lower()

print("Fin del programa.")
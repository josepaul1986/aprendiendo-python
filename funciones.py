def pedir_pizza():
    print("Request successful to wwww.dominos.com.gt/pedidos/pizza ")

def verificar_edad(edad):
    if edad < 18:
        print("No puedes entrar")
    elif edad >= 21:
        print("Puedes entrar al bar y tambien puedes beber.")
    else:
        print("Puedes entrar al bar pero no puedes beber.")

pedir_pizza()

verificar_edad(20)

verificar_edad(17)

verificar_edad(30)
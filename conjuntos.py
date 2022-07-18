# Obtener los sets del usuario
# Hacer la funcion de union
# Hacer la funcion de interseccion
# Hacer la funcion de diferencia
# Hacer la funcion de diferencia simetrica

def ver_menu():
    print("Menu de opciones para sus conjuntos de elementos: ")
    print("1. Union")
    print("2. Interseccion")
    print("3. Diferencia")
    print("4. Diferencia simetrica")
    print("5. Ver menu")
    print("6. Ingresar nuevos conjuntos")
    print("7. Ver conjuntos")
    print("8. Salir")

def imprimir_conjuntos(a,b):
    print("\nConjunto A: ")
    print(a)
    print("Conjunto B: ")
    print(b)

def ingresar_conjuntos():
    print("\n Introduce los elementos de los conjuntos separados por espacios: ")
    print("Ejemplo: 1 2 3 4 5")
    a = set(input("Elementos conjunto A: ").split())
    b = set(input("Elementos conjunto B: ").split())
    return [a,b]

def unir_conjuntos(a,b):
    print("\n La union de A y B es: {} \n".format(a.union(b)))

def intersectar_conjuntos(a,b):
    print("\n La interseccion de A y B es: {} \n".format(a.intersection(b)))

def difrenciar(a,b):
    print("\nQue diferencia deseas ejecutar?: ")
    print("1. A menos B")
    print("2. B menos A")
    diff_op = input("Cual eliges?: ")
    if diff_op == "1":
        print("\n La diferencia de A y B es: {} \n".format(a.difference(b)))
    elif diff_op == "2":
        print("\n La diferencia de A y B es: {} \n".format(b.difference(a)))
    else:
        print("Opcion no reconocida. Intente nuevamente.")
        difrenciar(a,b)

def diferenciar_simetricamente(a,b):
    print("\n La diferencia simetrica de A y B es: {} \n".format(a.symmetric_difference(b)))

def principal():
    print("Programa Ejemplo de conjuntos")
    
    conjuntos = ingresar_conjuntos()
    conjunto_a = conjuntos[0]
    conjunto_b = conjuntos[1]

    ver_menu()

    while True:
        opcion = input("Numero de opcion?: ")
        if opcion == "1":
            print("Union")
            unir_conjuntos(conjunto_a, conjunto_b)
        elif opcion == "2":
            print("Interseccion")
            intersectar_conjuntos(conjunto_a, conjunto_b)
        elif opcion == "3":
            print("Diferencia")
            difrenciar(conjunto_a,conjunto_b)
        elif opcion == "4":
            print("Diferencia simetrica")
            diferenciar_simetricamente(conjunto_a,conjunto_b)
        elif opcion == "5":
            ver_menu()
        elif opcion == "6":
            conjuntos = ingresar_conjuntos()
            conjunto_a = conjuntos[0]
            conjunto_b = conjuntos[1]
        elif opcion == "7":
            imprimir_conjuntos(conjunto_a,conjunto_b)
        elif opcion == "8":
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")
            continue
    print("\nPrograma finalizado")

principal()

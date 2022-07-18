#Agregar articulos
#Remover articulos
#Ver articulos

lista_articulos = list();

def agregar_articulo():
    new_item = input("\nIngrese la descripcion del nuevo articulo: ")
    lista_articulos.append(new_item.capitalize())
    print("\nOK: Articulo agregado!\n")

def remover_articulo():
    for articulo in lista_articulos:
        print("{0}. {1}".format(lista_articulos.index(articulo) + 1,articulo))
    try:
        id = int(input("Seleccione numero del item a eliminar: "))
        del lista_articulos[id-1]
        print("\nOK: Articulo removido!\n")
    except IndexError or ValueError:
        input("\nEl indice no existe, intente de nuevo. Presione enter para continuar.")

def ver_articulos():
    print("\nOK: lista de articulos -> ")
    for articulo in lista_articulos:
        print("{0}. {1}".format(lista_articulos.index(articulo) + 1,articulo))
    input("Presione enter para continuar.")

print("\nBienvenido a la lista de compras: \n")

while True:
    print("\nEstas son las operaciones que puedes realizar:")
    print("1 - Agregar articulo")
    print("2 - Remover articulo")
    print("3 - Ver los articulos")
    print("4 - Salir\n")
    operacion = input("Selecciona una operacion: ")
    if operacion == "1":
        agregar_articulo()
    elif operacion == "2":
        remover_articulo()
    elif operacion == "3":
        ver_articulos()
    elif operacion == "4":
        break
    else:
        print("\nError: opcion de menu no reconocida.\n")
        continue

print("\nPrograma finalizado.\n")
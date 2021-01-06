#Agregar un contacto
#Remover un contacto
#Actualizar un contacto
#Ver un contacto
#Ver todos los contactos

agenda = dict()

def agregar_contacto():
    nombre = input("Nombre del nuevo contacto: ")
    numero = input("Numero del nuevo contacto: ")
    agenda[nombre] = numero
    input("\nOK: contacto agregado! Presione enter para continuar.")

def remover_contacto():
    ver_contactos()
    nombre_busqueda = input("Nombre del contacto a que desea eliminar: ")
    try:
        del agenda[nombre_busqueda]
    except KeyError:
        input("\nERROR: El nombre no fue encontrado. Presione enter para continuar")
    else:
        input("\nOK: contacto removido! Presione enter para continuar.")

def actualizar_contacto():
    ver_contactos()
    nombre_busqueda = input("Nombre del contacto a actualizar: ")
    numero_nuevo = input("Numero del contacto a actualizar: ")
    agenda[nombre_busqueda] = numero_nuevo
    input("\nOK: contacto actualizado! Presione enter para continuar.")

def ver_contacto():
    nombre_busqueda = input("Nombre del contacto a buscar: ")
    try:
        print("\nDatos en agenda: {0} - {1}".format(nombre_busqueda, agenda[nombre_busqueda]))
    except KeyError:
        input("\nERROR: El registro no fue encontrado. Presione enter para continuar.")
    else:
        input("\nOK: contacto desplegado! Presione enter para continuar.")

def ver_contactos():
    print("\nLista de contactos -> \n")
    i = 1
    if len(agenda) == 0:
        input("\nNo tienes ningun contacto registrado. Presiona enter para continuar.")
    else:
        for contacto in agenda:
            print(str(i) + ": " + contacto + " - " + agenda[contacto])
            i += 1
        input("\nPresione enter para continuar.")

def principal():
    while True:
        print("\nEstas son las operaciones que puedes realizar:")
        print("1 - Agregar contacto")
        print("2 - Remover contacto")
        print("3 - Actualizar contacto")
        print("4 - Ver un contacto")
        print("5 - Ver todos los contactos")
        print("6 - Salir\n")
        operacion = input("Selecciona una operacion: ")
        if operacion == "1":
            agregar_contacto()
        elif operacion == "2":
            remover_contacto()
        elif operacion == "3":
            actualizar_contacto()
        elif operacion == "4":
            ver_contacto()
        elif operacion == "5":
            ver_contactos()
        elif operacion == "6":
            break
        else:
            print("\nError: opcion de menu no disponible.\n")
            continue
    print("\nPrograma finalizado.\n")

print("\nBienvenido a la agenda telefonica CLI: \n")
principal()
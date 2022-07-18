#UI
#Agregar articulos
#Ver articulos
#Salir

import os

os.chdir("Archivos")

def add_item(articulo):
    file = open("list.txt","a")
    file.write("{}\n".format(articulo))
    file.close()
    print("Item saved!")

def get_items():
    file = open("list.txt","rt")
    info = file.read()
    file.close()
    print("Lista de compras guardado: \n{}".format(info))

def show_menu():
    print("\n1. Add an item")
    print("2. Show all items")
    print("3. Show the menu")
    print("4. Exit")

print("Welcome to market list maker!")
show_menu()

operation = "0"
while operation != "6":
    operation = input(": ")
    if operation == "1":
        add_item(input("Escribe aqui el articulo que quieres agregar: "))
    elif operation == "2":
        get_items()
    elif operation == "3":
        show_menu()
    elif operation == "4":
        break
    else:
        print("\nError: Invalid option.")

print("App closed! Bye!")
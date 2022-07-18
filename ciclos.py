manzanas = 10

while manzanas > 0:
    print("Me estoy comiendo la manzana " + str(manzanas))
    manzanas -= 1

print("Sin manzanas :)")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero == 5:
        continue
    print(numero)


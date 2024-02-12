import random

n = int(input("Ingrese el tamaño de la lista"))

lista_numeros = []

for i in range(0, n):

    lista_numeros.append(random.randint(1 , 100))

print(lista_numeros)
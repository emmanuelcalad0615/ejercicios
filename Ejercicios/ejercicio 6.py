#Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
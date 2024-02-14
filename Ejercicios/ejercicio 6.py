#Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

#como se usa la lista
"""
lista_numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(lista_numeros)
print(resultado)
"""

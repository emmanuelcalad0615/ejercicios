#Escribir una función que calcule el factorial de un número dado

def factorial(x):
    if x == 0 or n == 1:
        resultado=1
    elif x > 1:
        resultado=x*factorial(x-1)
    return resultado
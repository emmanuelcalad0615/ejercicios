#Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida
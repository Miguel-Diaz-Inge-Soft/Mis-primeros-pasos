# se tiene la sig lista=[[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
#imprimir la lista, posterior fijar con el valor cero todos los elementos mayores
#a 10, contenidos en todos los elementos de la variable "lista"


lista=[[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
print(f"Impresión de la lista: {lista}")


for k in range(len(lista)):
    for x in range(len(lista[k])):
        if lista[k][x]>10:
            lista[k][x]=0


print(f"Impresión de la lista ya modificada: {lista}")

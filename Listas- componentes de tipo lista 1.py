#creacion de lista por asignación

lista=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print(lista)
print("------")
#imprimer el primer componente de la lista
print(lista[0])
print("------")

#imprimir el primer valor de la primera lista de la lista
print(lista[0][0])
print("------")

#imprimir cada componente de la primera lista de toda la lista
for x in range(len(lista[0])):
    print(lista[0][x])
print("------")

#imprimir todos los valores de cada lista contenida dentro de la lista principal
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
print("------")


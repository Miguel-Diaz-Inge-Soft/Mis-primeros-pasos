lista=[]
#obtener el numero mayor de una lista
for x in range (5):
    valor=int(input("Ingresar valor: "))
    lista.append(valor)

mayor=lista[0]

for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print(f"Lista completa: {lista}")
print(f"Mayor de la lista: {mayor}")

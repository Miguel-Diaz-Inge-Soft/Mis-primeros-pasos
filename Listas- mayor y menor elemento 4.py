lista=[]
suma=1
for x in range(5):
    valor=int(input(f"Ingresar valor {x+1}: "))
    lista.append(valor)

mayor=lista[0]

for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
    else:
        if lista[x]==mayor:
            suma=suma+1

print(f"Número que es el mayor de todos; {mayor}")
print(f"Se repite {suma} veces en la lista")


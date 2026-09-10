lista=[]

for x in range(5):
    valor=int(input(f"Ingresar valor {x+1}: "))
    lista.append(valor)

menor=lista[0]

for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion = x+1

print(f"Lista de los vaalores: {lista}")
print(f"Número menor: {menor}")
print(f"posición del número menor: {posicion}")

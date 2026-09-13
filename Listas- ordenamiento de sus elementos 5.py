valores=[]

n=int(input("Ingresar cantidad de valores a procesar: "))

for i in range(n):
    valor=int(input(f"Ingresar valor {i+1}: "))
    valores.append(valor)

for k in range(n-1):
    for x in range(n-1):
        if valores[x]>valores[x+1]:
            aux=valores[x]
            valores[x]=valores[x+1]
            valores[x+1]=aux
print(f"Lista ordenada de menor a mayor: {valores}")

for k in range(n-1):
    for x in range(n-1):
        if valores[x]<valores[x+1]:
            aux=valores[x]
            valores[x]=valores[x+1]
            valores[x+1]=aux

print(f"Lista ordenada de mayor a menor: {valores}")

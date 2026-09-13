sueldos=[]

for x in range(5):
    valor=int(input(f"Ingresar valor {x+1}: "))
    sueldos.append(valor)

print(f"Lista desordenada: {sueldos}")

for k in range(4):
    for x in range(4-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print(f"Lista ordenada: {sueldos}")

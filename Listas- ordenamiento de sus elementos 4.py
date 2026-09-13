sueldos=[]

n=int(input("Ingresar cantidad de trabajadores a procesar: "))

for x in range(n):
    sueldo=int(input(f"Ingresar sueldo del trabajador {x+1}: "))
    sueldos.append(sueldo)
    
print(f"Lista de sueldos previa al ordenamientos: {sueldos}")

for k in range(n-1):
    for x in range(n-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print(f"Sueldos de manera ordenada: {sueldos}")


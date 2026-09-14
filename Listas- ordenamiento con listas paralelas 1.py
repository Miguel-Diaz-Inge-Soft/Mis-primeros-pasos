nombres=[]
notas=[]

n=int(input("Ingresar cantidad de alumnos a procesar: "))

for x in range(n):
    nombre=input(f"Ingresar nombre del alumno {x+1}: ")
    nombres.append(nombre)
    nota=float(input(f"Ingresar nota del alumno {x+1}: "))
    notas.append(nota)

print("Lista previa al ordenamiento:")
print(nombres)
print(notas)

for k in range(n-1):
    for x in range(n-1-k):
        if notas[x]<notas[x+1]:
            aux=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux

            aux2=nombres[x]
            nombres[x]=nombres[x+1]
            nombres[x+1]=aux2

print("Lista ordenada de mayor a menor")
print(nombres)
print(notas)

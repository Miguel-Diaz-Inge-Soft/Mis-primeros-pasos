empleados=[]
faltas=[]

n=int(input("Ingresar cantidad de empleados a procesar: "))

for x in range(n):
    faltas.append([])
    empleado=input(f"Ingresar nombre del empleado N° {x+1}: ")
    empleados.append(empleado)

    n2=int(input("¿Cuántos días faltó? "))
    for k in range (n2):
        falta=int(input(f"Ingresar día del mes que faltó {empleado}: "))
        faltas[x].append(falta)

print("Nombres y días de faltas")
for x in range(n):
    print(empleados[x], ", faltó: ", faltas[x])

print("Empledos que tuvieron menos faltas")
for x in range(n):
    if len(faltas[x])<=2:
        print(empleados[x], "faltas: ", len(faltas[x]))
        

empleados=[]
sueldos=[]

n=int(input("Ingresar cantidad de empleados a procesar: "))


for x in range(n):
    empleado=input(f"Ingresar empleado N° {x+1}: ")
    empleados.append(empleado)
    sueldo=int(input(f"Ingresar sueldo de {empleado}: "))
    sueldos.append(sueldo)

print("Lista de empleados y sueldos")
for x in range(n):
    print(empleados[x], " - ", sueldos[x])

posicion=0
while posicion<len(empleados):
    if sueldos[posicion]>1000:
        empleados.pop(posicion)
        sueldos.pop(posicion)
    else:
        posicion=posicion+1

print("Lista de empleados y sueldos actualizada")
for x in range(len(sueldos)):
    print(empleados[x], " - ",sueldos[x])

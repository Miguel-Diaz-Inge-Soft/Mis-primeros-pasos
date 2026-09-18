empleados=[]
sueldos=[]
totalsueldos=[]
suma1=0
suma2=0
suma3=0

for x in range(3):
    empleado=input(f"Ingresar nombre del empleado {x+1}: ")
    empleados.append(empleado)
    sueldo1=int(input(f"Ingresar primer sueldo mensual del empleado {x+1}: "))
    sueldo2=int(input(f"Ingresar segundo sueldo mensual del empleado {x+1}: "))
    sueldo3=int(input(f"Ingresar tercer sueldo mensual del empleado {x+1}: "))
    sueldos.append([sueldo1,sueldo2,sueldo3])

for x in range(3):
    suma1=suma1+sueldos[0][x]
    suma2=suma2+sueldos[1][x]
    suma3=suma3+sueldos[2][x]

totalsueldos.append([suma1,suma2,suma3])

print("Sueldos pagados durante los últimos 3 meses: ")
print(empleados)
print(sueldos)

if suma1>suma2 and suma1>3:
    print(f"Empleado con mayor sueldo: {empleados[0]}, {suma1}")
elif suma2>suma1 and suma2>suma3:
    print(f"Empleado con mayor sueldo: {empleados[1]}, {suma2}")
elif suma3 > suma1:
    print(f"Empleado con mayor sueldo: {empleados[2], {suma3}}")

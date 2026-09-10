n=int(input("Ingresar cantidad de operarios de la mañana: "))
n2=int(input("Ingresar cantidad de operarios de la tarde: "))
sueldo_mañana=[]
sueldo_tarde=[]
for x in range(n):
      sueldo1=float(input(f"Ingresar sueldo de la mañana del operario {x+1}: "))
      sueldo_mañana.append(sueldo1)
for x in range(n2):
    sueldo2=float(input(f"Ingresar sueldo de la tarde del operario {x+1}: "))
    sueldo_tarde.append(sueldo2)

print(f"sueldos de la mañana: {sueldo_mañana}")
print(f"sueldos de la tarde: {sueldo_tarde}")


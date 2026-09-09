lista=[]
suma=0

for x in range(5):
    sueldo=float(input(f"Ingresar sueldo del empleado {x+1}: "))
    lista.append(sueldo)
    suma=suma+sueldo

prom=suma/5

print(f"El promedio de los 5 sueldos de cada empledo es de : {prom}")

      

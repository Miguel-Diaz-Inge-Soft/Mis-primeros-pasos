n=int(input("ingresar cantidad de valores a cargar"))
suma1=0
suma2=0

for x in range (n):
    valor=int(input("ingresar valor"))
    if valor>=100:
        suma1=suma1+1
    else:
        suma2=suma2+1
print("valores que son mayores e iguales a 1000: ",suma1)
print("valores que son menores a 1000: ",suma2)

n=int(input("ingresar cantidad de personas a registrar: "))
x=1
suma=0

while x<=n:
    altura=float(input("ingresar altura de la persona en metros: "))
    suma=suma+altura
    x=x+1
prom=suma/n
print("el promedio de las alturas es de: ",prom)

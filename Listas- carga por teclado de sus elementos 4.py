lista=[]
suma=0
mas_prom=0
men_prom=0
n=int(input("Ingresar cantidad de alturas a cargar: "))

for x in range(n):
    altura=float(input(f"Ingresar altura de la persona {x+1}: "))
    lista.append(altura)
    suma=suma+altura

prom=suma/n

for x in range(n):
    if lista[x]>prom:
        mas_prom=mas_prom+1
    else:
        if lista[x]<prom:
            men_prom=men_prom+1
        
print(f"Suma de los valores ingresados {suma}")
print(f"Promedio de los valores ingresados {prom}")
print(f"Personas más altas que el promedio: {mas_prom}")
print(f"Personas más bajas que el promedio: {men_prom}")

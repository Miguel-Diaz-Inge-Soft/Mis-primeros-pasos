suma=0
n=int(input("ingresar cantidad de valores a procesar: "))


for x in range(n):
    valor=int(input("ingresar valor: "))
    if x>=n-5:
        suma=suma+valor
print("suma de los ultimos 5 numeros: ",suma)
    



def menor_mayor(enteros,cant):
    
    for x in range(cant):
        for k in range(0,cant-x-1):
            if enteros[k]>enteros[k+1]:
                aux=enteros[k]
                enteros[k]=enteros[k+1]
                enteros[k+1]=aux


    print(f"Lista ordenada: {enteros}")


def carga ():
    lista=[]
    n=int(input("Ingresar cuántos valores desea ordenar: "))

    for x in range(n):
        valor=int(input(f"Ingresar valor {x+1}: "))
        lista.append(valor)

    menor_mayor(lista,n)

#Principal
carga()

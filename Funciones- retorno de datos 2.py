def mayor_numero(numeros):
    mayor=numeros[0]

    for x in range (1, len(numeros)):
        if mayor<numeros[x]:
            mayor=numeros[x]

    return mayor

def carga():
    n=int(input("¿cuántos números va a ingresar?"))
    lista=[]
    for x in range(n):
        valor=int(input(f"Ingresar valor {x+1}: "))
        lista.append(valor)
        
    mayor_numero(lista)


    print(f"Lista de valores: {lista}")
    print(f"El número mas grande de la lista es: {mayor_numero(lista)}")



#PRINCIPAL
carga()

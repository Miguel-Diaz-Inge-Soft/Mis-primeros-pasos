def menor():
    lista=[]
    for x in range(3):
        valor=int(input(f"Ingresar valor {x+1}: "))
        lista.append(valor)

    menor=lista[0]
    for x in range(1,3):
        if menor > lista[x]:
            menor =lista[x]
        else:
            pass
    print(f"El menor número de los 3 es: {menor} ")
    print("----------------------------------------------------")
#Maín
menor()
menor()
menor()

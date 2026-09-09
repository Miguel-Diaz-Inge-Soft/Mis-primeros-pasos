frase=int(input("Escribir el número '00' si desea salir, 2 para continuar: "))
lista=[]
x=0
while  True:
    if frase !=00:
        x=x+1
        valor=int(input(f"Ingresar valor {x}, (digite '00' para salir): "))
        lista.append(valor)
        if valor==00:
            break
    else:
            break
        
print("Programa finalizado")
print(lista)

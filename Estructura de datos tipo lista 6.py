lista=[]
suma=0
x=0
while x<5:
    nombre=input(f"Ingresar nombre {x+1 } de 5 : ")
    lista.append(nombre)
    if len(nombre)>=5:
        suma=suma+1
    x=x+1

print("numeros iguales o mayores a 5 caracteres: ",suma)


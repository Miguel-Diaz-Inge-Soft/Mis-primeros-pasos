lista=[]
lista2=[]
n=int(input("¿Cuántos valores se van a cargar? "))

for x in range(n):
    valor=int(input(f"Ingresar valor {x+1}: "))
    lista.append(valor)

posicion=0
while posicion<len(lista):
    if lista[posicion]>=10:
        lista2.append(lista[posicion])
        lista.pop(posicion)
    else:
        posicion=posicion+1

print("Lista actualizada: ")
print(lista)
print("Lista nueva: ")
print(lista2) 

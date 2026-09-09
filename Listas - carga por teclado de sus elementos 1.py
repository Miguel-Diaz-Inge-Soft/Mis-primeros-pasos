n=int(input("¿Cuántos valores desea agregar? " ))
lista=[]
x=0

while x<n:
    valor=int(input(f"Agregar valor {x+1}: "))
    lista.append(valor)
    x=x+1

print(f"Lista de los valores: {lista}")

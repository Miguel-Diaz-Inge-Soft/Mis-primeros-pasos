listas=[]
suma=0

#Se colicita por teclado dos enteros, el primero indica la catdad de elementos que crearemos en la lista
#El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal
#Por último imprimir la suma de todos los elementos
n=int(input("¿Cuántas listas desea cargar? "))
v=int(input("¿Cuántos valores cargará en cada lista? "))

for k in range(n):
    listas.append([])
    for x in range(v):
        valor=int(input(f"Ingrese valor {x+1} de la lista {k+1}: "))
        listas[k].append(valor)
        suma=suma+listas[k][x]

print(f"La suma de todos lo valores es de : {suma}")

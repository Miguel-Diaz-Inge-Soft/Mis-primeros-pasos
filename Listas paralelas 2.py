productos=[]
precios=[]

for x in range (5):
    producto=input(f"Ingresar nombre del producto {x+1}: ")
    productos.append(producto)
    precio=int(input(f"Ingresar precio del producto {x+1}: "))
    precios.append(precio)

suma=0

for x in range(1,5):
    if precios[0]<precios[x]:
        suma=suma+1

print("Productos y precios: ")
print(productos)
print(precios)
print(f"Productos que tiene mayor valor al primero: {suma}")

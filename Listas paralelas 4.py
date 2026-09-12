lista1=[]
lista2=[]
lista3=[]

n=int(input("Ingresar cantidad de datos pares a procesar: "))
      
for x in range(n):
      valor=int(input("Ingresar valor de la lista 1: "))
      lista1.append(valor)
      valor2=int(input("Ingresar valor de la lista 2: "))
      lista2.append(valor2)


for x in range(n):
      valor3=lista1[x]+lista2[x]
      lista3.append(valor3)

print(f"Lista 1:                                            {lista1}")
print(f"Lista 2:                                            {lista2}")
print(f"Lista de la suma de las dos listas: {lista3} ")

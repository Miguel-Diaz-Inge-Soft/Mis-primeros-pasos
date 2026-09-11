lista1=[]

for x in range (5):
    nom=input(f"Ingresar nombre de la persona {x+1}: ")
    lista1.append(nom)

menor=lista1[0]

for x in range (1,5):
    if lista1[x]<menor:
        menor=lista1[x]

        
print(f"Lista de nombres Ingresados: {lista1}")
print(f"Menor nombre alfabeticamente: {menor}")

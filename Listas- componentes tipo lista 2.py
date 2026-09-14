lista=[[1,2,3,4,5],[6,7,8,9,10]]

suma1=0
suma2=0

#primer forma de resolverlo
for x in range(len(lista[0])):
    suma1=suma1+lista[0][x]
    

for x in range(len(lista[1])):
    suma2=suma2+lista[1][x]

print(f"Suma de la primer lista: {suma1}")
print(f"Suma de la segunda lista: {suma2}")
print("------")

#Segunda forma de resolverlo
for k in range(len(lista)):
    suma=0
    for x in range(len(lista[k])):
        suma=suma+lista[k][x]
    print(f"Suma de la primer lista: {suma}")
    

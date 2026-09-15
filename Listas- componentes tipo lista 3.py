lista=[[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]

suma=0

for k in range(len(lista)):
    for x in range(len(lista[k])):
        
     suma=suma+lista[k][x]


print(f"Suma de todos los valores de la listas: {suma}")

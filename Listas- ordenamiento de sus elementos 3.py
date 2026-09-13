paises=[]

for x in range(5):
    pais=input(f"Ingresar país {x+1}: ")
    paises.append(pais)

print(f"Lista sin ordenar: {paises}")
    
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

print(f"Lista ordenada de los paises alfabéticamente: {paises}")

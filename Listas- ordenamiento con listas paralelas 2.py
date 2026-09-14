paises=[]
abis=[]

n=int(input("ingresar cantidad de paises  procesar: "))

for x in range(n):
    pais=input(f"Ingresar nombre del pais {x+1}: ")
    paises.append(pais)
    abi=int(input(f"Ingresar cantidad de habitates que tiene {paises[x]}: "))
    abis.append(abi)


for k in range(n-1):
    for x in range(n-1):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux

            aux2=abis[x]
            abis[x]=abis[x+1]
            abis[x+1]=aux2

            
            
print("Listado de los paises ordenados alfabeticamente: ")
print(paises)
print(abis)

for k in range(n-1):
    for x in range(n-1):
        if abis[x]>abis[x+1]:
            aux=abis[x]
            abis[x]=abis[x+1]
            abis[x+1]=aux

            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2

print("Listado de los paises ordenados por cantidad de población de menor a mayor: ")
print(abis)
print(paises)

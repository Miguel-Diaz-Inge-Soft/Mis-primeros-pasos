padres=[]
hijos=[]

n=int(input("Ingresar cuántas familia va a registrar: "))

for k in range(n):
    hijos.append([])
    padre=input(f"Nombre del padre {k+1}: ")
    madre=input(f"Nombre de la madre {k+1}: ")
    padres.append([padre,madre])

    condicion1=input("¿tienen hijos? (responda con un si o un no) ")
    condicion2=condicion1.lower()
    
    if condicion2=="si":
        n2=int(input("¿Cuántos hijos tienen? "))
        for x in range(n2):
            hijo=input(f"Ingresar nombre del hijo/a {x+1}: ")
            hijos[k].append(hijo)
    elif condicion2=="no":
        pass
            
        
print("Lista de padres y sus hijos: ")
print(padres)
print(hijos)


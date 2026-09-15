#se tiene la siguiente lista;
#Lista=[[100,7,85,8],[4,8,56,25][67,89,23,1][78,56]]
#Imprimir la lista, posterior se fija con el valor cero
#todos los elementos mayor a 50 del primer elemento de la "lista" osea lista=[100,7,85,8]


lista=[[100,7,85,8],[4,8,56,25],[67,89,23,1],[78,56]]
print(f"Impreción de lista: {lista}")

for x in range(len(lista[0])):
    if lista[0][x]>50:
        
        lista[0][x]=0

print(f"Lista ya modificada: {lista}")




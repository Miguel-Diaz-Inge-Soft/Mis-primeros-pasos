lista=[12,999,450,300,67,89,456,876]
suma=0
x=0
while x<len(lista):
    if lista[x]>=100:
        suma=suma+1
    x=x+1
print("valores que excede la cantidad de 100 en la lista: ",suma)

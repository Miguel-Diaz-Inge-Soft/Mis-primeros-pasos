lista=[]

#Primer métedo 
for x in range(1,51):  
    lista.append(list(range(1, x + 1)))
print(lista)

#segundo método para hacerlo

lista=[list(range(1,x+1))for x in range(1,51)]
print(lista)

numeros=[]

for x in range(10):
    numero=int(input("Ingresar número: "))
    numeros.append(numero)
print(numeros)


posicion=0

while posicion<len(numeros):
    if numeros[posicion]==5:
        numeros.pop(posicion)
    else:
        posicion=posicion+1




print(numeros)

x=1
cantma=0
cantme=0
while x<=10:
    notas=int(input("ingresa la nota: "))
    if notas >=7:
        cantma=cantma+1
    else:
        cantme=cantme+1
    x=x+1
print("cantidad de notas mayores o iguales a 7")
print(cantma)
print("cantidad de notas menores a 7")
print(cantme)

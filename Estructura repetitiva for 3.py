suma1=0
suma2=0

for x in range (10):
    nota=int(input("ingresar nota"))
    if nota>=7:
        suma1=suma1+1
    else:
        suma2=suma2+1

print("notas mayor o igual a 7: ",suma1)
print("notas menor a 7: ",suma2)

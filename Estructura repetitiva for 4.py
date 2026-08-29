suma1=0
suma2=0

for x in range(10):
    valor=int(input("ingresar valor: "))
    if valor%5==0 and valor%5==0:
        suma1=suma1+1
        suma2=suma2+1
    else:
        if valor%5==0:
            suma1=suma1+1
        else:
            if valor%3==0:
                suma2=suma2+1
print("valores que son multiplos de 5: ",suma1)
print("valores que son multiplos de 3: ",suma2)

suma1=0
suma2=0
x=1
while x<=15:
    ingreso=int(input("ingresar valor: "))
    suma1=suma1+ingreso
    x=x+1
print(".......")
x=1
while x<=15:
    ingreso2=int(input("ingresar valor: "))
    suma2=suma2+ingreso2
    x=x+1
    
if suma1>suma2:
    print(suma1," es mayor primer lista")
else:
    print(suma2," es mayor segunda lista")

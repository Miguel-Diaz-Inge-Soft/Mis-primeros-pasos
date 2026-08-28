x=1
par=0
impar=0
n=int(input("ingresa cantidad de valores a procesar: "))

while x<=n:
    valor=int(input("ingresar valor: "))
    if valor%2==0:
        par=par+1
    else:
        if valor%2==1:
            impar=impar+1
    x=x+1


print("total numeros pares: ",par)
print("total numeros impares: ",impar)

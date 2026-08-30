equilatero=0
isoceles=0
escaleno=0
n=int(input("ingresar cantidad de triangulos a procesar: "))
for xa in range (n):
    lado1=int(input("ingresar  lado 1 del triangulo ",))
    lado2=int(input("ingresar lado 2 del triangulo "))
    lado3=int(input("ingresar lado 3 del triangulo "))

    if lado1==lado2 and lado1==lado3:
        equilatero=equilatero+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            isoceles=isoceles+1
        else:
            escaleno=escaleno+1

print("cantidad de triangulos de cada tipo equilatero: ",equilatero, " isoceles: ",isoceles," escaleno: ",escaleno)
    

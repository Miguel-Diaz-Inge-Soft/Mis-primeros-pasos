n=int(input("ingresar cantidad de piezas a procesar"))
x=1
cantidad=0
while x<=n:
    largo=float(input("ingresar medidas"))
    if largo >=1.20 and largo<=1.30:
        cantidad=cantidad+1
    x=x+1
print("cantidad de piezas aptas")
print(cantidad)
                
    

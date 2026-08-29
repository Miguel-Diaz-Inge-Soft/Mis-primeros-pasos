cant12=0
n=int(input("ingresar cuantos triangulos se van a procesar"))
for x in range(n):
    base=int(input("ingresar base del triangulo: "))
    altura=int(input("ingresar altura del triangulo: "))
    superficie=(base*altura)/2
    print("datos del triangulo base: ", base," altura: ",altura," superficie: ",superficie) 
    
    if superficie>=12:
        cant12=cant12+1
print("cantidad de triangulos donde su superficie es mayor 12: ",cant12)

cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("ingressr puntos a procesar"))
for f in range (n):
    x=int(input("ngrese coordenada x: "))
    y=int(input("ingrese coordenada y: "))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1

print("cantidad de puntos en el primer cuadrante: ",cant1)
print("cantidad de puntos en el segundo cuadrante: ",cant2)
print("cantidad de puntos en el tercer cuadrante: ",cant3)
print("cantidad de puntos en el cuarto cuadrante: ",cant4)

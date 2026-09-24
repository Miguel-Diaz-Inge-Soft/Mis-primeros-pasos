def cantidad_vocales(palabra):
    palabra1=palabra.lower()
    suma=0
    for x in range (len(palabra1)):
        if palabra1[x]=="a" or palabra1[x]=="e" or palabra1[x]=="i" or palabra1[x]=="o" or palabra1[x]=="u":
            suma=suma+1

    print("Cantidad de vocales que tiene la oración: ", suma)

    
def carga():
    palabra=input("Ingresar oración a calcular: ")
    cantidad_vocales(palabra)
    

#Principal
carga()

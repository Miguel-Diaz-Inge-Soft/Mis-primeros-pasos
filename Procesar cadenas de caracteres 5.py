oracion=input("ingresar oración: ")
oracion1=oracion.upper()
x=0
voc=0

while x<len(oracion1):
    if oracion[x]=="a" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="u":
        voc=voc+1
    x=x+1



print("cantidad de vocales que hay en la oracion: ",voc)

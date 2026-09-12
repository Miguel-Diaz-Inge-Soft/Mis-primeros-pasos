sueldo=[]

for x in range(5):
    valor=int(input(f"Ingresar sueldo {x+1}: "))
    sueldo.append(valor)

print(f"Lista original de los sueldos:  {sueldo}")

for x in range(4):
    if sueldo[x]>sueldo[x+1]:
        aux=sueldo[x]
        sueldo[x]=sueldo[x+1]
        sueldo[x+1]=aux

print(f"Lista nueva: {sueldo} ")

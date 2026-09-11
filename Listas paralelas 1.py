nombres=[]
edades=[]

for x in range(5):
    nombre=input(f"Ingresar el nombre de la persona {x+1}: ")
    nombres.append(nombre)
    edad=int(input(f"Ingresar la edad de la persona {x+1}: "))
    edades.append(edad)

print("Personas mayores de edad: ")

for x in range (5):
    if edades[x]>=18:
        print(f"{nombres[x]} es mayor de edad")
        

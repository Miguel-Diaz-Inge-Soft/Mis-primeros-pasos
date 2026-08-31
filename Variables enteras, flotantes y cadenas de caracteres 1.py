print("datos de la persona: ")
nombre1=input("ingrese nombre de la persona")
edad1=int(input("ingrese edad de la persona"))
estatura1=float(input("ingrese estatura de la persona. ej 1.75"))
print("persona dos: ")
nombre2=input("ingrese nombre de la persona")
edad2=int(input("ingrese edad de la persona"))
estatura2=float(input("ingrese estatura de la persona. ej 1.75"))

print("persona mas alta")
if estatura1>estatura2:
    print(nombre1)
else:
    print(nombre2)

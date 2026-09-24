def retornar_superficie(lado):
    superficie=lado*lado
    return superficie

#principal
lad=int(input("Ingrese lado del cuadrado: "))
superficie=retornar_superficie(lad)
print(f"El área del cuadrado es:  {superficie}")
if retornar_superficie(lad)>80:
    print("La superficie excede el límite")

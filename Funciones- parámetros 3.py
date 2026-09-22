def perimetro(lado):
    perimetro=lado+lado+lado+lado
    print(f"Su perímetro es: {perimetro}")

def superficie(lado):
    superficie=lado*lado
    print(f"Su área es: {superficie}")

def carga():
    lado=float(input("Ingresar lado del cuadrado: "))
    desicion=int(input("Desea conocer 1=Perímetro 2=Área:  (escriba número)  "))
    if desicion==1:
        perimetro(lado)
    if desicion==2:
        superficie(lado)


carga()

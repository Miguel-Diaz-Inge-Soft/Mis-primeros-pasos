def calcular_perimetro_area(lado):
    
    datos=[]
    perimetro=lado*4
    area=lado*lado
    datos.append([perimetro, area])
    return datos

def carga():
    valor=int(input("Ingresar el valor que tiene el lado del cuadrado: "))
    print(f"El valor del perimetro y area es: {calcular_perimetro_area(valor)}")


#PRINCIPAL
carga()


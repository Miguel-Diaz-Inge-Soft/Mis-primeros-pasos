def  presentacion():
    print("programa que permite cargar dos valores por teclado")
    print("Efectua la suma de los valores")
    print("muestre el resultado de la suma")
    print("---------------------------------------------------------------------")

def carga_suma():
    valor1=int(input("Ingrese primer valor: "))
    valor2=int(input("Ingrese segundo valor: "))
    suma=valor1+valor2
    print(f"La suma de los valores es: {suma}")
    print("---------------------------------------------------------------------")

def finalizacion():
    print("Gracias por su participación")

#bloque principal del programa
presentacion()
carga_suma()
finalizacion()

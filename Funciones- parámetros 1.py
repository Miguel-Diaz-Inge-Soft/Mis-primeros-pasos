def mostrar_mensaje(mensaje):
    print("------------------------------------")
    print(mensaje)
    print("------------------------------------")

def suma():
    valor1=int(input("Ingresar primer valor: "))
    valor2=int(input("Ingresar segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es : ",suma)

#Bloque principal
mostrar_mensaje("el programa calcula la suma de dos números")
suma()
mostrar_mensaje("gracias por su participación")

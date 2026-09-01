suma=0
opcion="si"
while opcion=="si":
    valor=int(input("ingrese numero a sumar"))
    suma=suma+valor
    opcion=input("¿desea continuar ingresando numeros? escriba si o no: ")
print("suma de los valores ingresados")
print(suma)


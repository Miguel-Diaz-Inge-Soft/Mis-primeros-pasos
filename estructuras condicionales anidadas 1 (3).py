nu=int(input("ingrese numero a analizar"))

if nu<10:
    print("el numero es de un digito")
else:
    if nu<100:
        print("el numero es de 2 digitos")
    else:
        if nu<1000:
            print("el numero es de tres digitos")
        else:
            print("el numero no esta dentros de los digitos acordados")

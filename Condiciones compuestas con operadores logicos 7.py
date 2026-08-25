equis=int(input("ingresar valor de X distinto a cero :"))
if equis==0:
    print("favor de poner su numero diferente de cero, si no la aplicacion se cerrara (1 intento mas)")
    equis=int(input("ingresar valor de X distinto a cero :"))
ye=int(input("ingresar valor de Y distinto a cero :"))
if ye==0:
    print("favor de poner su numero diferente de cero, si no la aplicacion se cerrara (1 intento mas)")
    ye=int(input("ingresar valor de Y distinto a cero :"))

if equis>0 and ye>0:
    print("se encuentra en el primer cuadrante")
else:
    if equis<0 and ye<0:
        print("se encuentra en el tercer cuadrante")
    else:
        if equis<0:
            print("se encuentra en el segundo cuadrante")
        else:
            print("se encuentra en el cuarto cuadrant")

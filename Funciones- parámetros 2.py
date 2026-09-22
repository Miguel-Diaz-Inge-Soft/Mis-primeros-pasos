def mayor(v1,v2,v3):
    print("El mayor de los tres números es: ")
    if v1>v2 and v2>v3:
        print(v1)

    elif v2>v3 and v2>v1:
        print(v2)

    elif v3>v2 and v3>v1:
        print(v3)

def carga() :
    valor1=int(input("Ingresar primer número: "))
    valor2=int(input("Ingresar segundo número: "))
    valor3=int(input("Ingresar tercer número: "))
    mayor(valor1,valor2,valor3)


#Principal
carga()

nu1=int(input("ingresar el primer valor :"))
nu2=int(input("ingresar el segundo valor :"))
nu3=int(input("ingresar tercer valor :"))

if nu1>nu2 and nu1>nu3:
    print(nu1 , " es el mayor")
else:
    if nu2>nu1 and nu2>nu3:
        print(nu2, " es el mayor")
    else:
        print(nu3," es mayor)")

if nu1<nu2 and nu1<nu3:
    print(nu1, " es el menor")
else:
    if nu2<nu1 and nu2<nu3:
        print(nu2," es el menor")
    else:
        print(nu3," es el menor")

sueldo=int(input("ingresar sueldo del operario :"))
antigue=int(input("ingresarantiguedad del operario en años :"))

if sueldo<500 and antigue>=10:
    aumento=sueldo*0.20
    totalsueldo=aumento+sueldo
    print("el total de su sueldo es de :",totalsueldo)
else:
    if antigue<10:
        aumento=sueldo*0.05
        totalsueldo=aumento+sueldo
        print("el total de su sueldo es de :",totalsueldo)
    else:
        print("no hay cambios en su salario")

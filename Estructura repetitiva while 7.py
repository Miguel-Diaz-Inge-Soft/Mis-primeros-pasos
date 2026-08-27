n=int(input("ingresar cantidad de  empleados que trabajan"))
x=1
sueldo1=0
sueldo2=0
total=0
while x<=n:
    sueldobase=int(input("ingresar el sueldo del operario"))
    if sueldobase<=300:
        sueldo1=sueldo1+1
        total=total+sueldobase
    else: 
        sueldo2=sueldo2+1
        total=total+sueldobase
    x=x+1
print("total del sueldo: ",total)
print(sueldo1, " sueldos son en rango de 100 a 300")
print(sueldo2, "sueldos son mayor a 300")


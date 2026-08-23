no1=int(input("ingrese primer nota del alumno: "))
no2=int(input("ingrese segunda nota del alumno: "))
no3=int(input("ingrese tercer nota del alumno: "))
prom=(no1+no2+no3)/3
if prom>=7:
    print("aprobado")
else:
    if prom>=4:
        print("esta enla cuerda floja")
    else:
        print("esta reprobadisimo")

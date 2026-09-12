alumnos=[]
notas=[]
suma1=0
suma2=0
suma3=0

n=int(input("Ingresar cantidad de alumnos a pocesar: "))

for x in range(n):
    alumno=input(f"Ingresar nombre del alumno {x+1}: ")
    alumnos.append(alumno)
    nota=int(input(f"Ingresar nota del amuno {x+1}: "))
    notas.append(nota)


for x in range(len(notas)):
    if notas[x]>=8:
        suma1=suma1+1
        print(f"{alumnos[x]}: excelente")
    elif notas[x]>=5:
        suma2=suma2+1
        print(f"{alumnos[x]}: regular")
    else:
        notas[x]>=0
        suma3=suma3+1
        print(f"{alumnos[x]}: reprobado")

print("Cantidad de alumnos: ")
print(f"Excelente: {suma1}")
print(f"Regular: {suma2}")
print(f"Reprobado: {suma3}")

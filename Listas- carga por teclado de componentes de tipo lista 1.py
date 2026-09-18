#Se crea y carg una lista con los nombres de alumnos N. Cada alumno tiene dos notas, almacenar
#los notas en un lista paralela. Cada componente de la lista paralela debe ser tambien una lista con
#las dos notas. Imprimir luego cada nombre y sus notas

nombres=[]
notas=[]
n=int(input("¿Cuántos alumnos registrará? "))

for x in range(n):
    nombre=input(f"Ingresar nombre del alumno {x+1}: ")
    nombres.append(nombre)
    nota1=int(input("Ingresar primer nota: "))
    nota2=int(input("Ingresar segunda nota: "))
    notas.append([nota1,nota2])

for x in range(n):
    print(nombres[x], notas[x][0], notas[x][1])

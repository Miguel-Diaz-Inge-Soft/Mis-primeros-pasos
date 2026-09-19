paises=[]
temp=[]

temptris=[]

for x in range(4):
    pais=input(f"Ingresar país número {x+1}: ")
    paises.append(pais)
    temp1=int(input(f"Ingresar primer temperatura media de {pais}: "))
    temp2=int(input(f"Ingresar segunda temperatura media de {pais}: "))
    temp3=int(input(f"Ingresar tercer temperatura media de {pais}: "))
    temp.append([temp1,temp2,temp3])
    

    
print("Países y temperaturas")
print(paises)
print(temp)

suma=0
for k in range(4):
    for x in range(3):
        suma=suma+temp[k][x]

    promedio=suma/3
    temptris.append(promedio)
    suma=0
print(paises)
print(temptris)

if temptris[0]>temptris[1] and temptris[0]>temptris[2] and temptris[0]>temptris[3]:
    print(f"País con mayor temperatura trimestral {paises[0]} {temptris[0]}")
elif temptris[1]>temptris[0] and temptris[1]>temptris[2] and temptris[1]>temptris[3]:
    print(f"País con mayor temperatura trimestral {paises[1]} {temptris[1]}")
elif  temptris[2]>temptris[0] and temptris[2]>temptris[1] and temptris[2]>temptris[3]:
    print(f"País con mayor temperatura trimestral {paises[2]} {temptris[2]}")
elif temptris[3]>temptris[0] and temptris[3]>temptris[1] and temptris[3]>temptris[2]:
    print(f"País con mayor temperatura trimestral {paises[3]} {temptris[3]}")

    

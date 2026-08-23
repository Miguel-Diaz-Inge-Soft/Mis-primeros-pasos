canp=int(input("ingresar cantidad de preguntas realizadas"))
canb=int(input("ingresar cantidad de preguntas buenas que se contestaron"))

por=(canb/canp)*100

if por>=90:
    print("nivel maximo")
else:
    if por>=75:
        print("nivel medio")
    else:
        if por>=50:
            print("nivel regular")
        else:
            print("fuera de serie")
        

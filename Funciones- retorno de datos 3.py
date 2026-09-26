def determinar_cadenas(lista):
    igual="Las dos cadenas tienen mismos caracteres"
    if len(lista[0])>len(lista[1]):
        return lista[0]
    elif len(lista[0])==len(lista[1]):
        return igual
    else:
        return lista[1]
    
def carga():
    cadenas=[]
    for x in range(2):
        palabra=input(f"Ingresar cadena N° {x+1}: ")
        cadenas.append(palabra)

    determinar_cadenas(cadenas)

    print(f"La cadena con mas caracteres es: {determinar_cadenas(cadenas)}")


#PRINCIPAL
carga()
carga()
    
        

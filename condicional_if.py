#---condicional if/elif/else----
#Estructura del condicional IF:
if True : 
    print("Se ejecuta la instrucción")

#Ejemplo if 
edad=24
if edad>18:
    print("Eres un adulto")
else:
    print("Eres joven")

#Estructura del ELIF
if False:
    print("la primera condicion")
elif True:
    print("segunda condicion")
elif False:
    print("tercera condicion")
else:
    print("Todas son falsas")

#EJERCICIO: CLASIFICACION DE EDAD
edad =100
if edad <18: #false
    print("Eres menor de edad")
elif  edad>=18 and edad<65: #true 
    print("eres un adulto")
else:
    print("eres un adulto mayor")

#estructura condicional anidada 

if True:
    if False:
        print("se ejecuta la instruccion")
    elif True:
        print("No se ejecuta la instruccion")
    else:
        print("No se ejecuta la instruccion")
else:
    print("no se ejecuta la instruccion")

#Ejercicio: clasificacion de edad If anidado
edad=100
if edad<18:
    if edad >12 and edad <18:
        print("Eres adolecente")
    else:
        print("Eres un niño")
else:
    if edad >=18 and edad <60:
        print("Adulto")
    else:
        print("Adulto Mayor")

#Ejercicio del partido con if:
marcador_colombia=int(input("ingrese el marcador de Colombia "))
marcador_chile=int(input("Ingrese el marcador de Chile "))
if marcador_colombia>marcador_chile:
    print("Colombia es el mejor y por eso ganó")
elif marcador_colombia==marcador_chile:
        print("quedamos empatados")
else:
    print("perdimos el partido")

#Operador ternario

numero=4
if numero % 2 == 0:
    print("El numero es par")
else:
    print("el numero es impar")

print("el numero es par" if numero % 2 == 0 else "el numero es impar")


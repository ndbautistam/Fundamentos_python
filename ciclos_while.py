# CICLOS WHILE

#BUCLE INFINITO:

"""
while True:
print("Llenando Memoria RAM")
"""

#Estructura de un WHILE

i = 1 #Inicializar la Variable de Control
while i < 6: # Condincion
    print(f"Bloque Codigo: {i}")
    i +=1 #Incrementar la Variable de Control

#EJERCICIO: VALIDAR SI ES MENOR DE EDAD

edad = 16

while edad < 18:
    print(f"Eres menor de edad, porque tienes {edad} años")
    edad +=1
else:
    print("Eres mayor de edad, porque tienes mas de 18 años")
    
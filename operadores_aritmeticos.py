#---OPERADORES ARITMÉTICOS----

a=10
b=3
#suma
suma= a + b
print(f"la suma de {a} y  {b} es: {suma}")

#resta 

resta = a - b
print(f"la resta de {a} y {b} es {resta}")

#Multiplicacion 
multiplicacion=a*b
print(f"la multiplicacion de {a} y {b} es {multiplicacion}")

#division
division=a/b
print(f"la division de {a} y {b} es {division}")

#divion sin decimales
division_1=a//b
print(f"la division entera de {a} y {b} es {division_1}")

#Modulo o residuo
modulo= a%b
print(f"el modulo de {a} y {b} es {modulo}")

#exponenciacion
potencia = a**b
print(f"la potencia de {a} y {b} es {potencia}")

#----PRECEDENCIA DE OPERADORES----
resultado = a+b*2
print(f"el resultado de la operacion 10+3*2 es:{resultado}") 

#Para cambia el orden 
resultado_2= (10+3)*2
print(f"el resultado de la operacion (10+3)*2 es {resultado_2}")

resultado_3=10*3//3
print(f"el resultado da {resultado_3}")

ejercicio = ((a+b)*(a-b)/(a*b))-((a**b)%3)
print(f"el resultado del ejercicio es {ejercicio}")

#----LIBRERIAS EN PYTHON----
import math

print(math.pi)
print(math.e)
print(math.sqrt(16))

import random
print(random.random())# Numero aleatorio entre 0 y 1

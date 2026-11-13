print("Hello word")
#Tipo de escritura de las variables 

#camelCase
aprendizSena= "sena"

#PascalCase
AprendizSena= "sena"

#snake_case - Vamos a usar este
aprendiz_sena= "sena"

#Reglas de las variables:
nombre_Completo_1="Dayana"

#---TIPOS DE DATOS PRIMITIVOS---
nombre= "Dayana"
print(type(nombre))

edad=32
print(type(edad))

estatura=1.61
print(type(estatura))

activo= True
print(type(activo))

complejo = 2+3j
print(type(complejo))

byte =b"HOLA"
print(type(byte))#bytes

nulo =None 
print(type(nulo))

#-----TIPOS DE DATOS ESTRUCTURAS----
lista= ["python", "js"]
print(type(lista))#list

conjunto={"Html","css"}
print(type(conjunto))#set 

tupla=("Java", "C#")
print(type(tupla))

diccionario={"Nombre":"Andres","Edad" :23}
print(type(diccionario))

#----Conversión de tipos de datos o casteo----
#Casteo de entero a texto
telefono = 3001687718#int
print(type(telefono),telefono)

telefono_str= str(telefono)#string
print(type(telefono_str),telefono_str)


#Casteo de texto a entero
cedula="1193078386"#string
print(type(cedula),cedula)

cedula_int=int(cedula)#Entero
print(type(cedula_int),cedula_int)


#casteo de Buleano a entero
matriculado=False
print(type(matriculado))#bool

matriculado_int= int(matriculado)#Entero
print(type(matriculado_int),matriculado_int)


#casteo de decimal a entero
promedio=4.13
print(type(promedio),promedio)

promedio_int= int(promedio)#Entero borra las decimas 
print(type(promedio_int),promedio_int)


#Casteo de entero a decimal 
edad=24
print(type(edad),edad)#int

edad_float=float(edad)#float
print(type(edad_float),edad_float)


#Casteo de entero a boooleano
activo=0
print(type(activo))#int

activo_bool=bool(activo)
print(type(activo_bool),activo_bool)#bool


#Ejemplos locos
edad_sami=6
print(type(edad_sami),edad_sami)

edad_sami_float=float(edad_sami)
print(type(edad_sami_float),edad_sami_float)



# casteo de entero a decimal
promedio = 4.13
print(type(promedio), promedio)# float

promedio_int =int(promedio)
print(type(promedio_int), promedio_int)#entero

#casteo de entero a decimal

edad = 26
print(type(edad),edad) #int

edad_float = float(edad)
print(type(edad_float),edad_float) #float

#casteo de un booleano a un flotante o decimal

beneficio = True
print(type(beneficio), beneficio)# bool

beneficio_float = float(beneficio)
print(type(beneficio_float),beneficio_float)#float

# casteo de decimal a booleANO

descuento = 10.5
print(type(descuento),descuento)#float

descuento_bool = bool(descuento)
print(type(descuento_bool),descuento_bool) # bool

# este es un comentario de una sola linea
"""este es un comentario de varias lineas que se utiliza para esplicar el codigo de manera mas detallada"""

# LA IDENTACION EN PYTHON ---------

# condicional if

if 5 > 2:
    print("5 es mayor que 2")
    
else:
    print("5 no es mayor que 2")
    

# INPUT: ENTRADA DE DATOS

nombre_completo = input("Ingrese tu nombre completo: ")
programa = input("¿Cuál es tu programa de formación? ")

# OUTPUT: SALIDA DE DATOS

print("Hola " + nombre_completo + " Bienvenido al curso de Python")

print("Hola mi nombre es: ", nombre_completo, "y estoy en el programa de: ", programa)

# IMPRESION CON F-STRING

print(f"Hola mi nombre es {nombre_completo}, y estoy en el programa de: {programa}")

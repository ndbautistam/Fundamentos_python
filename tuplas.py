# TUPLAS

# Estructura de una Tupla

# Indice:     0             1             2 
tupla = ("elemento_1", "elemento_2", "elemento_3")
print(type(tupla)) # <class 'tuple'>

tupla_2 = "a", "b", "c"
print(type(tupla_2)) #<class 'tuple'>

tupla_3 = ("Hola",)
print(type(tupla_3))  #<class 'tuple'>

tupla_4 = tuple("Hola")
print(tupla_4) # ('H', 'o', 'l', 'a')
print(type(tupla_4))

tupla_mixta = ("Hola", 123, 3.14, True, [1,2,3])
print(tupla_mixta)


# TUPLAS DE APRENDICES SENA ADSO 3233140

# Indice:        0        1        2       3        4         5
aprendices = ("Dayana", "Jhon", "Oscar", "Luis", "Pepito", "Jhon")
print(aprendices)

# Acceder a un Elemento de la Tupla
print(aprendices[2]) # Oscar

# Modificar un Elemto de la Tupla: Esto generará un error porque las tuplas son inmutables

# aprendices[0] = "Diana"

#Consultar Rangos de Elementos en las Tuplas
print(aprendices[0:2]) # ('Dayana', 'Jhon')
print(aprendices[1:4]) # ('Jhon', 'Oscar', 'Luis')
print(aprendices[1:]) # ('Jhon', 'Oscar', 'Luis', 'Pepito')

#CONCATENAR TUPLAS +
tupla_uno = (1,2,3)
tupla_dos = (4,5,6)

tupla_suma = tupla_uno + tupla_dos
print(tupla_suma) # (1, 2, 3, 4, 5, 6)

# MULTIPLICAR UNA TUPLA
tupla_multiplicada = tupla_uno * 3
print(tupla_multiplicada) # (1, 2, 3, 1, 2, 3, 1, 2, 3)


# METODOS DE LAS TUPLAS ------------

# MEDIR LA LONGITUD DE UNA TUPLA .len()
print(len(aprendices)) # 5

#CONTAR ELEMENTOS REPETIDOS EN UNA TUPLA .count()
print(aprendices.count("Jhon")) # 2 veces

#OBTENER EL INDICE DE UN ELEMENTO .index()
print(aprendices.index("Dayana")) # Indice 0


# MODIFICAR UNA TUPLA CONVIRTIENDOLA EN LISTA
lenguajes = ("HTML", "CSS", "JavaScript")
print(lenguajes) #()
print(type(lenguajes)) # <class 'tuple'>

lista_lenguajes = list(lenguajes) #Casteo
print(lista_lenguajes) # []
print(type(lista_lenguajes)) # <class 'list'>

lista_lenguajes.append("Python") # Agregar Elemento
print(lista_lenguajes) #['HTML', 'CSS', 'JavaScript', 'Python']

lenguajes = tuple(lista_lenguajes) #Casteo a Tupla nuevamente
print(lenguajes) # (, "Python")
print(type(lenguajes)) #<class 'tuple'>

# COMPROBACION DE PERTENECIA CON "IN" Busqueda
print("Python" in lenguajes) #True
print("C++" in lenguajes) # False

if "HTML" in lenguajes:
    print("HTML fue encontrado en la Tupla")
else:
    print("HTML NO fue encontrado en la Tupla")


# EMPAQUETAR TUPLAS

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "Topografia"

tupla_programas = (programa_1, programa_2, programa_3) #Empaquetar
print(tupla_programas) # ('ADSO', 'SST', 'Topografia')
print(type(tupla_programas)) #<class 'tuple'>


# DESEMPAQUETAR TUPLAS

tupla_ciudades = ("Duitama", "Sogamoso", "Tunja")

ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades # Desempaquetar

print(ciudad_1) #Duitama
print(ciudad_2) #Sogamoso
print(ciudad_3) #Tunja

# Iterar o Recorrer una TUPLA "FOR"
for ciudad in tupla_ciudades:
    print(ciudad)
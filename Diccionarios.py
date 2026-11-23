# DICCIONARIOS

#Estructura de un Diccionario

diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"    
}
print(type(diccionario)) #<class 'dict'>

#Diccionario vacio
diccionario_vacio = {}
print(type(diccionario_vacio)) #<class 'dict'>

# Diccionario con Elementos
diccionario_aprendiz = {
    "nombre": "Felipe",
    "apellido": "Sandoval",
    "programa": "ADSO",
    "ficha": "3233140",
    "edad": 32
}

print(diccionario_aprendiz)

# Obtener un valor del Diccionario por la Clave

print(diccionario_aprendiz["programa"]) # ADSO
# print(diccionario_aprendiz["correo"]) # Key Error

print(diccionario_aprendiz.get("programa")) #ADSO
print(diccionario_aprendiz.get("correo")) # None

# Obtener solo las Claves del Diccionario .keys()
print(diccionario_aprendiz.keys())
# dict_keys(['nombre', 'apellido', 'programa', 'ficha', 'edad'])

# Obtener solo los valores del Dicionario .values()
print(diccionario_aprendiz.values())
# dict_values(['Felipe', 'Sandoval', 'ADSO', '3233140', 32])

# Obtener la clave y el valor .items()
print(diccionario_aprendiz.items())
# dict_items([('nombre', 'Felipe'), ('apellido', 'Sandoval'), ('programa', 'ADSO'), ('ficha', '3233140'), ('edad', 32)])


#Agregar o crear un nuevo Elemento al Diccionario
diccionario_aprendiz["correo"] = "afsandoval@sena.edu.co"
print(diccionario_aprendiz) # {'correo': 'afsandoval@sena.edu.co'}

# Modificar un valor del Diccionario
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz) # {'programa': 'SST'}

# Metodo UPDATE() para Actualizar un valor
diccionario_aprendiz.update({"nombre": "Andres"})
print(diccionario_aprendiz) # {"nombre": "Andres"}

# Agregar un nuevo Elemento con Update()
diccionario_aprendiz.update({"ciudad": "Duitama"}) 
print(diccionario_aprendiz) # {'ciudad': 'Duitama'}

#Eliminar un Elemento del Diccionario

# Elimina el Ultimo Elemento .popitem()
diccionario_aprendiz.popitem()
print(diccionario_aprendiz) # Eliminio {'ciudad': 'Duitama'}

# Eliminar un Elemento Especifico .pop()
diccionario_aprendiz.pop("edad")
print(diccionario_aprendiz)

# Eliminar Todos los Elementos del Diccionario con .clear()
# diccionario_aprendiz.clear()
# print(diccionario_aprendiz)

# Comprobar la Pertenecia con "IN" Busqueda
print("ficha" in diccionario_aprendiz) # True
print("telefono" in diccionario_aprendiz) # False

if "ficha" in diccionario_aprendiz:
    print("La Clave ficha esta dentro del Diccionario")
else:
    print("La Clave ficha NO esta dentro del Diccionario")
    
# Recorrer un Diccionario con el Ciclo FOR

# 1. Recorrer solo las Claves del Diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)
    
# 2. Recorrer solo los Valores del Diccionario
for valor in diccionario_aprendiz.values():
    print(valor)
    
# 3. Recorrer las Claves y Valores del Diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave} : {valor}")
    

#DICCIONARIOS ANIDADOS --------

aprendices = {
    "aprendiz_1": {
        "nombre": "James",
        "apellido": "Rodriguez",
        "programa": "ADSO"
    },
    "aprendiz_2" : {
        "nombre": "Falcao",
        "apellido": "Garcia",
        "programa": "SST"
    },
    "aprendiz_3" : {
        "nombre": "Lucho",
        "apellido": "Diaz",
        "programa": "Minas"
    }
}

# Acceder a un valor de un Diccionario Anidado
print(aprendices["aprendiz_2"]["programa"]) # SST

# Recorrer un Diccionario Anidado con Ciclo FOR
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
#--LISTAS---

#Estructura de una lista 

lista=["Dato_1","Dato_2","Dato_3"]
print(type(lista)) #class list 

#Lista Mixta
listamixta=["Hola",123,3.14,True,["Adso","sst"]]

#LISTA DE APRENDICES SENA ADSO 3233140

aprendices=["Miguel","Sebastian","Lizeth","Oscar","John"]
print(aprendices)

#Acceder a un elemento de la lista 
print(aprendices[2])#Lizeth

#Modificar un elemento de la lista 
aprendices[0]= "Luis"
print(aprendices)

#consultar Rangos de elementos de la lista 

print(aprendices[0:2])#[luis, sebastian, Migel]
print(aprendices[2:4])
print(aprendices[0::2])

#concatenar listas 
programas_tecnicos=["Sistemas Teleinformáticos","Redes"]
programas_tecnologicos=["ADSO","Topografia"]
programas_SENA= programas_tecnicos+programas_tecnologicos
print(programas_SENA)#se unen los dos

#Extender listas con .extend()
nuevos_programas_tecnicos= ["Inteligencia Artificial","Mineria de Datos","Redes"]
programas_tecnicos.extend(nuevos_programas_tecnicos)
print(programas_tecnicos)#se agregan los nuevos datos 

#Medir la longitud de una lista usando el operador .len()
print(len(programas_tecnicos))#4 elementos tiene la lista
print(len(programas_tecnologicos))#2 elementos tiene 

#contar o buscar elementos repetidos en una lista
print(programas_tecnicos)
print(programas_tecnicos.count("Redes"))#se repite dos veces "Redes" en la lista

#obtener el indice de un elemento .index
print(aprendices.index("Lizeth"))
print(programas_tecnicos.index("Mineria de Datos"))
print(programas_tecnologicos.index("ADSO"))

#Copiar una lista .copy()
nueva_lista_aprendices = aprendices.copy()
print(nueva_lista_aprendices)

#Agregar nuevos elementos a la que copie con la funcion .append()
nueva_lista_aprendices.append("Adriana")
nueva_lista_aprendices.append("Diana")
print(nueva_lista_aprendices)

#Agregar un nuevo elemento en una posición del indice .insert()
nueva_lista_aprendices.insert(1, "Dayana")
print(nueva_lista_aprendices)

#Eliminar un elemento de la lista 
#.remove() Elimina la primera ocurrencia de la lista
nueva_lista_aprendices.remove("Oscar")
print(nueva_lista_aprendices)

#.pop Elimina segun el indice
nueva_lista_aprendices.pop(0)
print(nueva_lista_aprendices)

#.clear() Limbia o borra todos los elementos de la lista 
#nueva_lista_aprendices.clear()
#print(nueva_lista_aprendices)

#Ordenar la lista
#A-Z Ascendentemente .sort()
nueva_lista_aprendices.sort()
print(nueva_lista_aprendices)

#Ordenar descendentemente Z-A .reverse()
nueva_lista_aprendices.reverse()
print(nueva_lista_aprendices)

#Buscar elementos en la lista con el operador "in"
if "Diana" in nueva_lista_aprendices:
    print("Diana se encontró en la lista de aprendices")
else: 
    print("Diana no se encontró en la lista de aprendices")
busqueda= "Diana" in nueva_lista_aprendices
print(busqueda)#True
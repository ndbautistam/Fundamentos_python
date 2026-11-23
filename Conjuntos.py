#---CONJUNTOS----

#Estructura básica de un conjunto

conjunto={"elemento_1","elemento_2","elemento_3"}
print(type(conjunto))

conjunto_2=set()
print(type(conjunto_2))

conjunto_3={}
print(type(conjunto_3))

#Crear un conjunto
programas={"ADSO","SST","mineria","ADSO","SST"}
print(type(programas))

#---Metodos de conjunto---

frutas = {"mango", "guayaba","mora"}

#agregar un nuevo elemento al conjunto

frutas.add("fresas")
print(frutas)

frutas.add("mora")#elemento duplicado asi que no lo agrega 

#Eliminar un elemento del conjunto



# ACTIVIDAD 3: GESTION DE LISTA DE REPRODUCCION MUSICAL

# 1. Crear una lista con 5 canciones
canciones = ["Flowers", "Anti-Hero", "As It Was", "Dance The Night", "Levitating"]

print("Lista inicial:")
print(canciones)


# 2. Agregar una cancion al final con append()
canciones.append("Blinding Lights")
print("\nDespues de append():")
print(canciones)


# Agregar una cancion en la segunda posicion con insert()
canciones.insert(1, "Cruel Summer")
print("\nDespues de insert():")
print(canciones)


# Agregar dos canciones con extend()
canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("\nDespues de extend():")
print(canciones)


# 3. Eliminar una cancion por su nombre con remove()
canciones.remove("Anti-Hero")
print("\nDespues de remove():")
print(canciones)


# Eliminar la ultima cancion con pop()
eliminada = canciones.pop()
print("\nCancion eliminada con pop():")
print(eliminada)

print("Lista despues de pop():")
print(canciones)


# 4. Ordenar las canciones alfabeticamente
canciones.sort()
print("\nLista ordenada alfabeticamente:")
print(canciones)


# 5. Responder las preguntas usando metodos

# Cuantas canciones tiene la playlist
print("\nCantidad de canciones:")
print(len(canciones))

# En que posicion esta la primera cancion agregada
print("\nPosicion de Blinding Lights:")
print(canciones.index("Blinding Lights") + 1)

# Cuantas veces aparece Bonus Track 1
print("\nVeces que aparece Bonus Track 1:")
print(canciones.count("Bonus Track 1"))

# Actividad 2: Analisis de Temperaturas Semanales

# 1. Crear la lista de temperaturas de los 14 dias
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 2. Imprimir temperaturas usando indices positivos y negativos
print("ANALISIS DE TEMPERATURAS")


print("Temperatura del primer dia:", temperaturas[0])
print("Temperatura del ultimo dia:", temperaturas[-1])

print("Temperatura del dia 7:", temperaturas[6])
print("Temperatura del dia 7 usando indice negativo:", temperaturas[-8])

print("Temperatura del penultimo dia:", temperaturas[12])
print("Temperatura del penultimo dia usando indice negativo:", temperaturas[-2])

# 3. Utilizar slicing para obtener diferentes partes de la lista

primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]
dias_pares = temperaturas[1::2]
temperaturas_invertidas = temperaturas[::-1]

print("\nPrimera semana:")
print(primera_semana)

print("Segunda semana:")
print(segunda_semana)

print("Temperaturas de los dias pares:")
print(dias_pares)

print("Temperaturas en orden invertido:")
print(temperaturas_invertidas)

# 4. Calcular el promedio de cada semana

promedio_semana1 = sum(primera_semana) / len(primera_semana)
promedio_semana2 = sum(segunda_semana) / len(segunda_semana)

print("\nPROMEDIO DE TEMPERATURAS")


print("Promedio de la primera semana:", promedio_semana1)
print("Promedio de la segunda semana:", promedio_semana2)

# 5. Comparar los promedios de las dos semanas

if promedio_semana1 > promedio_semana2:
    print("La primera semana tuvo mayor temperatura promedio.")

elif promedio_semana2 > promedio_semana1:
    print("La segunda semana tuvo mayor temperatura promedio.")

else:
    print("Las dos semanas tuvieron la misma temperatura promedio.")

#  ACTIVIDAD 3: Clasificador de IMC

print("=" * 48)
print("     CLASIFICADOR DE ÍNDICE DE MASA CORPORAL")
print("=" * 48)

# PASO 1: Solicitar los datos al usuario
peso    = float(input("\nIngresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))


# BONUS: Validar que los valores sean positivos
if peso <= 0 or estatura <= 0:
    print("\n Error: el peso y la estatura deben ser valores positivos mayores que cero. Por favor, reinicia el programa e intenta de nuevo.")
else:
    # PASO 2: Calcular el IMC
    imc = peso / (estatura ** 2)
    
    if imc < 18.5:
        clasificacion = "Bajo peso"
        consejo = "Se recomienda consultar un médico o nutricionista."
        icono = "🔵"
    elif imc < 25.0:                  # Implícitamente: >= 18.5 y < 25.0
        clasificacion = "Normal"
        consejo = "¡Excelente! Mantén tus hábitos saludables."
        icono = "🟢"
    elif imc < 30.0:                  # Implícitamente: >= 25.0 y < 30.0
        clasificacion = "Sobrepeso"
        consejo = "Se sugiere mejorar la dieta e incrementar la actividad física."
        icono = "🟡"
    else:                             # Implícitamente: >= 30.0
        clasificacion = "Obesidad"
        consejo = "Es importante consultar a un profesional de la salud."
        icono = "🔴"


    # PASO 4: Mostrar los resultados con formato legible
    print("\n" + "=" * 48)
    print("                  RESULTADO")
    print("=" * 48)
    print(f"  Peso ingresado:   {peso:.1f} kg")
    print(f"  Estatura:         {estatura:.2f} m")
    print(f"  IMC calculado:    {imc:.2f}")
    print("-" * 48)
    print(f"  Clasificación:    {icono}  {clasificacion}")
    print(f"  Consejo:          {consejo}")
    print("=" * 48)
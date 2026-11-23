# SENTENCIA MATCH -> SWITCH

#MATCH - Dias de la semana

""" dia = int(input("Ingrese el numero del Día de la Semana: "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dia incorrecto")
        
"""
        
        
#EJERCICIO: FALTAS APRENDIZ SENA

falta_aprendiz = input("Ingrese la Falta del aprendiz: ").lower() # Convertir Texto minuscul

match falta_aprendiz:
    case "comer":
        print("Llamado de Atención por Comer en Formacion")
    case "inpuntualidad":
        print("Llamado de Atencion por Llegar Tarde")
    case "uniforme":
        print("Llamado de Atencion por NO portar el uniforme")
    case "jugar":
        print("Llamado de atención por Jugar durante la Formación")
    case _:
        print("Aprendiz Sin Faltas")
        
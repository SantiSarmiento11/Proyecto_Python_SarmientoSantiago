from calcular_totales import * 
from datetime import *
from mover_alertas import *
from Obtener_fecha_actual import *

def porcentaje_alerta_diaria(gastos):

    dias = 1
    total_diario=calcular_total_gastos(gastos, dias)
    porcentaje = 500000
    hoy = obtener_fecha()


    if total_diario > porcentaje:
        print("Superaste el porcentaje de gasto de hoy")
        print("Fecha de superacion del porcentaje: ", hoy)

        alerta = {
        "tipo": "diaria",
        "fecha":hoy,
        "porcentaje": porcentaje,
        "gastado": total_diario
        }

        alertas = json_a_datos()

        alertas.append(alerta)
        guardar_a_json(alertas) 
    else:
        print("")

def porcentaje_alerta_semanal(gastos):

    dias = 7
    total_semanal=calcular_total_gastos(gastos, dias)
    porcentaje = 3000000
    hoy= obtener_fecha()
    ahora=obtener_fecha()


    if total_semanal > porcentaje:
        print("Superaste el porcentaje de gasto de esta semana")
        print(f"Fecha de superacion del porcentaje: {hoy}")

        alerta = {
        "tipo": "semanal",
        "fecha": obtener_fecha(),
        "porcentaje": porcentaje,
        "gastado": total_semanal
        }

        alertas = json_a_datos()

        alertas.append(alerta)
        guardar_a_json(alertas)
    else:  
        print("")



    
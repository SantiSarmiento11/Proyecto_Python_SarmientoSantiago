import json
import os
import mover_gastos as mg
from registro_datos import registro_datos
import listar_gastos
from calcular_totales import *
import reporte as r

ARCHIVO_GASTOS_JSON = "archivo.json"
#desde main voy a correr mi menu principal, desde aca llamare a las funciones principales para ejecutar mi menu
#le pregunto al usuario que funcion quiere realizar y llamo la funcion.
def menu_principal():
    while True:
        
        gastos = mg.json_a_datos()
        
        print("/n==========Administrador de Gastos==========")
        print("Que proceso deseas realizar?")
        print("Escribe 1 para registrar un nuevo gasto")
        print("Escribe 2 para Para listar los gastos")
        print("Escribe 3 para calcular los gastos totales")
        print("Escribe 4 para generar reporte")
        print("5 para salir")
        opcion = int(input("Dame la opcion: "))

        if opcion == 1:
            registro_datos(gastos)
        if opcion == 2:
            listar_gastos.listar_gastos(gastos)
        if opcion == 3:
            calcular_gastos(gastos)
        if opcion == 4:
            r.generar_reporte(gastos)
        if opcion == 5:
            break

if __name__ == "__main__":
    menu_principal()

    


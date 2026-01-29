from tabla_gastos import mostrar_tabla_gastos
import json
from datetime import datetime


#esta funcion al reccorer gasto por gasto busca el valor de la clave categoria y si corresponde con la que da
#el usuario se guarda
def filtrar_gastos_por_categoria(gastos, categoria):
    return [g for g in gastos if g["categoria"] == categoria.lower()]


#Aca al poner una fecha de cada gasto en una variable, puedo validar si esa fecha esta o no
#dentro del periodo de tiempo, si esta guarda el gasto
def filtrar_por_fecha(gastos, fecha_inicio, fecha_fin):

    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    
    resultado = []
    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        if inicio <= fecha_gasto <= fin:
            resultado.append(gasto)
    return resultado


#Este es un menu que me ayudara a saber que quiere el usuario
#con esto llamo las funciones anteriores y las uso para listar los gastos
def listar_gastos(gastos):
    if not gastos:
        print("\n No hay gastos registrados.")
        return

    while True:
        print("\n=============================================")
        print("Listar Gastos")
        print("=============================================")
        print("1. Ver todos los gastos")
        print("2. Filtrar por categoría")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")

        opcion = input("Opción: ").strip()

        #Utilizo la funcion mostra tabla con tabulate para mostrar los gastos ya listados
        if opcion == "1":
            mostrar_tabla_gastos(gastos)
        if opcion == "2":
            categoria = input("Dame la categoria a filtrar: ").strip()
            if not categoria:
                print("Categoria necesaria")
                continue
            gastosxcategoria = filtrar_gastos_por_categoria(gastos, categoria)
            if gastosxcategoria:
                mostrar_tabla_gastos(gastosxcategoria)
            else:
                print(f" No se encontraron gastos en la categoría: '{categoria}'.")
        if opcion == "3":
            try:
                inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
                fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
                
                gastos_fecha = filtrar_por_fecha(gastos, inicio, fin)
                if gastos_fecha:
                    mostrar_tabla_gastos(gastos_fecha)
                else:
                    print("No se encontraron gastos en ese rango de fechas")
            except ValueError:
                print("Formato de fecha inválido")
        
        if opcion == "4":
            break



           





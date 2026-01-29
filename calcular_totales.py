from datetime import *
from tabulate import tabulate

def calcular_total_gastos(gastos, dias=None):
    if not gastos:
        return 0.0

    hoy = datetime.now()
    total = 0.0

    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")

        if dias is None:
            total += gasto["monto"]
        elif dias == 0 and fecha_gasto.date() == hoy.date():
            total += gasto["monto"]
        elif dias and hoy - fecha_gasto <= timedelta(days=dias):
            total += gasto["monto"]

    return total


# Calcula el total por categoría
def calcular_totales_por_categoria(gastos, dias=None):
    categorias = {}
    hoy = datetime.now()

    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        incluir = False

        if dias is None:
            incluir = True
        elif dias == 0 and fecha_gasto.date() == hoy.date():
            incluir = True
        elif dias and hoy - fecha_gasto <= timedelta(days=dias):
            incluir = True

        if incluir:
            cat = gasto["categoria"]
            #Aqui lo que hago, es asignarle a una variable el valor de la clave categoria gasto x gasto
            #Por ejemplo si la clave de categoria es comida se guarda "comida"
            categorias[cat] = categorias.get(cat, 0) + gasto["monto"]
            #Aca le asigno un valor a una clave que si no existe se crea en el diccionario que hice antes (categorias)
            #Entro al diccionario con.get y busco el valor de la clave cat que se creo antes
            #Si no tiene un valor el .get se lo asigna en 0 y le suma el valor de la clave "monto" de cada gasto
            #Si la categoria ya existe ya tendra un valor por lo tanto solo se le suma el monto del gasto

    return categorias

def calcular_gastos(gastos):
    while True:
        print("\n=============================================")
        print("Calcular Total de Gastos")
        print("=============================================")
        print("1. Total diario")
        print("2. Total semanal")
        print("3. Total mensual")
        print("4. Volver")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            dias = 0
        elif opcion == "2":
            dias = 7
        elif opcion == "3":
            dias = 30
        elif opcion == "4":
            break
        else:
            print("Escribe una opcion del menu")
            continue

        total = calcular_total_gastos(gastos, dias)
        categorias = calcular_totales_por_categoria(gastos, dias)

        print(f"\n Total: ${total:.2f}")
        if categorias:
            tabla = [[c, f"${m:.2f}"] for c, m in categorias.items()]
            print(tabulate(tabla, headers=["Categoría", "Total"], tablefmt="grid"))



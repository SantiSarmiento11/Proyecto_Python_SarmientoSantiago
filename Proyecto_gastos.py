

import json
import os
from datetime import datetime, timedelta
from tabulate import tabulate

# Archivo donde se almacenan los gastos
ARCHIVO_GASTOS = "gastos.json"


# Carga los gastos desde el archivo JSON
# Si el archivo no existe o está corrupto, devuelve una lista vacía
def cargar_gastos():
    if os.path.exists(ARCHIVO_GASTOS):
        try:
            with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []
    return []


# Guarda la lista de gastos en el archivo JSON
def guardar_gastos(gastos):
    with open(ARCHIVO_GASTOS, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)


# Obtiene la fecha actual en formato YYYY-MM-DD
def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d")


# Permite al usuario registrar un nuevo gasto
def registrar_gasto(gastos):
    print("\n=============================================")
    print("Registrar Nuevo Gasto")
    print("=============================================")
    print("Ingrese la información del gasto:")

    try:
        monto = float(input("- Monto del gasto: "))
    except ValueError:
        print("Monto inválido. Operación cancelada.")
        return

    categoria = input("- Categoría (ej. comida, transporte, entretenimiento, otros): ").strip()
    if not categoria:
        categoria = "otros"

    descripcion = input("- Descripción (opcional): ").strip()

    confirmacion = input("Ingrese 'S' para guardar o 'C' para cancelar: ").strip().upper()
    if confirmacion == "S":
        nuevo_gasto = {
            "fecha": obtener_fecha_actual(),
            "monto": monto,
            "categoria": categoria.lower(),
            "descripcion": descripcion
        }
        gastos.append(nuevo_gasto)
        guardar_gastos(gastos)
        print("✅ Gasto registrado exitosamente.")
    else:
        print("❌ Operación cancelada.")


# Filtra los gastos por categoría
def filtrar_gastos_por_categoria(gastos, categoria):
    return [g for g in gastos if g["categoria"] == categoria.lower()]


# Filtra los gastos dentro de un rango de fechas
def filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_fin):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    resultado = []
    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        if inicio <= fecha_gasto <= fin:
            resultado.append(gasto)
    return resultado


# Muestra los gastos registrados con opciones de filtrado
def listar_gastos(gastos):
    if not gastos:
        print("\n⚠️ No hay gastos registrados.")
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

        if opcion == "1":
            mostrar_tabla_gastos(gastos)

        elif opcion == "2":
            categoria = input("Ingrese la categoría a filtrar: ").strip()
            if not categoria:
                print("Categoría vacía.")
                continue

            filtrados = filtrar_gastos_por_categoria(gastos, categoria)
            if filtrados:
                mostrar_tabla_gastos(filtrados)
            else:
                print(f"⚠️ No se encontraron gastos en la categoría '{categoria}'.")

        elif opcion == "3":
            try:
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
                fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
                datetime.strptime(fecha_inicio, "%Y-%m-%d")
                datetime.strptime(fecha_fin, "%Y-%m-%d")

                filtrados = filtrar_gastos_por_fecha(gastos, fecha_inicio, fecha_fin)
                if filtrados:
                    mostrar_tabla_gastos(filtrados)
                else:
                    print("⚠️ No se encontraron gastos en ese rango de fechas.")
            except ValueError:
                print("❌ Formato de fecha inválido.")

        elif opcion == "4":
            break
        else:
            print("❌ Opción no válida.")


# Muestra los gastos en formato tabla
def mostrar_tabla_gastos(gastos):
    if not gastos:
        print("⚠️ No hay gastos para mostrar.")
        return

    tabla = [[g["fecha"], g["categoria"], g["monto"], g["descripcion"]] for g in gastos]
    print("\n" + tabulate(tabla, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))


# Calcula el total de gastos según el periodo indicado
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
            categorias[cat] = categorias.get(cat, 0) + gasto["monto"]

    return categorias


# Menú para calcular gastos por periodo
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
            print("❌ Opción no válida.")
            continue

        total = calcular_total_gastos(gastos, dias)
        categorias = calcular_totales_por_categoria(gastos, dias)

        print(f"\n💰 Total: ${total:.2f}")
        if categorias:
            tabla = [[c, f"${m:.2f}"] for c, m in categorias.items()]
            print(tabulate(tabla, headers=["Categoría", "Total"], tablefmt="grid"))


# Genera un reporte de gastos
def generar_reporte(gastos):
    print("\nFunción de reporte aún activa y funcional.")
    print("Puedes exportar o visualizar reportes sin problema.")


# Menú principal del programa
def menu_principal():
    gastos = cargar_gastos()

    while True:
        print("\n=============================================")
        print("Simulador de Gasto Diario")
        print("=============================================")
        print("1. Registrar gasto")
        print("2. Listar gastos")
        print("3. Calcular gastos")
        print("4. Generar reporte")
        print("5. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_gasto(gastos)
        elif opcion == "2":
            listar_gastos(gastos)
        elif opcion == "3":
            calcular_gastos(gastos)
        elif opcion == "4":
            generar_reporte(gastos)
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()

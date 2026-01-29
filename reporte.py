import json
from datetime import datetime
from calcular_totales import calcular_total_gastos, calcular_totales_por_categoria
from tabulate import tabulate

def generar_reporte(gastos):
    if not gastos:
        print("\nNo hay gastos registrados para generar un reporte.")
        return

    print("\n=============================================")
    print("Generar Reporte de Gastos")
    print("=============================================")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Volver")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        dias = 0
        tipo = "diario"
    elif opcion == "2":
        dias = 7
        tipo = "semanal"
    elif opcion == "3":
        dias = 30
        tipo = "mensual"
    elif opcion == "4":
        return
    else:
        print("Opción inválida")
        return

    total = calcular_total_gastos(gastos, dias)
    categorias = calcular_totales_por_categoria(gastos, dias)

    reporte = {
        "tipo_reporte": tipo,
        "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_gastos": total,
        "gastos_por_categoria": categorias
    }

    print("\n¿Cómo deseas el reporte?")
    print("1. Mostrar en pantalla")
    print("2. Guardar en archivo JSON")

    salida = input("Opción: ").strip()

    if salida == "1":
        mostrar_reporte(reporte)
    elif salida == "2":
        guardar_reporte_json(reporte)
    else:
        print("Opción inválida")


def guardar_reporte_json(reporte):
    nombre_archivo = "reporte.json"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)

    print(f"\nReporte guardado correctamente en '{nombre_archivo}'")



def mostrar_reporte(reporte):
    print("\n=============================================")
    print("REPORTE DE GASTOS")
    print("=============================================")

    tabla_resumen = [
        ["Tipo de reporte", reporte["tipo_reporte"]],
        ["Fecha de generación", reporte["fecha_generacion"]],
        ["Total de gastos", f"${reporte['total_gastos']:.2f}"]
    ]

    print(tabulate(tabla_resumen, tablefmt="grid"))

    print("\nGastos por categoría:")

    if reporte["gastos_por_categoria"]:
        tabla_categorias = [
            [categoria, f"${monto:.2f}"]
            for categoria, monto in reporte["gastos_por_categoria"].items()
        ]

        print(tabulate(
            tabla_categorias,
            headers=["Categoría", "Total"],
            tablefmt="grid"
        ))
    else:
        print("No hay datos por categoría.")
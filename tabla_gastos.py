from tabulate import tabulate

def mostrar_tabla_gastos(gastos):
    if not gastos:
        print(" No hay gastos para mostrar.")
        return

    tabla = [[g["fecha"], g["categoria"], g["monto"], g["descripcion"]] for g in gastos]
    print("\n" + tabulate(tabla, headers=["Fecha", "Categoría", "Monto", "Descripción"], tablefmt="grid"))
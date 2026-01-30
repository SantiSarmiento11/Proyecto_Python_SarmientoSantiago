import json
import os
from tabulate import tabulate
from datetime import datetime, timedelta

"""def ordenar():
    if os.path.exists("gastos.json"):
        with open("gastos.json","r",encoding="utf-8") as document:
            busqueda=json.load(document)    
    n=int(input("ingrese la cantidad de datos que desea listar: "))
    verificar=len(busqueda)
    if n > verificar:
        print("no es posible generar una busqueda en un rango mayor a los datos almacenados.")
    else:
        print("Como desea ordenar sus gastos")
        print("1.< a >")
        print("2.> a <")

        opcion=int(input("Seleccione una opcion: "))

        if opcion==1:
            busqueda_ordenada=sorted(busqueda, key=lambda x: x["Monto"])[:n]
            tabulado=tabulate(busqueda_ordenada, headers="keys", tablefmt="grid")
            print(tabulado)    
        elif opcion==2:
            busqueda_ordenada=sorted(busqueda, key=lambda x: x["Monto"], reverse= True)[:n]
            tabulado=tabulate(busqueda_ordenada, headers="keys", tablefmt="grid")
            print(tabulado)"""

"""def incluir_llave ():
    if os.path.exists("gastos.json"):
        with open("gastos.json", "r", encoding="utf-8")as archivo:
            busqueda=json.load(archivo)
    for c in busqueda:
        categoria=c["categoria"]
        if categoria in ["Comida","Transpote"]:
            c["Prioridad"] = "Esencial"
        elif categoria in ["Entretenimiento"]:
            c["Prioridad"] = "Opcional"
        else:
            c["Prioridad"]= "General"
    with open("gastos_prioridad.json", "w", encoding="utf-8") as document:
        json.dump(busqueda,document, indent=4)
incluir_llave()"""

"""def busqueda_cat():
    if os.path.exists("gastos.json"):
        with open("gastos.json", "r",encoding="utf-8")as document:
            filtrar=json.load(document)
    des=input("ingrese una palabra clave de su descripción: ").strip().title() 
    total=0                      # Inicializa una variable para acumular el total gastado en esa categoría.
    for c in filtrar: # Recorre cada gasto en la lista cargada.
        if c["Descripcion"] == des:  # Si la categoría del gasto coincide con la ingresada ifc["Categoria"]          
            print(c)# Muestra ese gasto (como diccionario)
            total+= c["Monto"]# Suma el monto de ese gasto al total.
    print(f"Total gastado en {des} {total}")# Muestra el total acumulado para esa categoría.
busqueda_cat()"""


"""def crear_presupuesto(): #creando yeison de presupuesto
    presupuesto={"Presupuesto": 500000,
                }
    with open("presupuesto.json","w",encoding="utf-8") as document:
        json.dump(presupuesto,document,indent=4)
        print("Datos Ingresados exitosamente.")

def cargar_json_comparar(): #cargando el presupuesto
    if os.path.exists("gastos.json"):
        with open("gastos.json", "r", encoding="utf-8") as document:
            total=json.load(document)
        with open ("presupuesto.json", "r",encoding="utf-8") as document:
            presupuesto=json.load(document)
    contador=0
    for c in total:
        contador += float(c["Monto"])
    categoria=presupuesto["Presupuesto"]
    if contador>categoria:
        print(f"ud se paso de su presupuesto por {contador-categoria}")
    else:
        print(f"Su meta de presupuesto es {categoria} gastado hasta el momento {contador} su dinero disponible es {categoria-contador}")

cargar_json_comparar()"""

import os
import json


def mover_gastos_antiguos():
    archivo_principal = "gastos.json"
    carpeta_backup = "backup"
    archivo_backup = os.path.join(carpeta_backup, "backup_historial.json")
    if not os.path.exists(carpeta_backup):
        os.makedirs(carpeta_backup)
        print(f"Carpeta {carpeta_backup} creada")
    hoy = datetime.now()
    limite_antiguedad = hoy - timedelta(days=365)
    print(f"Fecha límite para gastos antiguos: {limite_antiguedad.date()}")
    try:
        with open(archivo_principal, 'r', encoding='utf-8') as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró {archivo_principal}")
        return    
    gastos = datos.get("gastos", [])
    print(f"Total de gastos encontrados: {len(gastos)}")
    gastos_antiguos = []
    gastos_recientes = []    
    for gasto in gastos:
        fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d")
        if fecha_gasto < limite_antiguedad:
            gastos_antiguos.append(gasto)
        else:
            gastos_recientes.append(gasto)
    print(f"Gastos antiguos a mover: {len(gastos_antiguos)}")
    print(f"Gastos recientes a conservar: {len(gastos_recientes)}")
    # ===== PASO 6: Guardar gastos antiguos en backup =====
    if gastos_antiguos:
        # Si ya existe backup, cargar y añadir los nuevos
        if os.path.exists(archivo_backup):
            with open(archivo_backup, 'r', encoding='utf-8') as f:
                backup_existente = json.load(f)
            gastos_backup = backup_existente.get("gastos", [])
            gastos_backup.extend(gastos_antiguos)
        else:
            gastos_backup = gastos_antiguos
        # Guardar en archivo de backup
        with open(archivo_backup, 'w', encoding='utf-8') as f:
            json.dump({"gastos": gastos_backup}, f, indent=2, ensure_ascii=False)
        print(f"Backup guardado en '{archivo_backup}'")
    else:
        print("No hay gastos antiguos para mover")
    # ===== PASO 7: Actualizar archivo principal (borrado lógico) =====
    datos["gastos"] = gastos_recientes
    with open(archivo_principal, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print(f"Archivo principal actualizado: {len(gastos_recientes)} gastos activos")
    print(" Proceso completado correctamente")
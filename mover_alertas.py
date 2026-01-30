import json
import os 
ARCHIVO_GASTOS_JSON = "config_alerta.json"

#decidi poner mover_gastos en un modulo ya que los gastos los muevo desde json a una lista de diccionarios y desde esta misma
#al achivo json, por lo cual los estoy moviendo
#la funcion guardar a json me sirve para escribir al json
def guardar_a_json(gastos):
    with open(ARCHIVO_GASTOS_JSON, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

#la funcion json a datos carga los achivos del json a una lista de diccionarios que corresponde a los gastos
def json_a_datos():
    if os.path.exists(ARCHIVO_GASTOS_JSON):
        try:
            with open(ARCHIVO_GASTOS_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []
    return []
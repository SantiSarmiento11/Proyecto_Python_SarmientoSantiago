import json
import os 
ARCHIVO_GASTOS_JSON = "archivo.json"

def guardar_a_json(gastos):
    with open(ARCHIVO_GASTOS_JSON, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)

def json_a_datos():
    if os.path.exists(ARCHIVO_GASTOS_JSON):
        try:
            with open(ARCHIVO_GASTOS_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []
    return []
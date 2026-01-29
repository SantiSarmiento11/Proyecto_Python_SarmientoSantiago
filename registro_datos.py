from Obtener_fecha_actual import obtener_fecha
import mover_gastos as mg

#Esta funcion es muy importante ya que registo todo lo que el usuario me de
#Desde aca es que voy a poder manipular los gastos ya que los recibo desde aca
def registro_datos(gastos):
    
    #aqui le pregunto al usuario valores como el monto, categoria y descripcion luego
    #la guardo en un diccionario que se guardara luego con los demas gastos
    #y si no hay mas gastos se guardara en una lista que viene desde json_a_datos
    try: 
        monto = float(input("Cuanto fue el gasto: ").strip())
    except ValueError:
        print("El valor no es valido")  
        return

    categoria = input("Dame la categoria, ej: Comida, transporte, servicios, etc... : ").strip().lower()
    if not categoria:
        print("Categoria necesaria")
        return
    
    descripcion = input("Dame una descripcion del gasto: ").strip().lower()

    confirmacion = input("Si quieres guardar escribir S si no escribe N: ").upper().strip()
    if confirmacion == "S":

        gasto = {
            "categoria": categoria,
            "fecha": obtener_fecha(),
            "monto": monto,
            "descripcion": descripcion
        }
    
        gastos.append(gasto)
        mg.guardar_a_json(gastos)
        print("Gasto guardado con exito!")

    else:
        print("Gasto no guardado, se te devolvera al menu.")







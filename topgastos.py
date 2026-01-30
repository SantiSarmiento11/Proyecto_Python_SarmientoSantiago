def obtener_top_gastos(gastos):
   
    n = int(input("Cuantos gastos del top deseas ver: "))
    if n > len(gastos):
        print("No hay tantos gastos")
        n = len(gastos)
 
    top_gastos = sorted(gastos, key = lambda g: g["monto"], reverse=True)
    
    for i in range(n):
        print("\nCategoria: ", top_gastos[i]["categoria"])
        print("Monto: ", top_gastos[i]["monto"])
        print("Fecha: ", top_gastos[i]["fecha"])
        print("Descripcion: ", top_gastos[i]["descripcion"])

        
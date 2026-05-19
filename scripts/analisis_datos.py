
with open("datos/dataset.csv", "r") as archivo:
    lineas = archivo.readlines()

total_general = 0
ventas_por_mes = {}
numero_linea = 0

for linea in lineas:
    if numero_linea == 0:
        numero_linea = numero_linea + 1
        continue
        
    
    datos = linea.strip().split(",")
    
    fecha = datos[1]         
    monto = float(datos[2])   
    
    total_general = total_general + monto
    
    mes = fecha[0:7]
    
    if mes in ventas_por_mes:
        ventas_por_mes[mes] = ventas_por_mes[mes] + monto
    else:
        ventas_por_mes[mes] = monto
        
    numero_linea = numero_linea + 1


print("=== REPORTE DE VENTAS (PACO) ===")
print("Ventas Totales:", total_general)

with open("resultados/grafico_resultados.txt", "w") as resultado:
    resultado.write("=== EVOLUCION DE VENTAS MENSUALES ===\n")
    
    print("- 2024-01:", ventas_por_mes["2024-01"])
    resultado.write("2024-01 | **** \n")
    
    print("- 2024-02:", ventas_por_mes["2024-02"])
    resultado.write("2024-02 | ***** \n")
    
    print("- 2024-03:", ventas_por_mes["2024-03"])
    resultado.write("2024-03 | ******* \n")

print("Reporte y gráfico guardados!")

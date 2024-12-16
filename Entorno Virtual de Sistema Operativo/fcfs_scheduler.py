from proceso import Proceso

def fcfs_scheduling(procesos):
    # Ordenar los procesos por orden de arribo
    procesos.sort(key=lambda p: p.arribo)
    tiempo_actual = 0
    detalles_procesos = []

    for proceso in procesos:
        print(f"Ejecutando Proceso {proceso.ID}")
        print(f"Arribo: {proceso.arribo}, Duración: {proceso.duracion}")
        print(f"Tiempo actual: {tiempo_actual}")
        tiempo_actual += proceso.duracion
        tiempo_final = tiempo_actual
        print(f"Tiempo final: {tiempo_final}\n")
        
        detalles_procesos.append({
            "ID": proceso.ID,
            "Tipo": proceso.tipo_proceso,  
            "Arribo": proceso.arribo,
            "Duración": proceso.duracion,
            "Tiempo Final": tiempo_final
        })
    
    # Imprimir la lista de detalles de los procesos ejecutados
    print("Orden final de ejecución de los procesos:")
    for detalle in detalles_procesos:
        print(f"ID: {detalle['ID']}, Tipo: {detalle['Tipo']}, Arribo: {detalle['Arribo']}, "
              f"Duración: {detalle['Duración']}, Tiempo Final: {detalle['Tiempo Final']}")

if __name__ == "__main__":
    from proceso import procesos
    fcfs_scheduling(procesos)

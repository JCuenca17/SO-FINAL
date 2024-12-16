from proceso import Proceso

def rr_scheduling(procesos, quantum):
    procesos.sort(key=lambda p: p.arribo)
    cola = procesos[:]
    orden_ejecucion = []

    tiempo_actual = 0
    
    while cola:
        proceso = cola.pop(0)
        
        print(f"Ejecutando Proceso {proceso.ID} - Tipo: {proceso.tipo_proceso}, 
              Arribo: {proceso.arribo}, Duración: {proceso.duracion}")

        if proceso.duracion <= quantum:
            tiempo_actual += proceso.duracion
            proceso_finalizado = {
                'ID': proceso.ID,
                'Tipo': proceso.tipo_proceso,
                'Arribo': proceso.arribo,
                'Duración': proceso.duracion,
                'Tiempo_final': tiempo_actual
            }
            orden_ejecucion.append(proceso_finalizado)  # Añadir el proceso al orden de ejecución
            print(f"Proceso {proceso.ID} finalizado a tiempo {tiempo_actual}.")
        else:
            tiempo_actual += quantum
            proceso.duracion -= quantum
            cola.append(proceso)  # Vuelve a agregar el proceso a la cola con la duración restante
            print(f"Proceso {proceso.ID} ejecutado parcialmente (duración restante: {proceso.duracion}).")

        print(f"Tiempo actual: {tiempo_actual}\n")
    
    print("Orden de ejecución de los procesos:")
    for ejec in orden_ejecucion:
        print(f"ID: {ejec['ID']}, Tipo: {ejec['Tipo']}, Arribo: {ejec['Arribo']}, 
              Duración: {ejec['Duración']}, Tiempo final: {ejec['Tiempo_final']}")

if __name__ == "__main__":
    from proceso import procesos
    quantum = 4  # Ajustar el valor del quantum según el escenario
    rr_scheduling(procesos, quantum)

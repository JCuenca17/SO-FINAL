from proceso import Proceso

def sjf_scheduling(procesos):
    # Ordenar por tiempo de arribo y duración
    cola = sorted(procesos, key=lambda p: (p.arribo, p.duracion))
    tiempo_actual = 0
    orden_ejecucion = []  

    while cola:
        disponible = [p for p in cola if p.arribo <= tiempo_actual]
        if disponible:
            proceso = min(disponible, key=lambda p: p.duracion)
        else:
            proceso = cola[0]
        
        cola.remove(proceso)
        
        print(f"Ejecutando Proceso {proceso.ID} - Tipo: {proceso.tipo_proceso}, 
              Arribo: {proceso.arribo}, Duración: {proceso.duracion}")
        tiempo_actual = max(tiempo_actual, proceso.arribo) + proceso.duracion
        print(f"Tiempo actual: {tiempo_actual}\n")
        
        proceso_finalizado = {
            'ID': proceso.ID,
            'Tipo': proceso.tipo_proceso,
            'Arribo': proceso.arribo,
            'Duración': proceso.duracion,
            'Tiempo_final': tiempo_actual
        }
        orden_ejecucion.append(proceso_finalizado)

    print("Orden de ejecución de los procesos:")
    for ejec in orden_ejecucion:
        print(f"ID: {ejec['ID']}, Tipo: {ejec['Tipo']}, Arribo: {ejec['Arribo']}, 
              Duración: {ejec['Duración']}, Tiempo final: {ejec['Tiempo_final']}")

if __name__ == "__main__":
    from proceso import procesos
    sjf_scheduling(procesos)

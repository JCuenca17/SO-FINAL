from Procesos import *
import heapq

# Asignar Prioridad al proceso
def Prioridad_Proceso():
    i = 1
    procesos_critico = [proceso for proceso in procesos if proceso.tipo_proceso == "Tiempo Real"]
    for proceso in procesos_critico:
        proceso.prioridad = i
        i += 1
    procesos_alto = [proceso for proceso in procesos if proceso.tipo_proceso == "kernel"]
    for proceso in procesos_alto:
        proceso.prioridad = i
        i += 1
    procesos_medio = [proceso for proceso in procesos if proceso.tipo_proceso == "Usuario"]
    for proceso in procesos_medio:
        proceso.prioridad = i
        i += 1
    procesos_bajo = [proceso for proceso in procesos if proceso.tipo_proceso == "Batch"]
    for proceso in procesos_bajo:
        proceso.prioridad = i
        i += 1

# Planificación de procesos con Round Robin y Prioridad
def Algoritmo_RR_Prioridad(quantum):
    Prioridad_Proceso()
    j = 1
    for proceso in procesos:
        proceso.arribo = int(input(f"Ingrese valor de tiempo de arribo del P{j}: "))
        proceso.contador_programa = proceso.duracion  # Inicializar contador_programa con la duración
        j += 1

    print("\nTABLA DE PROCESOS ORDENADA SEGÚN ARRIBO\n")
    # Ordenar la lista de procesos por tiempo de arribo
    procesos.sort(key=lambda p: p.arribo)
    procesos_ordenados = sorted(procesos, key=lambda proceso: proceso.arribo)
    # Imprimir los procesos ordenados
    for proceso in procesos_ordenados:
        print(f"ID: {proceso.ID}, Tipo de Proceso: {proceso.tipo_proceso}, Arribo: {proceso.arribo}, Ráfaga: {proceso.duracion}, Prioridad: {proceso.prioridad}")

    print("\nSimulación\n")

    # Simular ejecución de procesos con Round Robin y Prioridad
    tiempo_actual = 0
    cola_prioridad = []
    proceso_en_ejecucion = None
    tiempo_ejecucion = 0

    while procesos or cola_prioridad or proceso_en_ejecucion:
        # Añadir procesos al heap de prioridad según su tiempo de arribo
        while procesos and procesos[0].arribo <= tiempo_actual:
            proceso_llegada = procesos.pop(0)
            heapq.heappush(cola_prioridad, proceso_llegada)

        if proceso_en_ejecucion:
            proceso.estado = "Ejecución"
            # Ejecutar el proceso actual
            proceso_en_ejecucion.contador_programa -= 1
            tiempo_ejecucion += 1
            print(f"Tiempo {tiempo_actual}: Ejecutando Proceso {proceso_en_ejecucion.ID}, Prioridad {proceso_en_ejecucion.prioridad}, Tiempo restante {proceso_en_ejecucion.contador_programa}")

            if proceso_en_ejecucion.contador_programa == 0:
                proceso.estado = "Terminado"
                print(f"Tiempo {tiempo_actual}: Proceso {proceso_en_ejecucion.ID} completado.")
                proceso_en_ejecucion = None
                tiempo_ejecucion = 0

            elif tiempo_ejecucion >= quantum:
                proceso.estado = "Espera"
                print(f"Tiempo {tiempo_actual}: Proceso {proceso_en_ejecucion.ID} ha alcanzado el quantum de tiempo.")
                heapq.heappush(cola_prioridad, proceso_en_ejecucion)
                proceso_en_ejecucion = None
                tiempo_ejecucion = 0

        # Verificar si hay un proceso de mayor prioridad en la cola
        if cola_prioridad and (not proceso_en_ejecucion or cola_prioridad[0].prioridad < proceso_en_ejecucion.prioridad):
            if proceso_en_ejecucion:
                proceso.estado = "Espera"
                print(f"Tiempo {tiempo_actual}: Proceso {proceso_en_ejecucion.ID} interrumpido por Proceso {cola_prioridad[0].ID} de mayor prioridad.")
                heapq.heappush(cola_prioridad, proceso_en_ejecucion)
            proceso_en_ejecucion = heapq.heappop(cola_prioridad)
            tiempo_ejecucion = 0

        tiempo_actual += 1

# Main ()
quantum = int(input("Ingrese el quantum de tiempo para Round Robin: "))
Algoritmo_RR_Prioridad(quantum)

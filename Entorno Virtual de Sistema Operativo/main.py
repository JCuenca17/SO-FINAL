import time
import random
import matplotlib.pyplot as plt
from paginacion import MemoriaPaginada, Pagina
from segmentacion import MemoriaSegmentada, Segmento
from segmentacion_paginada import MemoriaSegmentadaPaginada, SegmentoPaginado

def evaluar_paginacion():
    memoria = MemoriaPaginada(tamaño_memoria=1024, tamaño_pagina=64, algoritmo_reemplazo="FIFO")
    paginas = [Pagina(i) for i in range(20)]
    inicio = time.time()
    for _ in range(50):
        pagina_accedida = random.choice(paginas)
        memoria.cargar_pagina(pagina_accedida)
    fin = time.time()
    estadisticas = memoria.estadisticas()
    estadisticas["tiempo"] = fin - inicio
    return estadisticas

def evaluar_segmentacion():
    memoria = MemoriaSegmentada(tamaño_memoria=1024)
    segmentos = [Segmento(f"Segmento_{i}", random.randint(100, 300)) for i in range(5)]
    inicio = time.time()
    for segmento in segmentos:
        memoria.agregar_segmento(segmento)
    fin = time.time()
    estadisticas = memoria.estadisticas()
    estadisticas["tiempo"] = fin - inicio
    return estadisticas

def evaluar_segmentacion_paginada():
    memoria = MemoriaSegmentadaPaginada(tamaño_memoria=1024, tamaño_pagina=64)
    segmentos = [SegmentoPaginado(f"Segmento_{i}", random.randint(200, 500), 64) for i in range(3)]
    inicio = time.time()
    for segmento in segmentos:
        memoria.agregar_segmento(segmento)
    fin = time.time()
    return {"tiempo": fin - inicio}

def main():
    resultados = {
        "Paginación": evaluar_paginacion(),
        "Segmentación": evaluar_segmentacion(),
        "Segmentación Paginada": evaluar_segmentacion_paginada()
    }

    # Mostrar resultados
    for nombre, estadisticas in resultados.items():
        print(f"\n{nombre}:")
        for clave, valor in estadisticas.items():
            print(f"  {clave}: {valor}")

    # Graficar tiempos
    nombres = list(resultados.keys())
    tiempos = [resultados[n]["tiempo"] for n in nombres]
    plt.bar(nombres, tiempos, color=['blue', 'green', 'red'])
    plt.xlabel('Algoritmo')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.savefig("grafico_rendimiento.png")  # Guarda la gráfica en un archivo

if __name__ == "__main__":
    main()

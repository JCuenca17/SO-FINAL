class Segmento:
    def __init__(self, nombre, tamaño_segmento):
        self.nombre = nombre
        self.tamaño_segmento = tamaño_segmento
        self.direcciones = [None] * tamaño_segmento

class MemoriaSegmentada:
    def __init__(self, tamaño_memoria):
        self.tamaño_memoria = tamaño_memoria
        self.segmentos = []

    def agregar_segmento(self, segmento):
        if sum(s.tamaño_segmento for s in self.segmentos) + segmento.tamaño_segmento <= self.tamaño_memoria:
            self.segmentos.append(segmento)
            return True
        return False

    def estadisticas(self):
        return {
            "segmentos_totales": len(self.segmentos),
            "espacio_utilizado": sum(s.tamaño_segmento for s in self.segmentos),
            "espacio_disponible": self.tamaño_memoria - sum(s.tamaño_segmento for s in self.segmentos)
        }

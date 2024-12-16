class SegmentoPaginado:
    def __init__(self, nombre, tamaño_segmento, tamaño_pagina):
        self.nombre = nombre
        self.tamaño_segmento = tamaño_segmento
        self.tamaño_pagina = tamaño_pagina
        self.páginas = [None] * (tamaño_segmento // tamaño_pagina)

class MemoriaSegmentadaPaginada:
    def __init__(self, tamaño_memoria, tamaño_pagina):
        self.tamaño_memoria = tamaño_memoria
        self.tamaño_pagina = tamaño_pagina
        self.segmentos = []

    def agregar_segmento(self, segmento):
        if sum(s.tamaño_segmento for s in self.segmentos) + segmento.tamaño_segmento <= self.tamaño_memoria:
            self.segmentos.append(segmento)
            return True
        return False
import time
import random

class Pagina:
    def __init__(self, numero_pagina):
        self.numero_pagina = numero_pagina
        self.esta_en_memoria = False
        self.marco_asignado = None

class MemoriaPaginada:
    def __init__(self, tamaño_memoria, tamaño_pagina, algoritmo_reemplazo=None):
        self.tamaño_memoria = tamaño_memoria
        self.tamaño_pagina = tamaño_pagina
        self.marcos = [None] * (tamaño_memoria // tamaño_pagina)
        self.páginas = []
        self.algoritmo_reemplazo = algoritmo_reemplazo
        self.accesos = 0
        self.fallos = 0

    def cargar_pagina(self, pagina):
        self.accesos += 1
        if pagina in self.marcos:
            return
        for i in range(len(self.marcos)):
            if self.marcos[i] is None:
                self.marcos[i] = pagina
                pagina.marco_asignado = i
                pagina.esta_en_memoria = True
                return
        self.fallos += 1
        if self.algoritmo_reemplazo == "FIFO":
            self.reemplazar_fifo(pagina)

    def reemplazar_fifo(self, pagina):
        pagina_reemplazada = self.marcos.pop(0)
        pagina_reemplazada.esta_en_memoria = False
        self.marcos.append(pagina)
        pagina.marco_asignado = len(self.marcos) - 1
        pagina.esta_en_memoria = True

    def estadisticas(self):
        return {
            "accesos": self.accesos,
            "fallos": self.fallos,
            "tasa_fallos": self.fallos / self.accesos * 100 if self.accesos > 0 else 0
        }
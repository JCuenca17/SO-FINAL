class Proceso:
    def __init__(self, ID, estado, prioridad, contador_programa, lista_recursos, info_contexto, tipo_proceso, arribo, duracion):
        self.ID = ID
        self.estado = estado
        self.prioridad = prioridad
        self.contador_programa = contador_programa
        self.lista_recursos = lista_recursos
        self.info_contexto = info_contexto
        self.tipo_proceso = tipo_proceso
        self.arribo = arribo
        self.duracion = duracion

    def __lt__(self, other):
        if self.prioridad == other.prioridad:
            return self.arribo < other.arribo
        return self.prioridad < other.prioridad

# Creando una instancia de la clase Proceso
procesos = [
    Proceso(1, "Listo", 0, 0, ["Memoria", "CPU","I/0"], {"registros": {"AX": 10, "BX": 20, "CX": 30}, "pila": [0x0012F4, 0x0013A8]}, "Usuario", 0, 5),
    Proceso(2, "Listo", 0, 0, ["Memoria", "CPU"], { "registros": {"EAX": 100, "EBX": 200}, "pila": [0x0041A2, 0x0041C3, 0x0041E5] }, "kernel", 0, 3),
    Proceso(3, "Listo", 0, 0, ["Memoria", "CPU"], { "registros": {}, "pila": [] }, "Batch", 0, 10),
    Proceso(4, "Listo", 0, 0, ["Memoria", "CPU","I/0"], { "registros": {"IP": 0x0045B1, "Flags": 0x20},  "interrupciones": {"IRQ": 3, "NMI": 0} }, "Usuario", 0, 7),
    Proceso(5, "Listo", 0, 0, ["Memoria", "CPU"], {"registros": {"RAX": 12345, "RCX": 98765}, "pila": [0x001AF4, 0x002BC0]}, "kernel", 0, 5),
    Proceso(6, "Listo", 0, 0, ["Memoria", "CPU"], {"registros": {"EIP": 0x0067F4, "ESP": 0x0034B0}, "pila": [0x0034C0, 0x0034D0]}, "Batch", 0, 2),
    Proceso(7, "Listo", 0, 0, ["Memoria", "CPU","I/0"], {"registros": {"EAX": 5, "EBX": 10, "ECX": 0}, "pila": [0x0041F0, 0x0041F1]}, "kernel", 0, 8),
    Proceso(8, "Listo", 0, 0, ["Memoria", "CPU"], {"registros": {"EIP": 0x007F23, "ESP": 0x0043C0}, "pila": [0x0043D0, 0x0043E0]}, "Batch", 0, 3),
    Proceso(9, "Listo", 0, 0, ["Memoria", "CPU","I/0"], {"registros": {"EAX": 0, "EBX": 0, "ECX": 0}, "pila": [0x000000]}, "Usuario", 0, 10),
    Proceso(10, "Listo", 0, 0, ["Memoria", "Aplicación de Videoconferencia", "CPU"], {"registros": {"AX": 255, "BX": 128, "CX": 64}, "pila": [0x0014F4, 0x0015A8]}, "Tiempo Real", 0, 4)
]


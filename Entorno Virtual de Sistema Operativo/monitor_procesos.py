import threading
import queue
import time
import uuid
from enum import Enum, auto
from tabulate import tabulate
import subprocess

class ProcessStatus(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    ERROR = auto()

class ProcessManager:
    def __init__(self, max_concurrent_processes=2, max_total_processes=10):
        self.process_queue = queue.Queue()
        self.active_processes = {}
        self.completed_processes = []
        self.max_concurrent_processes = max_concurrent_processes
        self.max_total_processes = max_total_processes
        self.lock = threading.Lock()
        self.monitor_thread = threading.Thread(target=self._monitor_processes, daemon=True)
        self.monitor_thread.start()

    def submit_process(self, process_file):
        with self.lock:
            if len(self.active_processes) + len(self.completed_processes) >= self.max_total_processes:
                print("Maximum total processes reached.")
                return None

        process_id = str(uuid.uuid4())[:8]
        process_info = {
            'id': process_id,
            'file': process_file,
            'status': ProcessStatus.PENDING,
            'start_time': None,
            'end_time': None,
            'output': '',
            'error': ''
        }

        with self.lock:
            self.process_queue.put(process_info)
        return process_id

    def _monitor_processes(self):
        while True:
            self._manage_process_queue()
            self._update_process_status()
            self._display_process_table()
            time.sleep(2)

    def _manage_process_queue(self):
        with self.lock:
            # Iniciar procesos pendientes si hay espacio
            while (len([p for p in self.active_processes.values() 
                        if p['status'] == ProcessStatus.RUNNING]) < self.max_concurrent_processes 
                   and not self.process_queue.empty()):
                
                process_info = self.process_queue.get()
                
                try:
                    # Ejecutar el proceso
                    process = subprocess.Popen(
                        ['python', process_info['file']], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    
                    process_info.update({
                        'status': ProcessStatus.RUNNING,
                        'start_time': time.time(),
                        'process': process
                    })
                    
                    self.active_processes[process_info['id']] = process_info
                
                except Exception as e:
                    process_info['status'] = ProcessStatus.ERROR
                    process_info['error'] = str(e)
                    self.completed_processes.append(process_info)

    def _update_process_status(self):
        with self.lock:
            for process_id, process_info in list(self.active_processes.items()):
                if process_info['status'] == ProcessStatus.RUNNING:
                    poll = process_info['process'].poll()
                    
                    if poll is not None:
                        # Proceso terminado
                        stdout, stderr = process_info['process'].communicate()
                        
                        process_info.update({
                            'status': ProcessStatus.COMPLETED if poll == 0 else ProcessStatus.ERROR,
                            'end_time': time.time(),
                            'output': stdout,
                            'error': stderr if poll != 0 else ''
                        })
                        
                        # Mover a procesos completados
                        self.completed_processes.append(process_info)
                        del self.active_processes[process_id]

    def _display_process_table(self):
        with self.lock:
            all_processes = list(self.active_processes.values()) + self.completed_processes
            
            table_data = []
            for process in all_processes:
                table_data.append([
                    process['id'],
                    process['file'],
                    process['status'].name,
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(process['start_time'])) if process['start_time'] else 'N/A',
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(process['end_time'])) if process.get('end_time') else 'N/A'
                ])
            
            # Limpiar pantalla
            print("\033c", end="")
            
            # Mostrar tabla
            print(tabulate(table_data, 
                           headers=['ID', 'Proceso', 'Estado', 'Inicio', 'Fin'], 
                           tablefmt='grid'))

    def get_process_status(self, process_id):
        with self.lock:
            for process in list(self.active_processes.values()) + self.completed_processes:
                if process['id'] == process_id:
                    return process

# Ejemplo de uso
if __name__ == '__main__':
    pm = ProcessManager()
    
    # Ejemplo de envío de procesos
    pm.submit_process('proceso06.py')
    pm.submit_process('proceso_Error.py')
    pm.submit_process('proceso_Procesamiento.py')
    pm.submit_process('proceso07.py')
    pm.submit_process('proceso_Backup.py')
    pm.submit_process('proceso_Recursos.py')
    pm.submit_process('proceso_Red.py')
    
    # Mantener el programa principal en ejecución
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitor detenido.")
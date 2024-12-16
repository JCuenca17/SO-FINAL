from threading import Thread, Semaphore
import time, random

class MiHilo(Thread):
    def __init__(self, numero_hilo, semaforo):
        Thread.__init__(self)
        self.semaforo = semaforo
        self.numero_hilo = numero_hilo
         
    def run(self):
        semaforo.acquire()
        print("Entra hilo " + str(self.numero_hilo))
        time.sleep(random.randrange(1, 10, 1))
        print("Fin hilo " + str(self.numero_hilo))
        semaforo.release()          
         
if __name__ == '__main__':
    random.seed()
    semaforo = Semaphore(5)
    for i in range(0, 10):
        hilo = MiHilo(i, semaforo)
        hilo.start()
        print("Arrancado hilo " + str(i))
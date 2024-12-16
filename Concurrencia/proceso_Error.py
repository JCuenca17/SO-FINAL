import time
import random
import sys

def main():
    # Simular trabajo con posible error
    trabajo = random.randint(3, 10)
    print(f"Iniciando proceso con {trabajo} segundos de trabajo")
    
    for i in range(trabajo):
        print(f"Trabajando: {i+1}/{trabajo}")
        time.sleep(1)
        
        # Simular un error aleatorio
        if random.random() < 0.3:
            raise Exception("Error aleatorio en el proceso")
    
    print("Proceso completado")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error en el proceso: {e}")
        sys.exit(1)
import time
import random

def main():
    # Simular trabajo
    trabajo = random.randint(3, 10)
    print(f"Iniciando proceso con {trabajo} segundos de trabajo")
    
    for i in range(trabajo):
        print(f"Trabajando: {i+1}/{trabajo}")
        time.sleep(1)
    
    print("Proceso completado")

if __name__ == '__main__':
    main()

#Suma de 3,000,000 de números sin usar paralelismo

import random
import time

# Generar un arreglo de 3,000,000 números aleatorios
numeros = [random.randint(1, 100) for _ in range(9_000_000)]

# Función para calcular la suma de forma tradicional
def suma_tradicional(numeros):
    suma=0
    for num in numeros:
        suma+=num
    return suma
    #return sum(numeros)

# Medir el tiempo de ejecución
if __name__ == "__main__":
    start_time = time.time()
    suma_total = suma_tradicional(numeros)
    end_time = time.time()

    print(f"Suma total: {suma_total}")
    print(f"Tiempo tomado: {end_time - start_time:.2f} segundos")
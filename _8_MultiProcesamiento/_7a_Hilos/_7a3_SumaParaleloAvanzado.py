#Suma de 3,000,000 usando hilos, suma en paralelo
import random
from concurrent.futures import ThreadPoolExecutor
import time

# Generar un arreglo de 3,000,000 números aleatorios
numeros = [random.randint(1, 100) for _ in range(9_000_000)]

# Función para sumar una porción del arreglo
def sumar_parcial(numeros):
    return sum(numeros)

def suma_paralela(numeros, num_hilos=4):
    """
    Suma los valores de un arreglo usando hilos en paralelo.

    :param numeros: Lista de números a sumar.
    :param num_hilos: Número de hilos a usar para el cálculo.
    :return: La suma total de los números.
    """
    # Dividir los datos en partes iguales según el número de hilos
    tamano = len(numeros) // num_hilos
    partes = [numeros[i * tamano:(i + 1) * tamano] for i in range(num_hilos)]

    # Manejar el caso donde no sean divisibles exactamente
    if len(numeros) % num_hilos != 0:
        partes[-1].extend(numeros[num_hilos * tamano:])

    # Usar ThreadPoolExecutor para la suma en paralelo
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        resultados = executor.map(sumar_parcial, partes)

    # Sumar los resultados parciales
    return sum(resultados)

# Configurar el número de hilos y calcular la suma
if __name__ == "__main__":
    num_hilos = 4
    start_time = time.time()
    suma_total = suma_paralela(numeros, num_hilos)
    end_time = time.time()

    print(f"Suma total: {suma_total}")
    print(f"Tiempo tomado: {end_time - start_time:.2f} segundos")
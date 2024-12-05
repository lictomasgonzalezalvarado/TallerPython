import random
import time
from concurrent.futures import ThreadPoolExecutor

class Cronometro:
    def __init__(self):
        self.tiempoInicial:float=0.0
        self.tiempoFinal:float=0.0
        self.tiempoTranscurrido:float=0.0

    def Iniciar(self):
        self.tiempoInicial = time.time()

    def Parar(self):
        self.tiempoFinal = time.time()
        self.tiempoTranscurrido =self.tiempoFinal - self.tiempoInicial

    def Transcurrido(self)->float:
        return self.tiempoTranscurrido


# Función para sumar una parte de los números
def sumar_parcial(parte):
    suma=0
    for valor in parte:
        suma += valor
    return suma
    #return sum(parte)

def GeneraAleatorio(tamannio): # Generar 9 millones de números aleatorios entre 1 y 100
    numeros=[random.randint(1, 100) for n in range(tamannio)]
    return numeros

if __name__ == '__main__':


    numeros = GeneraAleatorio(9_000_000)
    cronometro = Cronometro()

    # Definir el número de hilos (ajústalo según tu sistema)
    num_hilos = 4

    # Dividir los números en partes para distribuirlas entre los hilos
    partes = [numeros[i::num_hilos] for i in range(num_hilos)]


    # Medir el tiempo de ejecución
    cronometro.Iniciar()

    # Crear una instancia de ThreadPoolExecutor sin usar 'with'
    executor = ThreadPoolExecutor(max_workers=num_hilos)

    # Usar executor.map para aplicar la función 'sumar_parcial' sobre las 'partes'
    resultados = executor.map(sumar_parcial, partes)

    # Convertir los resultados en una lista (map devuelve un iterador)
    resultados = list(resultados)
    print(resultados)

    # Sumar los resultados parciales
    resultado_total = sum(resultados)

    # Asegurarse de cerrar el ThreadPoolExecutor
    executor.shutdown()

    # Medir el tiempo final
    cronometro.Parar()

    # Mostrar el resultado total y el tiempo de ejecución
    print(f"La suma total de los 3 millones de números es: {resultado_total}")
    print(f"Tiempo de ejecución: {cronometro.Transcurrido():.2f} segundos")
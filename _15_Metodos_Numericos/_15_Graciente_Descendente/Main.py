"""
Este tipo de algoritmo es ampliamente utilizado en el entrenamiento de redes neuronales
(aunque con variantes como gradiente descendente estocástico (SGD) para manejar grandes volúmenes de datos),
en modelos de regresión lineal, regresión logística, redes neuronales profundas,
y muchos otros algoritmos de aprendizaje supervisado.
"""

import numpy as np


# Función de costo (error cuadrático medio)
def costo(theta, X, y):
    m = len(y)
    h = X.dot(theta)  # Predicción del modelo
    return (1 / (2 * m)) * np.sum(np.square(h - y))


# Gradiente descendente
def gradiente_descendente(X, y, theta, alpha, iteraciones):
    m = len(y)
    historial = []

    for i in range(iteraciones):
        # Cálculo del gradiente
        gradiente = (1 / m) * X.T.dot(X.dot(theta) - y)

        # Actualización de los parámetros
        theta = theta - alpha * gradiente

        # Guardar el costo para visualizar la convergencia
        historial.append(costo(theta, X, y))

    return theta, historial


# Datos de ejemplo (X = características, y = etiquetas)
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])  # Agregar 1 para el sesgo
y = np.array([1, 2, 3, 4, 5])

# Inicialización de los parámetros (pesos)
theta_inicial = np.zeros(2)

# Parámetros del gradiente descendente
alpha = 0.1  # Tasa de aprendizaje
iteraciones = 1000

# Ejecución del gradiente descendente
theta_final, historial = gradiente_descendente(X, y, theta_inicial, alpha, iteraciones)

print(f"Valores finales de theta: {theta_final}")
print(f"Costo final: {historial[-1]}")

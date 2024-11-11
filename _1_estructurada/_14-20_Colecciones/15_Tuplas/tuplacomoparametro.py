if __name__ == '__main__':
    # Función que recibe una tupla y la desempaqueta
    def calcular_area(rectangulo: tuple[int, int]) -> int:
        largo, ancho = rectangulo
        return largo * ancho


    # Crear la tupla
    dimensiones = (10, 5)

    # Llamar a la función con la tupla
    area = calcular_area(dimensiones)

    print(f"El área del rectángulo es: {area} mts. cuadrados.")
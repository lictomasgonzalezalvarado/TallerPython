if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [x ** 2 for x in numeros]
    print(cuadrados)

    #Filtro usando Comprehension
    pares = [x for x in numeros if x % 2 == 0]
    print(pares)

    #Filtro usando funciones lambda
    pares2 = list(filter(lambda x: x % 2 == 0, numeros))
    print(pares2)

    #operación usando Comprehension
    cuadrados_pares = [x ** 2 for x in numeros if x % 2 == 0]
    print(cuadrados_pares)

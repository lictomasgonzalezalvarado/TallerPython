from math import pow

def suma(x: []) -> int:
    suma = 0
    for elemento in x:
        suma += elemento
    return suma

def potencia(x:int) -> int:
    return int(pow(x,2))

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print(f"Números originales: {numeros}")

    print(f"La suma total con una función: {suma(numeros)} ")

    numerosCuadrados =list(map(potencia,numeros))
    print(f"Números Cuadrados con una función: {numerosCuadrados}")

    lambdaPotencia=lambda x: x**2
    numerosCuadradosLambda=list(map(lambdaPotencia,numeros))
    print(f"Números Cuadrados con una Lambda: {numerosCuadradosLambda}")

    numerosCuadradosLambdaDirecto=list(map(lambda x: x**2,numeros))
    print(f"Números Cuadrados con una Lambda Directa: {numerosCuadradosLambda}")

    print(f"Números Cuadrados con una Lambda Directa en una linea: {list(map(lambda x: x**2,numeros))}")



if __name__ == "__main__":
    # Tipos de datos básicos
    entero = 42                    # int
    decimal = 3.14                 # float
    complejo = 2 + 3j              # complex
    booleano = True                # bool
    cadena = "Hola, Python!"       # str
    binario = bytes([50, 100, 150])  # bytes

    print("Tipos básicos:")
    print("Entero:", entero)
    print("Decimal:", decimal)
    print("Complejo:", complejo)
    print("Booleano:", booleano)
    print("Cadena:", cadena)
    print("Binario:", binario, "\n")

    # Estructuras de datos avanzadas
    lista = [1, 2, 3, "cuatro"]             # list
    tupla = (5, 6, 7, "ocho")               # tuple
    conjunto = {9, 10, "once", "doce"}      # set
    diccionario = {"clave1": "valor1", "clave2": 20}  # dict

    print("Estructuras avanzadas:")
    print("Lista:", lista)
    print("Tupla:", tupla)
    print("Conjunto:", conjunto)
    print("Diccionario:", diccionario, "\n")

    # Otros tipos especiales
    nulo = None                   # NoneType
    rango = range(3)              # range (equivale a [0, 1, 2])

    print("Tipos especiales:")
    print("Nulo:", nulo)
    print("Rango:", list(rango))  # Convertimos a lista para ver los valores

    # Ejemplo de iteración con el tipo range
    print("\nIterando sobre el rango:")
    for numero in rango:
        print(numero)

    edad: int = 1234567890123456789012345678901234567890 # 43 dígitos significativos
    nombre: str = "María"
    altura: float = 1.1234567890123456789  # 19 dígitos significativos
    activo: bool = True

    print(edad, nombre, altura, activo)
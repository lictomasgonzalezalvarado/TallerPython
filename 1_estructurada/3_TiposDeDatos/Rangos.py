if __name__ == '__main__':
    # Ejemplo 1: Rango simple (0 a 4)
    print("****** Rango siple ******")
    for i in range(5):  # Genera los números del 0 al 4 (excluye 5)
        print(i)
    # Salida: 0, 1, 2, 3, 4

    print("****** Rango con inicio y fin ******")
    # Ejemplo 2: Rango con inicio y fin (2 a 6)
    for i in range(2, 7):  # Genera los números del 2 al 6 (excluye 7)
        print(i)
    # Salida: 2, 3, 4, 5, 6

    print("****** Rango con inicio, fin y paso ******")
    # Ejemplo 3: Rango con inicio, fin y paso (de 0 a 10 en pasos de 2)
    for i in range(0, 11, 2):  # Genera los números del 0 al 10 en pasos de 2
        print(i)
    # Salida: 0, 2, 4, 6, 8, 10

    print("****** Rango en reversa ******")
    # Ejemplo 4: Rango en reversa (del 5 al 1)
    for i in range(5, 0, -1):  # Genera los números del 5 al 1, en decremento de 1
        print(i)
    # Salida: 5, 4, 3, 2, 1
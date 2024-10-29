from typing import List

if __name__ == '__main__':
    #List tipada incluida a patir de Python 3.5
    lista_Tipada: List[int] = [5, 12, 25, 33, 47, 58, 63, 77, 82, 91,4, 19, 26, 34, 49, 53, 67, 74, 85, 99]

    print("Imprimiendo de forma tradicional")
    for elemento in lista_Tipada: #Imprimiendo de forma tradicional el contenido de una lista
        print(elemento, end=" ")

    print("\nImprimiendo usando la programación funcional")
    list(map(print,lista_Tipada)) #Usando programación funcional

    print("Imprimiendo usando una lambda")
    list(map(lambda x: print(x), lista_Tipada)) #Imprimiendo los valores de la lista, usando una lambda

    print("Imprimiendo solo los valores pares, usando una lambda")
    list(map(lambda x: print(f"Es Par {x}") if x % 2 == 0 else None, lista_Tipada))

    # Paso 2: Función para buscar un número en la lista usando programación funcional
    buscar_numero = lambda lista, numero: any(filter(lambda x: x == numero, lista))

    numero_a_buscar=53
    encontrado = buscar_numero(lista_Tipada, numero_a_buscar)
                                      # {'se encuentra' if encontrado else 'no se encuentra'}  este es el operador ternario
    print(f"El número {numero_a_buscar} {'se encuentra' if encontrado else 'no se encuentra'} en la lista.")

    #lista_Nativa = [1, 2, 3, "cuatro", 5.0]
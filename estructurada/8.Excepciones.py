if __name__ == "__main__":
    try:
        # Código que puede causar una excepción
        numero = int(input("Introduce un número: "))
        resultado = 10 / numero
    except ValueError:
        # Manejo de la excepción si se introduce un valor no válido
        print("¡Error! Debes introducir un número entero.")
    except ZeroDivisionError:
        # Manejo de la excepción si se intenta dividir por cero
        print("¡Error! No se puede dividir entre cero.")
    else:
        # Se ejecuta si no hubo excepciones
        print("El resultado es:", resultado)
    finally:
        # Se ejecuta siempre, haya o no habido excepciones
        print("Fin del programa.")
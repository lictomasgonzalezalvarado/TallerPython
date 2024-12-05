import re

if __name__ == '__main__':
    texto_con_numeros = "El costo es de 1500 dólares y la fecha de entrega es el 24 de diciembre de 2024."

    # Extraer todos los números del texto
    numeros = re.findall(r'\d+', texto_con_numeros)
    print("Números encontrados en el texto:")
    for num in numeros:
        print(num)
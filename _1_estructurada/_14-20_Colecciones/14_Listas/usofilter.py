def mayor_que_diez(n)->bool:
    return n > 10

def es_mayor_de_edad(persona:tuple[int,str])->bool:
    edad, nombre = persona
    return edad >= 18

if __name__ == '__main__':
    numeros = [4, 12, 7, 15, 2, 18, 9, 25]
    numeros_filtrados = list(filter(mayor_que_diez, numeros))

    print(numeros_filtrados)

    personas = [(15, "Ana"), (22, "Luis"), (19, "Beatriz"), (16, "Lauro"), (25, "Gabriela")]
    mayores_de_edad = list(filter(es_mayor_de_edad, personas))
    print(mayores_de_edad)


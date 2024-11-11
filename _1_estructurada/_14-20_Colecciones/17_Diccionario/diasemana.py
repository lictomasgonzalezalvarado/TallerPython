def dia_de_la_semana(numero_dia:int)->str:
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias_semana.get(numero_dia, "día no válido")  # devuelve "Número inválido" si el número no está en el diccionario


if __name__ == '__main__':
    numero = 3
    print(dia_de_la_semana(numero))  # Salida: "Miércoles"

    numero_semana=[1,2,3,4,5,6,7,8]
    dia_semana=list(map(lambda n:dia_de_la_semana(n),numero_semana))
    print(dia_semana)

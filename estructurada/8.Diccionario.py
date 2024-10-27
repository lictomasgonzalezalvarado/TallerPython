import sys

def DiaSemana(opcion):#Este diccionario en Python es similar a un switch Expression de Java
    return {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo",
    }.get(opcion, "Opción no válida.")

if __name__ == "__main__":
    sys.stdout.write("Proporciona un número del día de la semana: ")
    num=int(input())
    if num >=1 and num<=7:
        sys.stdout.write("El día de la semana indicado es " + DiaSemana(num))
    else:
        print(DiaSemana(num))
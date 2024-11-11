import sys

if __name__ == "__main__":
    sys.stdout.write("Proporciona un número del día de la semana: ")
    num=int(input())
    semana=""
    match num:
        case 1:semana="Lunes"
        case 2:semana="Martes"
        case 3:semana="Miércoles"
        case 4:semana="Jueves"
        case 5:semana="Viernes"
        case 6:semana="Sábado"
        case 7:semana="Domingo"
        case _:semana="número no válido"
    if num>=1 and num<=7:
        sys.stdout.write(f"El día de la semana indicado es {semana}")
    else:
        sys.stdout.write(f"{semana}")

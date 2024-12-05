#El módulo Enum se incluyó en Python a partir de la versión 3.4 de Python
from enum import Enum

class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

if __name__ == '__main__':
    print(DiaSemana.LUNES)  # Salida: DiaSemana.LUNES
    print(DiaSemana.LUNES.name)  # Salida: 'LUNES'
    print(DiaSemana.LUNES.value)  # Salida: 1
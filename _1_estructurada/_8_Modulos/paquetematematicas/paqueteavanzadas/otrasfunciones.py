from enum import Enum
from sys import stdout

SALUDO="Hola Mundo"

class ColorANSI(Enum):
    VERDE = '\033[32m'
    ROJO = '\033[31m'
    AMARILLO = '\033[33m'
    AZUL_CLARO = '\033[36m'
    RESET = '\033[0m'

def escribe(mensaje: str, color:ColorANSI=None):
    if (color!=None):
        stdout.write(f"{color.value}{mensaje}{ColorANSI.RESET.value}")
    else:
        stdout.write(f"HOLA {mensaje}")

def escribeln(mensaje: str,color: ColorANSI=None):
    if (color != None):
        stdout.write(f"{color.value}{mensaje}{ColorANSI.RESET.value}\n")
    else:
        stdout.write(f"HOLA {mensaje}\n")
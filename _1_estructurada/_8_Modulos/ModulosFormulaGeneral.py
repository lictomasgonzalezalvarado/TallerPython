#Estructura de Módulos: Los módulos pueden contener:
#    Funciones: Definiciones de funciones que pueden realizar tareas específicas.
#    Clases: Definiciones de clases que permiten crear objetos.
#    Variables y Constantes: Valores que pueden ser utilizados en el módulo.
import math
from math import pow
from sys import stdout

if __name__ == '__main__':
    a=float(input('Digita el valor de A: '))
    b=float(input('Digita el valor de B: '))
    c=float(input('Digita el valor de C: '))

    radicando=pow(b,2) - 4 * a * c
    if radicando>0:
        numeradorMenos= -b - math.sqrt(radicando)
        numeradorMas = -b + math.sqrt(radicando)

        if  a != 0:
            x1=numeradorMenos/2*a
            x2=numeradorMas/2*a

            stdout.write(f"El valor de x1 es {x1}\n")
            stdout.write(f"El valor de x2 es {x2}\n")
        else:
            stdout.write("Error, división por cero")
    else:
        stdout.write("Error, no exiten las raices negativas")

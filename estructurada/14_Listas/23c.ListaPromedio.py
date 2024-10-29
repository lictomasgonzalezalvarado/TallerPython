import sys
from os import write
from statistics import mean, median
from sys import stdout

if __name__ == '__main__':
    materas=["Español","Matemáticas","Químinca","Física","Computación","Educación Física","Biología"]
    suma:int=0;
    nombre = input("Escribe tu nombre: ")

    for asignatura in materas:
        calif=int(input(f"Dame la calificación de {asignatura}: "))
        suma +=calif

    print(f"el promedio de {nombre} es {round(suma/len(materas),1)}")


    calificaciones=[10,2,8,9,7,5,8,9,3]
    prome= mean(calificaciones)
    mediana=median(calificaciones)

    stdout.write(f"El promedio de {calificaciones} es {round(prome,1)} \n")
    stdout.write(f"La mediana de {calificaciones} es {mediana} \n")
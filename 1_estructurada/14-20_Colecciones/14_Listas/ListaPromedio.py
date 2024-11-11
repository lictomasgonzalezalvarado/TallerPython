from statistics import mean
from sys import stdout

if __name__ == '__main__':
    materas=["Español","Matemáticas","Químinca","Física","Computación","Educación Física","Biología"]
    calificaciones=[]

    nombre = input("Escribe tu nombre: ")

    for asignatura in materas:
        calif=int(input(f"Dame la calificación de {asignatura}: "))
        calificaciones.append(calif)

    prome = mean(calificaciones)
    print(f"el promedio de {nombre} es {round(prome,1)}")


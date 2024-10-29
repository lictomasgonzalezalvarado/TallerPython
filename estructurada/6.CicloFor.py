import sys
from os.path import split
from os.path import join

if __name__ == "__main__":
    for i in range(10):
        print(f"{i}")

    print("--------------------")
    for j in range(1,20):
        print(f"{j}", end=" ") # Esto end=" " se usa para anular el salto de línea

    sys.stdout.write("Texto sin salto de línea ") #Función utilizada para imprimir en pantalla sin salto de línea.

    print("--------------------")
    lista={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}

    for elemento in lista:
        print(elemento)

    lista2 = ["Federico", "Pablo", "Karla"]
    cadena:str=' '.join(lista2)#la función join se utiliza para
    print(cadena)
    separado=cadena.split()
    for dato in separado:
        print(dato)
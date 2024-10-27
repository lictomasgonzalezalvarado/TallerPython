import sys

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
    #la función join se utiliza para
    print(" ".join(lista2)) #El punto se utiliza para concatenar lo qeu retorne una función.
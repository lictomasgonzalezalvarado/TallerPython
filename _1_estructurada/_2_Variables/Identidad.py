if __name__ == '__main__':
    valor1:str="Hola Mundo de Hoy "*360
    valor2:str="Hola Mundo de Hoy "*360

    print(valor1)
    print(valor2)
    print("")
    print("Dirección de memoria de valor1: ",id(valor1))
    print("Dirección de memoria de valor2: ",id(valor2))

    if valor1 == valor2:
        print("Ambas cadenas son iguales")
    else:
        print("Ambas cadenas no son iguales")

    if valor1 is valor2: #Compara referencias de memoria
        print("Ambas cadenas están en la misma referencia de memoria")
    else:
        print("Ambas cadenas están en diferentes referencias de memoria")

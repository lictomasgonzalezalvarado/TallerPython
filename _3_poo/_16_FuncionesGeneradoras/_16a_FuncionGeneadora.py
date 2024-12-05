def generador1(num:int):
    print("Objeto generador 1")
    for i in range(0,num):
        return i

def generador2(num:int):
    print("\nObjeto generador 2")
    for i in range(0,num):
        print(i)


def generador3(num:int) -> list:
    print("\nObjeto generador 3")
    lista = []
    for i in range(0,num):
        lista.append(i)
    return lista

if __name__ == '__main__':
    print(generador1(20))
    print(generador2(20))

    for valor in generador3(20):
        print(valor)
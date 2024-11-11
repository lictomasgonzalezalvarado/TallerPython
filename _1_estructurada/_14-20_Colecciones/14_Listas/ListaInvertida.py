from sys import stdout

if __name__ == '__main__':
    lista=[]
    lista.append(8)
    lista.append(10)
    lista.append(9)
    lista.append(7)
    lista.append(11)
    lista.append(25)
    lista.append(33)

    print("************* Lista original ************")
    for elemento in lista:
        stdout.write(str(elemento) + ", ") # se imprime la lista original

    print("\n\n********* Lista Invertida *************")
    lista.reverse()
    for elemento in lista:
        stdout.write(str(elemento) + ", ") #se imprime la lista invertida
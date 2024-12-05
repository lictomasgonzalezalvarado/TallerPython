if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    listaImpares=list(filter(lambda x: x%2==0,numeros))
    listaPares=list(filter(lambda x: x%2==1,numeros))

    print(f"Lista de números pares: {listaPares}")
    print(f"Lista de numeros imapres: {listaImpares}")

    #Pero si antes aplicamos potencia y despues separamos en pares e impares
    listaImparesConPotencia=list(map(lambda z:z**2,filter(lambda t: t%2==1,numeros)))

    list(map(lambda x: print(x),listaImparesConPotencia))
    print("Numeros mayores a 200")
    list(map(lambda x: print(x),filter(lambda y: y > 200,listaImparesConPotencia)))

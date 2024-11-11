def cuadrado(x:int)-> int:
    return x**2

def Potencia(x:int,y:int) ->int:
    return x**y

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10] #Esto es una lista


    cuadrado=list(map(cuadrado,numeros))
    print(cuadrado)

    cubo=list(map(lambda x: Potencia(x, 3), numeros))
    print(f"El cubo de cada elemento es: {cubo}")

    cuarta=list(map(lambda x: x**4, numeros))
    print(f"La cuarta de cada elemento es: {cuarta}")

    edades = (12, 17, 18, 21, 15, 12, 23, 38, 10) #Esto es una tupla
    categorias = list(map(lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad", edades))

    print(categorias)
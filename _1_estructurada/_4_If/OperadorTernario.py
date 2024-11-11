#Estructura:
#     resultado = valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa

if __name__ == '__main__':
    edad = 18
    mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
    print(mensaje)


    edades = [12, 17, 18, 21, 15]


    categorias = list(map(lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad", edades))

    print(categorias)
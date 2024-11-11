from sys import stdout

if __name__ == '__main__':
    stdout.write("Proporciona un número de la semana: ")
    numero=int(input())

    if numero>=1 and numero<=7:
        dias={ #Esto es un diccionario
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sabado",
            7: "Domingo"
        }
        #print(dias[9]) #Busca una clave: Salida 'SyntaxError: invalid syntax' ya que la clave no existe
        #print(dias.get(9,"")) #Busca una clave: Salida '' ya que la clave no existe pero no marca error
        dia=dias[numero]

        stdout.write(f"El dia dela semana seleccionado es {dia}")
    else:
        stdout.write("Dia de la semana no valido")


class Calculadora:
    def __init__(self, n1, n2): #Este es un constructor con 2 pasos de parámetros.
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

    def saludo1(self, name: str): #Este metodo debe invocarse estrictamente con un argumento.
        print(f"¡Hola {name}!")

    def saludo2(self, name: str=None): #Este metodo puede invocarse  con o sin argumento.
        if name is not None:
            print(f"¡Hola {name}!")
        else:
            print("Hola desconocido")

    def saludo3(self, valor: str|int): #Este metodo puede invocarse  con o sin argumento.
        if isinstance(valor, str):
            print(f"¡Hola {valor}!")
        elif isinstance(valor, int):
            print(f"potencia es {valor**2}")
        else:
            print("Tipo de dato no valido")

    def saludo4(self, valor: str|int|float = None): #Este metodo puede invocarse  con o sin argumento.
        if valor is not None:
            if isinstance(valor, str):
                print(f"¡Hola {valor}!")
            elif isinstance(valor, int):
                print(f"potencia es {valor**2}")
            else:
                print(f"el número real es {valor}")
        else:
            print("Valor predeterminado Cuando como No Conozco")

obj = Calculadora(5,8)

print(obj.suma)
print(obj.resta)
print(obj.producto)
print(obj.division)

obj.saludo1("Manuel")
obj.saludo2()
obj.saludo2("Hector")
obj.saludo3("Jose Fausto Antonio")
obj.saludo3(9)

obj.saludo4("Ganriela")
obj.saludo4(12)
obj.saludo4(11.65)
obj.saludo4()


from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("Elegiste el color Rojo")
    case Color.GREEN:
        print("Elegiste el color verde")
    case Color.BLUE:
        print("Elegiste el color Azul")
import json
import sys

if __name__ == "__main__":
    # Definición de códigos ANSI
    RESET = "\033[0m"  # Restablece el color a su valor por defecto

    # Colores de texto
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Colores de fondo
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Abre el archivo JSON en modo de lectura con codificación UTF-8
    archivo = open("datos.json", "r", encoding="utf-8")
    try:

        # Carga el contenido del archivo JSON
        datos = json.load(archivo)

        # Recorre la lista de personas e imprime cada una
        i=1
        for persona in datos["personas"]:
            match i:
                case 1:
                    sys.stdout.write(RED)
                case 2:
                    sys.stdout.write(GREEN)
                case 3:
                    sys.stdout.write(BLUE)
                case _:
                    sys.stdout.write(RESET)

            print("Nombre:", persona["nombre"])
            print("Edad:", persona["edad"])
            print("Ciudad:", persona["ciudad"])
            print("Estado:", persona["estado"])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  # Línea en blanco para separar cada persona
            i+=1

    except FileNotFoundError:
        print("¡Error! El archivo no existe.")
    except json.JSONDecodeError:
        print("¡Error! El archivo no contiene un JSON válido.")
    except Exception as e:
        print("Pues no se que ocurrió:", e)
    finally:
        # Cierra el archivo manualmente
        archivo.close()
        print(RESET,"archivo Json cerrado")
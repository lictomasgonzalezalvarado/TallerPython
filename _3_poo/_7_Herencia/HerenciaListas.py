
class Biblioteca: # Clase base
    def __init__(self): #Constructor de lc clase base
        self.libros = []  # Lista para almacenar libros

    def addLibro(self, libro): #Metodo par agregar libros
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado a la biblioteca.")

    def showLibros(self): #Metodo para mostar lista de libros
        if self.libros:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print("La biblioteca está vacía.")


class BibliotecaDigital(Biblioteca): # Clase derivada
    def __init__(self): #Constructor de la clase derivada
        super().__init__() #Invocando el constructor de la clase base
        self.libros_descargados = []  # Lista para almacenar libros descargados

    def descargar_libro(self, libro):
        if libro in self.libros:
            self.libros_descargados.append(libro)
            print(f"Libro '{libro}' descargado.")
        else:
            print(f"El libro '{libro}' no está disponible en la biblioteca.")

    def mostrar_libros_descargados(self):
        if self.libros_descargados:
            print("Libros descargados:")
            for libro in self.libros_descargados:
                print(f"- {libro}")
        else:
            print("No hay libros descargados.")


if __name__ == '__main__':
    # Uso de la herencia
    biblioteca_digital = BibliotecaDigital()
    biblioteca_digital.addLibro("Python para Todos")
    biblioteca_digital.addLibro("Estructuras de Datos en Java")

    biblioteca_digital.showLibros()

    biblioteca_digital.descargar_libro("Python para Todos")
    biblioteca_digital.mostrar_libros_descargados()

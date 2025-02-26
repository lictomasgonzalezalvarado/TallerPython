# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase derivada
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.carrera = carrera

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llamamos al método de la clase base
        print(f"Carrera: {self.carrera}")

if __name__ == '__main__':

    # Uso de la herencia
    estudiante = Estudiante("Carlos", 20, "Ingeniería en Sistemas")
    estudiante.mostrar_informacion()

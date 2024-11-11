class Persona:
    def __init__(self, nombre, edad):
        # Inicialización de los atributos
        self._nombre = nombre
        self._edad = edad

    @property
    def getNombre(self):
        return self._nombre

    @property
    def getEdad(self):
        return self._edad

    def setNombre(self,nombre):
        self._nombre = nombre
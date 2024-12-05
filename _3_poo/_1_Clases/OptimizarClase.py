class Datos:
    # No se pueden añadir atributos
    # Menor consumo de memoria
    # Acceso más rápido a los atributos
    # Control sobre los atributos
    __slots__=('nombre','correo','whatsapp')

    def __init__(self, nombre, correo, whatsapp):
        self.nombre = nombre
        self.correo = correo
        self.whatsapp = whatsapp



if __name__ == '__main__':
    datos=Datos('Tomas','csctomasgonzalez@gmail.com','2481225850')

    print(datos.nombre)


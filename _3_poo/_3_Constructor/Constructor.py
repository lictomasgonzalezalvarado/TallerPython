class Ropa:
    def __init__(self, marca='Willow', talla='M', color='Rojo'):  # Este es el constructor sobrecargado y tiene  3 argumentos
        self.marca = marca
        self.talla = talla
        self.color = color

    def __str__(self):
        return self.marca + " - " + self.talla + " - " + self.color

    def __del__(self):
        print('Borrando ',self.__str__())

if __name__ == '__main__':
    camisa = Ropa("Panam","G", "Verde") #Esta es la instancia de clase
    camisaGenerica = Ropa()

    print(camisa)
    del camisa #Eliminando la instancia de clase
    print(camisaGenerica)
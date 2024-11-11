class Ropa:
    def __init__(self): #Este es el constructor y no tiene argumentos
        self.marca = 'Willow' #Estos son los atributos
        self.talla = 'M'
        self.color = 'Rojo'

    def __init__(self, marca, talla, color):  # Este es el constructor sobrecargado y tiene  3 argumentos
        self.marca = marca
        self.talla = talla
        self.color = color

camisa = Ropa("Panam","G", "Verde") #Esta es la instancia de clase

print(camisa.marca)
print(camisa.talla)
print(camisa.color)
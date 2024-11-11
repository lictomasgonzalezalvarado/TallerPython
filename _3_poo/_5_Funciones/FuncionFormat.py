#https://youtu.be/ElObT5rOx2M?si=jEK1loPvi8qkYear
#jacklyon
class Persona:
    pass #indicativo que por el momento no hay atributos

    def __init__(self,nombre, año): #esto es un constructor con dos parámetros
        self.nombre = nombre
        self.año = año

    def descripcion(self): #esto es un méodo
        return '{} tiene {} años'.format(self.nombre,self.año) #la función format ayuda a dar formato a una salida

    def comentario(self, frase): #esto es un método con un paso de parámetros.
        return '{} dice {}'.format(self.nombre, frase)




obj = Persona('Rafael',32)

print(obj.descripcion())
print(obj.comentario('que asistirá a la reunión'))

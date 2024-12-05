class BombaInfusion:
    def __init__(self):
        self.__dosis_hora =250
    #utilizar doble guion bajo (__) antes de un atributo no lo hace "privado"
    #el uso de __ activa el mecanismo de name mangling (ofuscación de nombres)
    #Python renombra internamente el atributo __dosis_hora. Denomiando ahora _BombaInfusion__dosis_hora
    #Esto evita que el atributo sea accedido directamente desde fuera de la clase

    @property   #Esto convierte el metodo en una propiedad de solo lectura
    def dosis_hora(self):
        return self.__dosis_hora

    @dosis_hora.setter   #Esto convierte el metodo en una propiedad de solo escritura
    def dosis_hora(self, dosis_hora):
        self.__dosis_hora = dosis_hora


if __name__ == '__main__':
    dosificador=BombaInfusion()
    # dosificador.dosis_hora='120'

    print(dosificador.dosis_hora)
    #print(dosificador._BombaInfusion__dosis_hora) #Finalmente esta es la manera de acceder al atributo con doble guion bajo
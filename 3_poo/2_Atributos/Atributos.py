class Archivo:
    # archivo:str #Esto es un atributo de tipo String
    estado:bool #En pyton todos los atributos son publicos
    tamannio:int #Esto es un atributo de tipo entero
    path:str
    def __init__(self):
        self.archivo:str="datos.txt"
        self.estado=False
        self.tamannio=566
        self.path="c:\\archivos de programa"



if __name__ == '__main__':
    archivo=Archivo() #Esta es una instancia de la clase Arhivo.
    print(archivo.tamannio)
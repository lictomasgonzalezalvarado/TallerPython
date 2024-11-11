from math import sqrt
from random import Random

class Opercaciones:
    def __init__(self, valor1, valor2, valor3):
        self.a:float= valor1
        self.b:float= valor2
        self.c:float= valor3

    def Mensaje(self):
        print("Esta clase resuelve la fórmula general")

    def Potencia(self):
        return self.b**2

    def Multiplicacion(self):
        return 4 * self.a * self.c

    def Raiz(self):
        return sqrt(self.Potencia() - self.Multiplicacion())

    def Division(self, x:float,y:float):
        return  x/y

    def Res(self):

        x1:flota = self.Division(-self.b + self.Raiz(),2 * self.a)
        x2:float = self.Division(-self.b - self.Raiz(),2 * self.a)
        return x1,x2 #Se devuelven los valores un una tupla

if __name__ == '__main__':
    general=Opercaciones(500,1200,-800)
    general.Mensaje()
    x1,x2=general.Res()
    print(f"x1= {x1}")
    print(f"x2= {x2}")
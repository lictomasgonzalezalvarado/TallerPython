from math import sqrt, pow

def factorial(n:float)-> float:
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

class FormulaGenereral:
    def __init__(self,a:float, b:float, c:float):
        self.a:float=a
        self.b:float=b
        self.c:float=c

    def _potencia(self):
        return pow(self.b,2)

    def _multiplicacion3(self):
        return 4 * self.a * self.c

    def _multiplicacion2(self):
        return 2 * self.a

    def _radicando(self):
        return self._potencia() - self._multiplicacion3()

    def _raiz(self):
        return sqrt(self._radicando())

    def solucion(self)-> tuple[float, float]:
        x1=(-self.b + self._raiz()) / self._multiplicacion2()
        x2=(-self.b - self._raiz()) / self._multiplicacion2()

        return round(x1,3),round(x2,3)

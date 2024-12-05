from paquetematematicas.paqueteavanzadas.funcionesavanzadas import *
from paquetematematicas.paqueteavanzadas.otrasfunciones import *

if __name__ == '__main__':
    general=FormulaGenereral(12,220,132)
    escribeln(SALUDO,ColorANSI.AZUL_CLARO)

    x1,x2=general.solucion()
    escribeln(f"Resultado formula general. x1= {x1}. x2={x2}")

    res=factorial(5)
    escribeln(f"El factorial de 5 es {res}",ColorANSI.VERDE)
    escribeln(f"El factorial de 5 es {res}",ColorANSI.ROJO)
    escribeln(f"El factorial de 5 es {res}",ColorANSI.AMARILLO)
    escribe(f"El factorial de 5 es {res}",ColorANSI.AZUL_CLARO)

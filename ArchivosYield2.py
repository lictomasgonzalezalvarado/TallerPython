import os
from os import times_result


def CarpetasPrincipales(rutaAbsoluta,carpetasExcluidas)->list[str]:
    for rutaPrincipal, subcarpetas, archivos in os.walk(rutaAbsoluta):
        subcarpetas = list(filter(lambda carpeta: carpeta not in carpetasExcluidas,subcarpetas))
        return subcarpetas

def Subcarpetas(rutaAbsoluta,carpetasExcluidas)->list[str]:
    for subcarpetas in CarpetasPrincipales(rutaAbsoluta, carpetasExcluidas):
        #rint(f'{rutaAbsoluta}\\{carpeta}')
        for rutaPrincipal, subsubcarpetas, archivos in os.walk(subcarpetas):
            if len(subsubcarpetas)>0:
                yield subsubcarpetas



if __name__ == '__main__':
    rutaAbsoluta = os.path.abspath(__file__)
    rutaAbsoluta = os.path.dirname(rutaAbsoluta)

    carpetasExcluidas = ['.env', '.git', '.idea','.venv']

    #print(rutaAbsoluta)
    print("")

    #with open("lista_carpetas.txt", "w") as f:
    for listadeSubcarpetas in Subcarpetas(rutaAbsoluta,carpetasExcluidas):
        for subcarpeta in listadeSubcarpetas:
            print(f"{rutaAbsoluta}\\{carpeta}\\{subcarpeta}")
                #f.write(f"{rutaAbsoluta}\\{carpeta}\\{subcarpeta}\n")

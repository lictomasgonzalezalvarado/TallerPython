import os

def carpetasprincipales(rutaAbsoluta:str,carpetasexcluidas:list[str])->list[str]:
    for rutaPrincipal, subcarpetas, archivos in os.walk(rutaAbsoluta):
        subcarpetas = list(filter(lambda carpeta: carpeta not in carpetasexcluidas,subcarpetas))
        return subcarpetas

def subcarpetas(rutasubcarpeta:str)->list[str]:
    for rutaPrincipal, subsubcarpetas, archivos in os.walk(rutasubcarpeta):
        if len(subsubcarpetas)>0:
            yield subsubcarpetas


if __name__ == '__main__':

    rutaAbsoluta = os.path.abspath(__file__)
    rutaAbsoluta = os.path.dirname(rutaAbsoluta)

    carpetasExcluidas = ['.env', '.git', '.idea','.venv']

    #print(rutaAbsoluta)
    print("")

    with open("lista_carpetas.txt", "w") as f:
        for carpeta in carpetasprincipales(rutaAbsoluta,carpetasExcluidas):
            rutacarpeta:str=rutaAbsoluta+"\\"+carpeta
            print(rutacarpeta)
            f.write(f'{carpeta}\n')
            for listadeSubcarpetas in subcarpetas(rutacarpeta):
                for subcarpeta in listadeSubcarpetas:
                    print(f"{rutacarpeta}\\{subcarpeta}")
                    f.write(f"{carpeta}\\{subcarpeta}\n")

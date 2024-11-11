from os import path
from pathlib import Path as PATH_ALIAS

if __name__ == '__main__':

    # Opción 1 para establecer la ruta
    ruta_principal = "F:\\Docencia ITSSMT\\AGO-DIC 2024\\Arq de Comp\\TallerPyton\\1_estructurada\\11_Archivos"

    # Opción 2 para establecer la ruta
    ruta_principal2 = r"F:\Docencia ITSSMT\AGO-DIC 2024\Arq de Comp\TallerPyton\1_estructurada\11_Archivos"

    # Opción 3 para establecer la ruta
    ruta_principal3 = F"F:/Docencia ITSSMT/AGO-DIC 2024/Arq de Comp/TallerPyton/1_estructurada/11_Archivos"

    # Opción 4 para establecer la ruta
    ruta_principal4 = path.join("F:\\","Docencia ITSSMT","AGO-DIC 2024","Arq de Comp","TallerPyton","1_estructurada","11_Archivos")

    # Opción 5 para establecer la ruta
    ruta_principal5 = PATH_ALIAS("F:/Docencia ITSSMT/AGO-DIC 2024/Arq de Comp/TallerPyton/1_estructurada/11_Archivos")

    #Obtener el path actual
    ruta_con_archivo=path.abspath(__file__)
    directorio =path.dirname(ruta_con_archivo)

    print("opción 1 ",ruta_principal)
    print("opción 2 ",ruta_principal2)
    print("opción 3 ",ruta_principal3)
    print("opción 4 ",ruta_principal4)
    print("opción 5 ",ruta_principal5)
    print("Path Actual  ",directorio)
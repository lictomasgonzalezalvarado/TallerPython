#La clase path del módulo os se utiliza para realizar operaciones
# relacionadas con las rutas de archivos y directorios
from os import path

#La clase walk del módulo os se utiliza para recorrer un directorio y sus subdirectorios
# de manera recursiva, generando los nombres de los archivos y subdirectorios en un árbol de directorios
from os import walk

if __name__ == '__main__':

    # Establecer la ruta actual
    ruta_con_archivo=r"F:\Docencia ITSSMT\AGO-DIC 2024\Arq de Comp\TallerPyton\estructurada\\"#path.abspath(__file__)
    ruta_principal = path.dirname(ruta_con_archivo)
    print(ruta_principal)

    # Lista para almacenar los nombres de las carpetas
    lista_carpetas = []
    #Lista de subcarpetas excluidas
    excluir_carpetas = ['.env', '.git', '.idea']

    # Recorre solo el primer nivel de carpetas en la ruta principal
    for carpeta_ruta, subcarpetas, archivos in walk(ruta_principal):
        # Filtra las subcarpetas que no están en la lista de exclusión
        subcarpetas = [subcarpeta for subcarpeta in subcarpetas if subcarpeta not in excluir_carpetas]

        # Agrega las carpetas en el nivel principal a la lista
        for subcarpeta in subcarpetas:
            # Obtiene la ruta relativa de la carpeta
            ruta_relativa = path.relpath(path.join(carpeta_ruta, subcarpeta), ruta_principal)
            lista_carpetas.append(ruta_relativa)

        # Detiene el recorrido después del primer nivel
        break


    # Guarda la lista en un archivo de texto
    with open("lista_carpetas.txt", "w") as f:
        for carpeta in lista_carpetas:
            f.write(f"{carpeta}\n")

    print("Lista de carpetas generada en 'lista_carpetas.txt'")
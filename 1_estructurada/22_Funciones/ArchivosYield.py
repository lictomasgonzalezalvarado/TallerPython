import os

def my_walk(directorio):
    # Lista de archivos y subdirectorios dentro del directorio dado
    for dirpath, dirnames, filenames in os.walk(directorio):
            # Generamos la tupla como 'os.walk()' devuelve
            yield dirpath, dirnames, filenames

if __name__ == '__main__':
    ruta_con_archivo = r"F:\Docencia ITSSMT\AGO-DIC 2024\Arq de Comp\TallerPyton"#os.path.abspath(__file__)
    for ruta, subcarpetas, archivos in my_walk(ruta_con_archivo):
        for carpeta in subcarpetas:
            print(f'{ruta}\\...{carpeta}...\\{archivos}')
            #print(f'Subdirectorios: {subcarpetas}')
            #print(f'Archivos: {archivos}')
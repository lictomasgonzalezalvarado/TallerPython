#Argumentos clave valor

def Argumentos(**args):
    if args: #El tipo de dato de argumentos es un diccionario
        for clave,valor in args.items():
            print(f"{clave}- {valor}")
    else:
        print("No hay argumentos")


def ArgumentosKeys(**args):
    if args: #El tipo de dato de argumentos es un diccionario
        for clave in args.keys():
            print(f"{clave}")
    else:
        print("No hay argumentos")

def ArgumentoClaveComprehension(**args):
    separador=","
    columnas = separador.join([f"{col}=%s" for col in args.keys()]) #Esto es un generador comprehension que guarda cada elemento en una lista
    print(columnas)

if __name__ == '__main__':
    # Argumentos(Nombre="Javier", ap="Juarez", am="Mendieta", edad=35)
    # ArgumentosKeys(Nombre="Javier", ap="Juarez", am="Mendieta", edad=35)
    ArgumentoClaveComprehension(Nombre="Javier", ap="Juarez", am="Mendieta", edad=35)
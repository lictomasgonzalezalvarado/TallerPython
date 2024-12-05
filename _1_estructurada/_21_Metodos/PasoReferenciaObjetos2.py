def agregar_elemento(diccionario):
    diccionario['nuevo'] = 'valor'

if __name__ == '__main__':
    mi_diccionario = {'original': 'datos'}

    agregar_elemento(mi_diccionario)

    print(mi_diccionario)
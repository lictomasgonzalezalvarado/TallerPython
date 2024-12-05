#Paso por referencia de objetos

def suma(a:int, b:int, lista:list):
    suma=a+b
    lista.append(a)
    lista.append(b)
    lista.append(suma)

def otraSuma(a:int, b:int, suma:int):
    suma=a+b

if __name__ == '__main__':
    miLista=[]

    suma(3,10,miLista)

    print(miLista)

    suma=0
    otraSuma(3,10,suma)
    print(suma)
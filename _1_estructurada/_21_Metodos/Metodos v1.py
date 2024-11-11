def suma (x:str,y:str):
    suma:str=x+y
    print(f"la suma de {x} + {y} es {suma}")

if __name__ == '__main__':
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese otro numero: "))

    suma(a,b)
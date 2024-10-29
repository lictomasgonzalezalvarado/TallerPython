#Muestra la potencia de un numero X a la Y
if __name__ == "__main__":
    print("Este programa calcula la potencia de x a la y")
    x=int(input("Proporciona el valor de la base "))
    y=int(input("Proporciona el valor de la potencia "))

    i=1
    resultado=1
    while i<=y:
        print(f"Conteo {i}")
        resultado*=x
        i+=1;

    print(f"El resultado de  {x} a la  {y} es {resultado}")

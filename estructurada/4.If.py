if __name__ == "__main__":
    a=int(input("Proporciona el valor de A "))
    b=int(input("Proporciona el valor de B "))
    c=int(input("Proporciona el valor de C "))

    if a>b:
        if a>c:
            print("El mayor es ",a)
        else:
            print(f"El mayor es {b}")
    elif b>c:
        print(f"El mayor es {b}")
    else:
        print(f"El mayor es {c}")




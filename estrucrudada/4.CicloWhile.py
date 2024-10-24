if __name__ == "__main__":
    fact=1
    num=int(input("Proporciona un numero "))
    valor=num
    while (num>0):
        fact=fact*num
        num-=1
    print(f"El fatorial de {valor} es {fact}")

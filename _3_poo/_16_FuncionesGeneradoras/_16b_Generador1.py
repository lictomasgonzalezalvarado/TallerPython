def generador1():
    for i in range(0,20):
        yield i

def generador2():
    for i in range(0,20):
        if i%2 == 0:
            yield f"{i} es par"
        else:
            yield f"{i} es impar"

if __name__ == '__main__':

    rango1=generador1()
    rango2=generador2()

    print(type(rango1))

    # print(next(rango1))
    # print(next(rango1))
    # print(next(rango1))
    # print(next(rango1))

    print(next(rango2))
    print(next(rango2))
    print(next(rango2))
    print(next(rango2))
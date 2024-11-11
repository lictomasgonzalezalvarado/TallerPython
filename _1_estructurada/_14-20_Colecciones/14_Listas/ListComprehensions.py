#https://ellibrodepython.com/list-comprehension-python

if __name__ == '__main__':
    #de forma tradicional
    cuadrados = []
    for i in range(5):
        cuadrados.append(i ** 2)

    #Con List Comprehension
    cuadrados = [i ** 2 for i in range(5)]
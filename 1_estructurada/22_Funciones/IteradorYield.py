
def contar_hasta(n)->tuple[str,int]:
    count = 1
    potencia=0
    while count <= n:
        potencia=count**2
        yield (f"valor: {count}",potencia)  # Pausa la función y devuelve el valor de count y potencia
        count += 1

if __name__ == '__main__':
    # Usando la función generadora
    for numero, potencia in contar_hasta(5):
        print(f"Para {numero} su potencia es {potencia}")
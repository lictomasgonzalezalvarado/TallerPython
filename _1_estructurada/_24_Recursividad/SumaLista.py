from typing import List
def SumaRecursiva(lista: List[int], indice: int = 0) -> int:
    if indice == len(lista):
        return 0
    return lista[indice] + SumaRecursiva(lista, indice + 1)

if __name__ == '__main__':
    numeros: List[int]=[10,56,2,98,74,12,56,32,65,12,45]

    suma:int =SumaRecursiva(numeros)
    print(f"La suma de {numeros} es {suma}")
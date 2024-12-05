from math import pow
pi=3.1416

def areacuadrado(base:float, altura:float)-> float:
    return base * altura

def areatriangulo(base:float, altura:float)-> float:
    return (base*altura)/2

def circulo(radio:float)-> float:
    return pi * pow(radio, 2)

def areatrapecio(baseMayo:float, baseMenor:float,altura:float)->float:
    return ((baseMayor + baseMenor) * altura) / 2

def areapentagono(apotema: float, perimetro: float)-> float:
    return (perimetro * apotema) / 2
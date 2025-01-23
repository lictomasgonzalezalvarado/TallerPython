if __name__ == '__main__':
    #Los sets son colecciones deordenadas de objetos únicos
    canasta = {'manzana','platano','pera','manzana','naranja','pera'}
    print(canasta)

    numeros={1,3,5,8,3,4,12,1}
    print(numeros)
    a=set('abradacabra')
    print(a)

    #Existen dos tipos de sets
    #Tipo 1: Sets Mutables (Se pueden añadir nuevos elementos)
    a = set('abradacabra')
    print(a)
    a.add('g')
    print(a)

    #Tipo 2: Sets inmutables (No se pueden añadir nuevos elementos)
    b=frozenset('perro')
    print(b)
    #b.add('k') #'frozenset' object has no attribute 'add'

    #Operaciones con los sets
    #Intersección
    #miSet={1,2,3,4,5,5}.intersection({3,4,5,6}) #opción 1
    miSet={1,2,3,4,5,6} & {3,4,5,6} #opción 2
    print("Intersección ",miSet)

    #Unión
    #miSet={1,2,3,4,5,6}.union({3,4,5,6}) #Opción 1
    miSet={1,2,3,4,5,6} | {3,4,5,6} #opción 2
    print("Union ",miSet)

    #miSet={1,2,3,4}.difference({2,3,5}) #opción 1
    miSet = {1, 2, 3, 4}-{2, 3, 5} #Opción 2
    print("Diferencia ",miSet)

    MiSet = {1,2,3,4,5,6}.symmetric_difference({2,3,5})
    print("Diferencia Simétrica ",MiSet)

    miSet={1,2,3,4,5}.issuperset({1,2,3})
    print("Verifica si es super set: ",miSet)

    miSet = {1, 2}.issubset({1, 2, 3})
    print("Verifica si es subset set: ", miSet)



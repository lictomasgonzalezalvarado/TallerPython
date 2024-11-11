if __name__ == '__main__':
    desordenado=[(100,'a','Guadalajara'),(39,'c','Queretaro'),(5,'b','Puebla'),(26,'d','Veracruz')]
    Odenar=list(sorted(desordenado,key=lambda x:x[0]))

    print(Odenar)
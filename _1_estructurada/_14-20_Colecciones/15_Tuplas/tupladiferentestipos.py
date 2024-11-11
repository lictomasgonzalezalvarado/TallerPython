if __name__ == '__main__':
    #Una tupla es una estructura para almacenar una colección de valore y ésta es inmutable.
    persona = ("Ana", 25, 1.75) # Tupla con diferentes tipos de datos

    nombre = persona[0] #Extrayendo el primer valor de la tupla
    edad = persona[1] #Extrayendo el segundo valor de la tupla
    altura = persona[2] #Extrayendo el tercero valor de la tupla

    print(f"Tipo de Dato de nombre: {type(nombre)}. Y su valor es {nombre}")
    print(f"Tipo de Dato de edad: {type(edad)}. Y su valor es {edad}")
    print(f"Tipo de Dato de altura: {type(altura)}. Y su valor es {altura} '\n\n")

    nombre2, edad2, altura2 = persona #Extrayendo los valores de la tupla en una sola línea
    print(f"Tipo de Dato de nombre: {type(nombre)}. Y su valor es {nombre}")
    print(f"Tipo de Dato de edad: {type(edad)}. Y su valor es {edad}")
    print(f"Tipo de Dato de altura: {type(altura)}. Y su valor es {altura}")
if __name__ == '__main__':
    # Nombre del archivo de texto
    nombre_archivo = "C:\\Users\\Socrates\\Documents\\Intercambio\\mensaje.txt"

    # Frase a guardar en el archivo
    frase = "Hola Mundo de los developers"

    try:
        # Abre el archivo en modo escritura (crea el archivo si no existe)
        with open(nombre_archivo, "w") as archivo:
            # Escribe la frase en el archivo
            archivo.write(frase)
        print(f"La frase se ha guardado exitosamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Se produjo un error al intentar guardar la frase: {e}")
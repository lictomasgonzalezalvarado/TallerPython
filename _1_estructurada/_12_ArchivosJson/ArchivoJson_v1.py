if __name__ == "__main__":
    #Versión corta de abrir un archivo Json
    # Abre el archivo JSON en modo de lectura y with se encarga de cerrarlo de forma automática
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) # Carga el contenido del archivo JSON

    # Muestra el contenido del JSON
    for persona in datos["personas"]:
        print("Nombre:", persona["nombre"])
        print("Edad:", persona["edad"])
        print("Ciudad:", persona["ciudad"])
        print("Estado:", persona["estado"])
        print("-------------------------")  # Línea en blanco para separar cada persona
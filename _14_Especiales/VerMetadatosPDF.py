import PyPDF2


def ver_metadatos_pdf(ruta_pdf):
    try:
        # Abrir el archivo PDF en modo lectura binaria
        with open(ruta_pdf, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)  # Crear un lector de PDF

            # Obtener los metadatos del archivo PDF
            metadatos = lector_pdf.metadata

            if metadatos:
                print("Metadatos del archivo PDF:")
                for clave, valor in metadatos.items():
                    print(f"{clave}: {valor}")

                # Mostrar detalles específicos de modificación
                if '/ModDate' in metadatos:
                    print(f"Fecha de última modificación: {metadatos['/ModDate']}")
                if '/Producer' in metadatos:
                    print(f"Producto/Programa que modificó el archivo: {metadatos['/Producer']}")
                if '/Creator' in metadatos:
                    print(f"Programa/Usuario que creó el archivo: {metadatos['/Creator']}")
            else:
                print("El archivo PDF no contiene metadatos.")

    except FileNotFoundError:
        print("Error: El archivo PDF no fue encontrado. Verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def eliminar_metadatos_pdf(ruta_pdf, salida_pdf):
    try:
        # Abrir el archivo PDF en modo lectura binaria
        with open(ruta_pdf, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)  # Crear un lector de PDF

            # Crear un escritor de PDF para el nuevo archivo sin metadatos
            escritor_pdf = PyPDF2.PdfWriter()

            # Copiar todas las páginas del archivo original al nuevo archivo
            for pagina in lector_pdf.pages:
                escritor_pdf.add_page(pagina)

            # No añadir metadatos al nuevo archivo (eliminación efectiva)
            escritor_pdf.add_metadata({})  # Se añade un diccionario vacío

            # Escribir el nuevo archivo PDF sin metadatos
            with open(salida_pdf, 'wb') as archivo_salida:
                escritor_pdf.write(archivo_salida)

            print("Metadatos eliminados correctamente.")
            print(f"Archivo limpio guardado en: {salida_pdf}")

    except FileNotFoundError:
        print("Error: El archivo PDF no fue encontrado. Verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def agregar_metadatos_pdf(ruta_pdf, salida_pdf, nuevos_metadatos):
    try:
        # Abrir el archivo PDF original en modo lectura binaria
        with open(ruta_pdf, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)  # Crear un lector de PDF

            # Crear un escritor de PDF para el nuevo archivo con metadatos
            escritor_pdf = PyPDF2.PdfWriter()

            # Copiar todas las páginas del archivo original al nuevo archivo
            for pagina in lector_pdf.pages:
                escritor_pdf.add_page(pagina)

            # Añadir nuevos metadatos al archivo
            escritor_pdf.add_metadata(nuevos_metadatos)

            # Guardar el nuevo archivo PDF con los metadatos añadidos
            with open(salida_pdf, 'wb') as archivo_salida:
                escritor_pdf.write(archivo_salida)

            print("Metadatos agregados correctamente.")
            print(f"Archivo con nuevos metadatos guardado en: {salida_pdf}")

    except FileNotFoundError:
        print("Error: El archivo PDF no fue encontrado. Verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    opc: int=1
    while not opc == 0:
        print("")
        print("1.-Ver Metadatos.")
        print("2.-Eliminar Metadatos.")
        print("3.-Agregar Metadatos.")
        print("0.- Salir")
        opc=int(input("Ingresa la opción deseada: "))
        if (opc >= 0) and (opc <=3):
            match opc:
                case 1:
                    ruta_pdf = input("Introduce la ruta del archivo PDF: ")
                    ver_metadatos_pdf(ruta_pdf)
                case 2:
                    ruta_pdf = input("Introduce la ruta del archivo PDF original: ")
                    salida_pdf = input("Introduce la ruta para guardar el PDF sin metadatos: ")
                    eliminar_metadatos_pdf(ruta_pdf, salida_pdf)
                case 3:
                    ruta_pdf = input("Introduce la ruta del archivo PDF original: ")
                    salida_pdf = input("Introduce la ruta para guardar el PDF con nuevos metadatos: ")

                    print("Introduce los nuevos metadatos para el PDF:")
                    nuevos_metadatos = {
                        '/Title': input("Título: "),
                        '/Author': input("Autor: "),
                        '/Subject': input("Asunto: "),
                        '/Creator': input("Creado por: "),
                        '/Producer': input("Aplicaicón utilizada: "),
                        '/CreationDate': input("fecha de creación: "),
                        '/ModDate': input("Fecha de la última modificación: "),
                    }

                    agregar_metadatos_pdf(ruta_pdf, salida_pdf, nuevos_metadatos)

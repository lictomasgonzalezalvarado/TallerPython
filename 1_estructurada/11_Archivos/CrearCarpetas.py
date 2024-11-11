import os

if __name__ == '__main__':
    # Lista de carpetas que deseas crear
    carpetas = [
        "10_Excepciones",
        "11_Archivos",
        "12_ArchivosJson",
        "13_ArchivosIni",
        "14-20_Colecciones",
        "1_MainPrincipal",
        "21_Metodos",
        "22_Funciones",
        "23_Recursividad",
        "2_Variables",
        "3_TiposDeDatos",
        "4_If",
        "5_CicloWhile",
        "6_CicloFor",
        "7_Match",
        "8_Modulos",
        "9_Diccionario",
        "14-20_Colecciones\\14_Listas",
        "14-20_Colecciones\\15_Tuplas",
        "14-20_Colecciones\\16_Conjuntos",
        "14-20_Colecciones\\17_Diccionario",
        "14-20_Colecciones\\18_Colas",
        "14-20_Colecciones\\19_NombreTuplas",
        "14-20_Colecciones\\20_Contador"
    ]

    # Especifica la ruta principal donde deseas crear las carpetas
    ruta_principal = os.path.abspath(__file__)  # Cambia esta ruta según tu preferencia
    ruta_principal = os.path.dirname(ruta_principal)
    print(ruta_principal)

    # Crea cada carpeta en la ruta especificada
    for carpeta in carpetas:
        ruta_completa = os.path.join(ruta_principal, carpeta)

        if not os.path.exists(ruta_completa):
            os.makedirs(ruta_completa, exist_ok=True)
            print(f"Carpeta creada: {ruta_completa}")

    print("Estructura de carpetas completada.")
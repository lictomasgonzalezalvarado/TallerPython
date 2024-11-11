import os

if __name__ == '__main__':
    # Lista de carpetas que deseas crear
    carpetas = [
        "10_principiossolid",
        "11_patronesdedisennio",
        "1_estructurada",
        "1_estructurada\\10_Excepciones",
        "1_estructurada\\11_Archivos",
        "1_estructurada\\12_ArchivosJson",
        "1_estructurada\\13_ArchivosIni",
        "1_estructurada\\14-20_Colecciones",
        "1_estructurada\\1_MainPrincipal",
        "1_estructurada\\21_Metodos",
        "1_estructurada\\22_Funciones",
        "1_estructurada\\23_Recursividad",
        "1_estructurada\\2_Variables",
        "1_estructurada\\3_TiposDeDatos",
        "1_estructurada\\4_If",
        "1_estructurada\\5_CicloWhile",
        "1_estructurada\\6_CicloFor",
        "1_estructurada\\7_Match",
        "1_estructurada\\8_Modulos",
        "1_estructurada\\9_Diccionario",
        "1_estructurada\\14_Listas",
        "1_estructurada\\15_Tuplas",
        "1_estructurada\\16_Conjunto",
        "1_estructurada\\17_Diccionario",
        "1_estructurada\\18_Colas",
        "1_estructurada\\19_NombreTupla",
        "1_estructurada\\20_Contador",
        "2_estructuradedatos",
        "2_estructuradedatos\\1_Pilas",
        "2_estructuradedatos\\2_Colas",
        "2_estructuradedatos\\3_Colas_Circulares",
        "2_estructuradedatos\\4_Listas_Enlazadas",
        "2_estructuradedatos\\5_Listas_Doblemente_Enlazadas",
        "2_estructuradedatos\\6_Arboles",
        "2_estructuradedatos\\7_Grafos",
        "3_poo",
        "3_poo\\10_Metodo__repr__",
        "3_poo\\11_Sobrecarga",
        "3_poo\\12_Interfaces",
        "3_poo\\12_Sobreesritura",
        "3_poo\\13_Polimorfismo",
        "3_poo\\1_Clases",
        "3_poo\\2_Atributos",
        "3_poo\\3_Constructor",
        "3_poo\\4_Metodos",
        "3_poo\\5_Funciones",
        "3_poo\\6_Propiedades",
        "3_poo\\7_Herencia",
        "3_poo\\8_Metodo__str__",
        "3_poo\\9_MarcadorPass",
        "4_basesdedatos",
        "4_basesdedatos\\1_ConectarMySql",
        "4_basesdedatos\\2_ConectarPostgreSQL",
        "4_basesdedatos\\3_ConectarSQLLite",
        "4_basesdedatos\\4_ConectarOracle",
        "4_basesdedatos\\5_ConectarSQLServer",
        "5_programacionfuncional",
        "6_interfazgrafica",
        "7_hilos",
        "8_net",
        "9_practicasdedisennio",
        "9_practicasdedisennio\\compositionoverInheritance",
        "9_practicasdedisennio\\dontrepeatyourself",
        "9_practicasdedisennio\\encapsulatewhatvaries",
        "9_practicasdedisennio\\failfast",
        "9_practicasdedisennio\\fluentinterface",
        "9_practicasdedisennio\\inmutability",
        "9_practicasdedisennio\\methodchaining",
        "9_practicasdedisennio\\selfencapsulatedfields",
        "9_practicasdedisennio\\yagni",
        "9_practicasdedisennio\\__pycache__",
        "9_practicasdedisennio\\__pycache__"
    ]

    # Especifica la ruta principal donde deseas crear las carpetas
    ruta_principal = os.path.abspath(__file__)  # Cambia esta ruta según tu preferencia
    ruta_principal = os.path.dirname(ruta_principal)
    # print(ruta_principal)

    for carpeta in carpetas:
        ruta_completa = os.path.join(ruta_principal, carpeta)
        # print(ruta_completa)

        if not os.path.exists(ruta_completa):
            os.makedirs(ruta_completa, exist_ok=True)
            print(f"Carpeta creada: {ruta_completa}")
        else:
            print(f"La carpeta {ruta_completa} ya existe")

    print("Estructura de carpetas completada.")
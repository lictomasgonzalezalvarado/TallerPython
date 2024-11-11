import os

if __name__ == '__main__':
    # Lista de carpetas que deseas crear
    carpetas = [
        "_10_principiossolid",
        "_10_principiossolid\\_1_singleresponsability",
        "_10_principiossolid\\_2_openclosed",
        "_10_principiossolid\\_3_liskovsustitution",
        "_10_principiossolid\\_4_interfacesegregation",
        "_10_principiossolid\\_5_dependencyinversion",
        "_11_patronesdedisennio",
        "_11_patronesdedisennio\\_10_decorador",
        "_11_patronesdedisennio\\_11_fachada",
        "_11_patronesdedisennio\\_12_pesomosca",
        "_11_patronesdedisennio\\_13_proxy",
        "_11_patronesdedisennio\\_14_cadenaderesponsabilidades",
        "_11_patronesdedisennio\\_15_iterador",
        "_11_patronesdedisennio\\_16_mediador",
        "_11_patronesdedisennio\\_17_dominio",
        "_11_patronesdedisennio\\_18_recuerdo",
        "_11_patronesdedisennio\\_19_observador",
        "_11_patronesdedisennio\\_1_metododefabrica",
        "_11_patronesdedisennio\\_20_estado",
        "_11_patronesdedisennio\\_21_estrategia",
        "_11_patronesdedisennio\\_22_plantilla",
        "_11_patronesdedisennio\\_23_visitante",
        "_11_patronesdedisennio\\_2_fabricaabstracta",
        "_11_patronesdedisennio\\_3_constructor",
        "_11_patronesdedisennio\\_4_prototipo",
        "_11_patronesdedisennio\\_5_unico",
        "_11_patronesdedisennio\\_6_fabrica",
        "_11_patronesdedisennio\\_7_adaptador",
        "_11_patronesdedisennio\\_8_puente",
        "_11_patronesdedisennio\\_9_compuesto",
        "_1_estructurada",
        "_1_estructurada\\_10_Excepciones",
        "_1_estructurada\\_11_Archivos",
        "_1_estructurada\\_12_ArchivosJson",
        "_1_estructurada\\_13_ArchivosIni",
        "_1_estructurada\\_14-20_Colecciones",
        "_1_estructurada\\_1_MainPrincipal",
        "_1_estructurada\\_21_Metodos",
        "_1_estructurada\\_22_Funciones",
        "_1_estructurada\\_23_Recursividad",
        "_1_estructurada\\_2_Variables",
        "_1_estructurada\\_3_TiposDeDatos",
        "_1_estructurada\\_4_If",
        "_1_estructurada\\_5_CicloWhile",
        "_1_estructurada\\_6_CicloFor",
        "_1_estructurada\\_7_Match",
        "_1_estructurada\\_8_Modulos",
        "_1_estructurada\\_9_Diccionario",
        "_1_estructurada\\_14_Listas",
        "_1_estructurada\\_15_Tuplas",
        "_1_estructurada\\_16_Conjunto",
        "_1_estructurada\\_17_Diccionario",
        "_1_estructurada\\_18_Colas",
        "_1_estructurada\\_19_NombreTupla",
        "_1_estructurada\\_20_Contador",
        "_2_estructuradedatos",
        "_2_estructuradedatos\\_1_Pilas",
        "_2_estructuradedatos\\_2_Colas",
        "_2_estructuradedatos\\_3_Colas_Circulares",
        "_2_estructuradedatos\\_4_Listas_Enlazadas",
        "_2_estructuradedatos\\_5_Listas_Doblemente_Enlazadas",
        "_2_estructuradedatos\\_6_Arboles",
        "_2_estructuradedatos\\_7_Grafos",
        "_3_poo",
        "_3_poo\\_10_Metodo__repr__",
        "_3_poo\\_11_Sobrecarga",
        "_3_poo\\_12_Interfaces",
        "_3_poo\\_12_Sobreesritura",
        "_3_poo\\_13_Polimorfismo",
        "_3_poo\\_1_Clases",
        "_3_poo\\_2_Atributos",
        "_3_poo\\_3_Constructor",
        "_3_poo\\_4_Metodos",
        "_3_poo\\_5_Funciones",
        "_3_poo\\_6_Propiedades",
        "_3_poo\\_7_Herencia",
        "_3_poo\\_8_Metodo__str__",
        "_3_poo\\_9_MarcadorPass",
        "_4_basesdedatos",
        "_4_basesdedatos\\_1_ConectarMySql",
        "_4_basesdedatos\\_2_ConectarPostgreSQL",
        "_4_basesdedatos\\_3_ConectarSQLLite",
        "_4_basesdedatos\\_4_ConectarOracle",
        "_4_basesdedatos\\_5_ConectarSQLServer",
        "_5_programacionfuncional",
        "_6_interfazgrafica",
        "_7_hilos",
        "_8_net",
        "_9_practicasdedisennio",
        "_9_practicasdedisennio\\_1_compositionoverInheritance",
        "_9_practicasdedisennio\\_2_dontrepeatyourself",
        "_9_practicasdedisennio\\_3_encapsulatewhatvaries",
        "_9_practicasdedisennio\\_4_failfast",
        "_9_practicasdedisennio\\_5_fluentinterface",
        "_9_practicasdedisennio\\_6_inmutability",
        "_9_practicasdedisennio\\_7_methodchaining",
        "_9_practicasdedisennio\\_8_selfencapsulatedfields",
        "_9_practicasdedisennio\\_9_yagni",

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
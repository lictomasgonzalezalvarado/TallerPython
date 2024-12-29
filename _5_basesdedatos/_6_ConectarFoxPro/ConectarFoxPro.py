import pyodbc

def conectar_a_dbf(ruta_dbf):
    try:
        # Configuración de la conexión
        conexion = pyodbc.connect(
            f"Driver={{Microsoft Visual FoxPro Driver}};"
            f"SourceType=DBF;"
            f"SourceDB={ruta_dbf};"
            f"Exclusive=No;"
        )
        print("Conexión exitosa.")
        return conexion
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos DBF:", e)
        return None

def ejecutar_consulta(conexion, consulta):
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
    except pyodbc.Error as e:
        print("Error al ejecutar la consulta:", e)
    finally:
        cursor.close()


if __name__ == '__main__':
    # Ruta del archivo DBF o directorio que contiene los DBF
    ruta_dbf = "D:\\Control de Proyectos\\Matricula SIE\\sie\\BD\\"

    for driver in pyodbc.drivers():
        print(driver)

    # Conexión a la base de datos
    #conexion = conectar_a_dbf(ruta_dbf)

    # Ejemplo de consulta (cambiar "tabla" por el nombre de la tabla real)
    # if conexion:
    #     consulta = "SELECT * FROM dplane"
    #     ejecutar_consulta(conexion, consulta)
    #     conexion.close()

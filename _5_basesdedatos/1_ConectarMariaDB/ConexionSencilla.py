if __name__ == '__main__':
    def conectar_y_consultar():
        try:
            # Establecer conexión a la base de datos
            conexion = mariadb.connect(
                # host="192.168.0.6",
                host="localhost",
                database="agenda",
                user="dbpocoyo",
                password="passwordagenda",
                port=3306  # Puerto predeterminado de MariaDB
            )
            print(type(conexion))
            print("Conexión a la base de datos del servidor Ounus")

            # Crear un cursor y ejecutar la consulta
            cursor = conexion.cursor()
            consulta = "SELECT id, nombre, ap, edad FROM datos"
            cursor.execute(consulta)

            # Recuperar y mostrar resultados
            resultados = cursor.fetchall()
            print("Resultado ", type(resultados))
            print("Datos en la tabla:")
            for fila in resultados:
                # print(fila)
                print(f"ID: {fila[0]}, Nombre: {fila[1]}, Apellido: {fila[2]}, Edad: {fila[3]}")

        except mariadb.Error as e:
            print(f"Error al conectar con la base de datos: {e}")

        finally:
            # Cerrar la conexión y el cursor si están abiertos
            if 'cursor' in locals() and cursor:
                cursor.close()
                print("Conexión cerrada.")
            if 'conexion' in locals() and conexion:
                conexion.close()
                print("Conexión cerrada.")
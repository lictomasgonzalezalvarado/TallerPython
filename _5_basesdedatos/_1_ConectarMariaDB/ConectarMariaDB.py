import mariadb
import platform

class ConexionMysql:
    def __init__(self, host, port, database, user, password):
        self.error: str = ""
        self.BanConexion: bool = False

        try:
            self.conexion = mariadb.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
            self.BanConexion = True
            self.cursor = self.conexion.cursor()
        except mariadb.Error as e:
            self.error = str(e)

    def Consultar(self,sql):
        if not self.conexion:
            print("No hay conexión activa a la base de datos.")
            return

        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except mariadb.Error as e:
            self.error = str(e)
            return None

    def __Operacion(self,sql, valores):
        ban: bool = False
        try:
            self.cursor.execute(sql, valores)  # Ejecuta la consulta con los valores proporcionados
            self.conexion.commit()  # Confirma los cambios en la base de datos
            ban = True
        except Exception as e:
            self.conexion.rollback()  # Revierte los cambios en caso de error
            self.error = str(e)
        return ban

    def Insertar(self, tabla, valores)->bool:
        sql = f"INSERT INTO {tabla} (nombre, ap, edad) VALUES (%s, %s, %s)"
        return self.__Operacion(sql, valores)

    def Eliminar(self, tabla, filtro)->bool:
        sql = f"delete from {tabla} where id = %s"
        return self.__Operacion(sql, filtro)

                                #**campos argumentos clave-valor
    def Actualizar(self, tabla, id:int, **campos)->bool:

        if campos:
            #Extrayendo del argumento clave-valor usando un generador comprehension
            columnas = ", ".join([f"{col}=%s" for col in campos.keys()])
            valores = list(campos.values()) + [id]
            sql = f"UPDATE {tabla} SET {columnas} WHERE id = %s"

            return self.__Operacion(sql, valores)
        else:
            self.error="No hay campos para actualizar"
            return False

    def __del__(self):
        # Cerrar la conexión y el cursor si están abiertos
        if 'cursor' in locals() and self.cursor:
            self.cursor.close()
        if 'conexion' in locals() and self.conexion:
            self.conexion.close()
        # print("Cerrando la conexión")

if __name__ == '__main__':
    conexion=ConexionMysql("127.0.0.1",33061,"agenda","dbpocoyo","passwordagenda")

    print("*****************************")
    print("Arquitectura de mi aplicación")
    print("*****************************")
    print(f"Arquitectura: {platform.architecture()}")

    if conexion.BanConexion:
        # if conexion.Insertar("datos",("Cesar", "Contreras Polanco", 41)):
        #     print("Registro insertado exitosamente.")
        # else:
        #     print(f"Error al insertar datos. {conexion.error}")

        # if conexion.Eliminar("datos",(4,)):
        #     print("Registro eliminado exitosamente.")
        # else:
        #     print(f"Error al eliminar el registro. {conexion.error}")

        # if conexion.Actualizar("datos",2,ap="Flores Torres"):
        #     print("Registro actualizado exitosamente.")
        # else:
        #     print(f"Error al actualizar el registro. {conexion.error}")

        res = conexion.Consultar('select * from datos')
        if res != None:
            for fila in res:
                print(f"ID: {fila[0]}, Nombre: {fila[1]}, Apellido: {fila[2]}, Edad: {fila[3]}")
        else:
            print(f"Error en la consulta. {conexion.error}")
    else:
        print(f"Error al conectar con la base de datos. {conexion.error}")
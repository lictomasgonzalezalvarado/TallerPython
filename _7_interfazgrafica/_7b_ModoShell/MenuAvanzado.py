from prompt_toolkit import PromptSession
from prompt_toolkit.shortcuts import radiolist_dialog, message_dialog

def main():
    # Opciones del menú
    opciones = [
        ("1", "1.- Mostrar lista DSN"),
        ("2", "2.- Mostrar drivers ODBC"),
        ("3", "3.- Consultar"),
        ("4", "4.- Insertar"),
        ("5", "5.- Eliminar"),
        ("6", "6.- Actualizar"),
        ("7", "7.- Salir"),
    ]

    while True:
        # Mostrar menú interactivo
        seleccion = radiolist_dialog(
            title="Menú Interactivo",
            text="Selecciona una opción:",
            values=opciones,
        ).run()

        # Limpiar la pantalla de la terminal para evitar parpadeos
        print("\033c", end="")

        if seleccion == "1":
            message_dialog(title="1.- Mostrar lista DSN", text="Mostrando lista DSN...\nPresiona Enter para continuar.").run()
        elif seleccion == "2":
            message_dialog(title="2.- Mostrar drivers ODBC", text="Mostrando drivers ODBC...\nPresiona Enter para continuar.").run()
        elif seleccion == "3":
            message_dialog(title="3.- Consultar", text="Consultando...\nPresiona Enter para continuar.").run()
        elif seleccion == "4":
            message_dialog(title="4.- Insertar", text="Insertando...\nPresiona Enter para continuar.").run()
        elif seleccion == "5":
            message_dialog(title="5.- Eliminar", text="Eliminando...\nPresiona Enter para continuar.").run()
        elif seleccion == "6":
            message_dialog(title="6.- Actualizar", text="Actualizando...\nPresiona Enter para continuar.").run()
        elif seleccion == "7":
            message_dialog(title="7.- Salir", text="Saliendo del sistema... 👋\nPresiona Enter para continuar.").run()
            break
        else:
            message_dialog(title="Error", text="Opción no válida. Inténtalo de nuevo.").run()

if __name__ == "__main__":
    main()
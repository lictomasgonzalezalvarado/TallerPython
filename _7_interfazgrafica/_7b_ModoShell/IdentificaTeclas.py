import curses

def key_identifier(stdscr):
    # Configurar la pantalla
    curses.curs_set(0)  # Ocultar el cursor
    stdscr.clear()
    stdscr.refresh()

    # Mostrar instrucciones
    stdscr.addstr(0, 0, "Presiona teclas para identificar. Presiona 'q' para salir.")
    stdscr.addstr(2, 0, "Tecla presionada: ")

    while True:
        # Leer la tecla presionada
        key = stdscr.getch()

        # Identificar la tecla
        if key == curses.KEY_F1:
            key_name = "F1"
        elif key == curses.KEY_F2:
            key_name = "F2"
        elif key == curses.KEY_F3:
            key_name = "F3"
        elif key == curses.KEY_F4:
            key_name = "F4"
        elif key == curses.KEY_F5:
            key_name = "F5"
        elif key == curses.KEY_F6:
            key_name = "F6"
        elif key == curses.KEY_F7:
            key_name = "F7"
        elif key == curses.KEY_F8:
            key_name = "F8"
        elif key == curses.KEY_F9:
            key_name = "F9"
        elif key == curses.KEY_F10:
            key_name = "F10"
        elif key == curses.KEY_F11:
            key_name = "F11"
        elif key == curses.KEY_F12:
            key_name = "F12"
        elif key == curses.KEY_HOME:
            key_name = "Inicio (Home)"
        elif key == curses.KEY_END:
            key_name = "Fin (End)"
        elif key == curses.KEY_DC:
            key_name = "Suprimir (Delete)"
        elif key == curses.KEY_IC:
            key_name = "Insertar (Insert)"
        elif key == curses.KEY_PPAGE:
            key_name = "Av Pág (Page Up)"
        elif key == curses.KEY_NPAGE:
            key_name = "Re Pág (Page Down)"
        elif key == curses.KEY_UP:
            key_name = "Flecha Arriba"
        elif key == curses.KEY_DOWN:
            key_name = "Flecha Abajo"
        elif key == curses.KEY_LEFT:
            key_name = "Flecha Izquierda"
        elif key == curses.KEY_RIGHT:
            key_name = "Flecha Derecha"
        elif key == 27:
            key_name = "Escape"
        elif key == ord('q'):
            break  # Salir del programa al presionar 'q'
        else:
            try:
                key_name = chr(key)
            except ValueError:
                key_name = f"Tecla no reconocida ({key})"

        # Mostrar la tecla presionada
        stdscr.addstr(2, 18, " " * 50)  # Limpiar línea anterior
        stdscr.addstr(2, 18, key_name)
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(key_identifier)

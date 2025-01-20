import curses

def main(stdscr):
    curses.curs_set(1)  # Hacer visible el cursor
    stdscr.addstr(0, 0, "El cursor ahora es visible.")
    stdscr.refresh()
    stdscr.getch()  # Esperar a que el usuario presione una tecla

    curses.wrapper(main)
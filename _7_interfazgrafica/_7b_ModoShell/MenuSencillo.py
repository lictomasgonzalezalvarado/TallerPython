import curses


def configurar_colores():
    """Configura los colores para usar en el programa."""
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)     # Títulos
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Texto general
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Opciones activas
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Resultados
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Barras decorativas


def mostrar_tabla(stdscr, datos):
    """Muestra una tabla con scroll y colores."""
    curses.curs_set(0)
    stdscr.clear()
    altura, ancho = stdscr.getmaxyx()
    tabla_ancho = 60
    tabla_altura = 15
    tabla_x = (ancho - tabla_ancho) // 2
    tabla_y = (altura - tabla_altura) // 2

    ventana_tabla = curses.newwin(tabla_altura, tabla_ancho, tabla_y, tabla_x)
    ventana_tabla.keypad(1)
    ventana_tabla.border()

    filas = len(datos)
    fila_actual = 0
    offset = 0  # Índice inicial de las filas visibles

    while True:
        ventana_tabla.clear()
        ventana_tabla.border()
        ventana_tabla.addstr(0, 2, " Tabla de Datos ", curses.color_pair(1) | curses.A_BOLD)

        for i in range(tabla_altura - 2):  # Espacio disponible para mostrar filas
            fila_idx = i + offset
            if fila_idx >= filas:
                break

            y = i + 1
            if fila_idx == fila_actual:
                ventana_tabla.addstr(y, 1, f"> {' | '.join(datos[fila_idx])}", curses.color_pair(3) | curses.A_REVERSE)
            else:
                ventana_tabla.addstr(y, 1, f"  {' | '.join(datos[fila_idx])}", curses.color_pair(2))

        # Dibujar barra de desplazamiento
        barra_altura = tabla_altura - 2
        proporcion = max(1, int((barra_altura / filas) * barra_altura))
        barra_inicio = int((fila_actual / filas) * barra_altura)

        for i in range(barra_altura):
            if barra_inicio <= i < barra_inicio + proporcion:
                ventana_tabla.addch(i + 1, tabla_ancho - 2, '|', curses.color_pair(3))
            else:
                ventana_tabla.addch(i + 1, tabla_ancho - 2, '|', curses.color_pair(5))

        ventana_tabla.refresh()

        # Leer entrada del usuario
        tecla = ventana_tabla.getch()
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
            if fila_actual < offset:
                offset -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < filas - 1:
            fila_actual += 1
            if fila_actual >= offset + (tabla_altura - 2):
                offset += 1
        elif tecla in (curses.KEY_ENTER, 10):
            return f"Seleccionaste la fila {fila_actual + 1}"
        elif tecla == 27:  # Presionar ESC para salir
            return "Saliendo de la tabla..."


def mostrar_formulario(stdscr, datos):
    """Muestra un formulario para insertar datos."""
    curses.curs_set(1)
    altura, ancho = stdscr.getmaxyx()
    formulario_ancho = 40
    formulario_altura = 10
    formulario_x = (ancho - formulario_ancho) // 2
    formulario_y = (altura - formulario_altura) // 2

    ventana_formulario = curses.newwin(formulario_altura, formulario_ancho, formulario_y, formulario_x)
    ventana_formulario.keypad(1)
    ventana_formulario.border()
    ventana_formulario.addstr(0, 2, " Formulario ", curses.color_pair(1) | curses.A_BOLD)

    campos = ["Campo 1:", "Campo 2:", "Campo 3:", "Campo 4:"]
    valores = []

    for idx, campo in enumerate(campos):
        ventana_formulario.addstr(2 + idx, 2, campo, curses.color_pair(2))
        curses.echo()
        ventana_formulario.refresh()
        entrada = ventana_formulario.getstr(2 + idx, len(campo) + 3, 30).decode("utf-8")
        valores.append(entrada)

    datos.append(valores)
    curses.noecho()
    ventana_formulario.addstr(len(campos) + 3, 2, "Datos guardados.", curses.color_pair(4))
    ventana_formulario.refresh()
    ventana_formulario.getch()


def menu_principal(stdscr):
    """Muestra el menú principal."""
    configurar_colores()
    curses.curs_set(0)
    stdscr.clear()
    altura, ancho = stdscr.getmaxyx()
    ventana_ancho = 80
    ventana_altura = len(opciones) + 15
    ventana_x = (ancho - ventana_ancho) // 2
    ventana_y = (altura - ventana_altura) // 2

    ventana = curses.newwin(ventana_altura, ventana_ancho, ventana_y, ventana_x)
    ventana.keypad(1)
    opcion_actual = 0

    while True:
        ventana.clear()
        ventana.border()
        ventana.addstr(0, 2, " Menú Principal ", curses.color_pair(1) | curses.A_BOLD)
        ventana.addstr(ventana_altura - 2, 2, " Usa ↑ ↓ y Enter para seleccionar ", curses.color_pair(5) | curses.A_DIM)

        for idx, opcion in enumerate(opciones):
            x = 2
            y = 2 + idx
            if idx == opcion_actual:
                ventana.addstr(y, x, f"> {opcion}", curses.color_pair(3) | curses.A_REVERSE)
            else:
                ventana.addstr(y, x, f"  {opcion}", curses.color_pair(2))

        ventana.refresh()

        tecla = ventana.getch()
        if tecla == curses.KEY_UP and opcion_actual > 0:
            opcion_actual -= 1
        elif tecla == curses.KEY_DOWN and opcion_actual < len(opciones) - 1:
            opcion_actual += 1
        elif tecla in (curses.KEY_ENTER, 10):
            resultado = ""

            match opcion_actual:
                case 0:
                    ventana.clear()
                    ventana.border()
                    ventana.addstr(0, 2, " Resultado ", curses.color_pair(1) | curses.A_BOLD)
                    ventana.addstr(2, 2, "Mostrar lista DSN", curses.color_pair(4))
                    ventana.addstr(ventana_altura - 2, 2, " Presiona cualquier tecla para continuar ", curses.color_pair(5) | curses.A_DIM)
                    ventana.refresh()
                    ventana.getch()
                case 1: resultado = "Mostrar drivers ODBC"
                case 2: resultado = mostrar_tabla(stdscr, datos)
                case 3:
                    mostrar_formulario(stdscr, datos)
                    resultado = "Datos insertados correctamente."
                case 4: resultado = "Eliminar"
                case 5: resultado = "Actualizar"
                case 6:
                    resultado = "Saliendo del sistema..."
                    ventana.addstr(ventana_altura - 3, 2, resultado, curses.color_pair(1) | curses.A_BOLD)
                    ventana.refresh()
                    curses.napms(1500)
                    break


datos = [['F01C1', 'F01C2', 'F01C3', 'F01C4'],
         ['F02C1', 'F02C2', 'F02C3', 'F02C4'],
         ['F03C1', 'F03C2', 'F03C3', 'F03C4'],
         ['F04C1', 'F04C2', 'F04C3', 'F04C4'],
         ['F05C1', 'F05C2', 'F05C3', 'F05C4'],
         ['F06C1', 'F06C2', 'F06C3', 'F06C4'],
         ['F07C1', 'F07C2', 'F07C3', 'F07C4'],
         ['F08C1', 'F08C2', 'F08C3', 'F08C4'],
         ['F09C1', 'F09C2', 'F09C3', 'F09C4'],
         ['F10C1', 'F10C2', 'F10C3', 'F10C4'],
         ['F11C1', 'F11C2', 'F11C3', 'F11C4'],
         ['F12C1', 'F12C2', 'F12C3', 'F12C4'],
         ['F13C1', 'F13C2', 'F13C3', 'F13C4'],
         ['F14C1', 'F14C2', 'F14C3', 'F14C4'],
         ['F15C1', 'F15C2', 'F15C3', 'F15C4'],
         ['F16C1', 'F16C2', 'F16C3', 'F16C4'],
         ['F17C1', 'F17C2', 'F17C3', 'F17C4'],
         ['F18C1', 'F18C2', 'F18C3', 'F18C4'],
         ['F19C1', 'F19C2', 'F19C3', 'F19C4'],
         ['F20C1', 'F20C2', 'F20C3', 'F20C4']
         ]

opciones = ["1.- Mostrar lista DSN", "2.- Mostrar drivers ODBC", "3.- Consultar", "4.- Insertar", "5.- Eliminar", "6.- Actualizar", "7.- Salir"]

curses.wrapper(menu_principal)

import curses

def mostrar_tabla(stdscr, datos):
    curses.curs_set(0)
    altura, ancho = stdscr.getmaxyx()
    tabla_ancho = 60
    tabla_altura = 15
    tabla_x = (ancho - tabla_ancho) // 2
    tabla_y = (altura - tabla_altura) // 2

    ventana_tabla = curses.newwin(tabla_altura, tabla_ancho, tabla_y, tabla_x)
    ventana_tabla.keypad(1)
    ventana_tabla.border()

    fila_actual = 0
    offset = 0
    filas = len(datos)

    while True:
        ventana_tabla.clear()
        ventana_tabla.border()
        ventana_tabla.addstr(0, 2, " Tabla de Datos ", curses.A_BOLD)

        for i in range(tabla_altura - 2):
            fila_idx = i + offset
            if fila_idx >= filas:
                break
            y = i + 1
            if fila_idx == fila_actual:
                ventana_tabla.addstr(y, 2, f"> {' | '.join(datos[fila_idx])} ", curses.A_REVERSE)
            else:
                ventana_tabla.addstr(y, 2, f"  {' | '.join(datos[fila_idx])}")

        ventana_tabla.refresh()

        tecla = ventana_tabla.getch()
        if tecla == curses.KEY_UP and fila_actual > 0:
            fila_actual -= 1
            if fila_actual < offset:
                offset -= 1
        elif tecla == curses.KEY_DOWN and fila_actual < filas - 1:
            fila_actual += 1
            if fila_actual >= offset + (tabla_altura - 2):
                offset += 1
        elif tecla == 10:
            return f"Seleccionaste la fila {fila_actual + 1}"
        elif tecla == 27:
            return "Saliendo de la tabla..."

def mostrar_formulario(stdscr, datos):
    curses.curs_set(1)
    altura, ancho = stdscr.getmaxyx()
    formulario_ancho = 50
    formulario_altura = 10
    formulario_x = (ancho - formulario_ancho) // 2
    formulario_y = (altura - formulario_altura) // 2

    ventana_formulario = curses.newwin(formulario_altura, formulario_ancho, formulario_y, formulario_x)
    ventana_formulario.keypad(1)
    ventana_formulario.border()

    campos = ["Nombre:", "Edad:", "Correo:", "Teléfono:"]
    valores = []

    for idx, campo in enumerate(campos):
        ventana_formulario.addstr(2 + idx, 2, campo)
        curses.echo()
        ventana_formulario.refresh()
        entrada = ventana_formulario.getstr(2 + idx, len(campo) + 3, 30).decode("utf-8")
        valores.append(entrada)

    datos.append(valores)

    ventana_formulario.addstr(len(campos) + 3, 2, "Datos guardados. Presiona cualquier tecla.")
    ventana_formulario.refresh()
    curses.curs_set(0)
    ventana_formulario.getch()

def mostrar_ayuda(stdscr):
    altura, ancho = stdscr.getmaxyx()
    ayuda_ancho = 50
    ayuda_altura = 10
    ayuda_x = (ancho - ayuda_ancho) // 2
    ayuda_y = (altura - ayuda_altura) // 2

    ventana_ayuda = curses.newwin(ayuda_altura, ayuda_ancho, ayuda_y, ayuda_x)
    ventana_ayuda.keypad(1)
    ventana_ayuda.border()

    ayuda_texto = [
        "Flechas: Navegar",
        "Enter: Seleccionar",
        "ESC: Volver",
        "Usa las opciones para gestionar datos"
    ]

    ventana_ayuda.addstr(0, 2, " Ayuda ", curses.A_BOLD)
    for idx, linea in enumerate(ayuda_texto):
        ventana_ayuda.addstr(2 + idx, 2, linea)

    ventana_ayuda.addstr(len(ayuda_texto) + 3, 2, "Presiona cualquier tecla para salir.", curses.A_DIM)
    ventana_ayuda.refresh()
    ventana_ayuda.getch()

def menu_principal(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.curs_set(0)
    stdscr.clear()

    datos = [["F01", "Nombre1", "23", "correo1@test.com"],
             ["F02", "Nombre2", "34", "correo2@test.com"],
             ["F03", "Nombre3", "45", "correo3@test.com"]]

    opciones = ["Ver Tabla de Datos", "Insertar Datos", "Ayuda", "Salir"]
    opcion_actual = 0

    while True:
        stdscr.clear()
        altura, ancho = stdscr.getmaxyx()
        stdscr.addstr(1, 2, " Sistema de Gestión ", curses.color_pair(1) | curses.A_BOLD)

        for idx, opcion in enumerate(opciones):
            x = 4
            y = 4 + idx
            if idx == opcion_actual:
                stdscr.addstr(y, x, f"> {opcion}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {opcion}")

        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla == curses.KEY_UP and opcion_actual > 0:
            opcion_actual -= 1
        elif tecla == curses.KEY_DOWN and opcion_actual < len(opciones) - 1:
            opcion_actual += 1
        elif tecla == 10:
            if opcion_actual == 0:
                resultado = mostrar_tabla(stdscr, datos)
            elif opcion_actual == 1:
                mostrar_formulario(stdscr, datos)
                resultado = "Datos insertados correctamente."
            elif opcion_actual == 2:
                mostrar_ayuda(stdscr)
                resultado = "Volviendo al menú principal."
            elif opcion_actual == 3:
                stdscr.addstr(altura - 2, 2, "Saliendo...", curses.color_pair(3) | curses.A_BOLD)
                stdscr.refresh()
                curses.napms(1000)
                break

            stdscr.addstr(altura - 2, 2, resultado, curses.color_pair(2) | curses.A_BOLD)
            stdscr.refresh()
            curses.napms(1000)

curses.wrapper(menu_principal)

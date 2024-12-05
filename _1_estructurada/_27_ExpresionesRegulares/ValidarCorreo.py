import re

def ValidarCorreo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, correo):
        print(f"El correo '{correo}' es válido.")
    else:
        print(f"El correo '{correo}' no es válido.")

if __name__ == '__main__':
    ValidarCorreo("ejemplo@dominio.com")
    ValidarCorreo("usuario@dominio@com")
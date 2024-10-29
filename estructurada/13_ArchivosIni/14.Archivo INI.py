import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Verifica que las secciones y claves existan
    if 'Maximus' in config and 'basedatos' in config['Maximus'] and 'usuario' in config['Maximus'] and 'contrasennia' in config['Maximus']:
        bd = config['Maximus']['basedatos']
        user = config['Maximus']['usuario']
        password = config['Maximus']['contrasennia']

        sys.stdout.write("Servidor Maximus\n")
        sys.stdout.write(f"Base de Datos: {bd}\n")
        sys.stdout.write(f"Usuario: {user}\n")
        sys.stdout.write(f"Contraseña: {password}\n")
    else:
        sys.stdout.write("La sección o la clave no existen.\n")

    sys.stdout.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    if 'Ounus' in config and 'basedatos' in config['Ounus'] and 'usuario' in config['Ounus'] and 'contrasennia' in config['Ounus']:
        bd = config['Ounus']['basedatos']
        user = config['Ounus']['usuario']
        password = config['Ounus']['contrasennia']

        sys.stdout.write("Servidor Ounus\n")
        sys.stdout.write(f"Base de Datos: {bd}\n")
        sys.stdout.write(f"Usuario: {user}\n")
        sys.stdout.write(f"Contraseña: {password}\n")
    else:
        sys.stdout.write("La sección o la clave no existen.\n")
import socket

# Configuración del cliente
HOST = '127.0.0.1'  # IP del servidor
PORT = 65432        # Puerto del servidor
FILENAME = 'archivo_a_enviar.txt'  # Nombre del archivo a enviar

def iniciar_cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        print(f"Conectado al servidor en {HOST}:{PORT}")

        # Enviar nombre del archivo
        cliente.sendall(FILENAME.encode())

        # Enviar contenido del archivo
        with open(FILENAME, 'rb') as f:
            while (datos := f.read(1024)):
                cliente.sendall(datos)
        print(f"Archivo {FILENAME} enviado con éxito.")

if __name__ == "__main__":
    iniciar_cliente()
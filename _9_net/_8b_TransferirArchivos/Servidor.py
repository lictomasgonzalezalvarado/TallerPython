import socket

# Configuración del servidor
HOST = '0.0.0.0'  # Escucha en todas las interfaces
PORT = 65432      # Puerto del servidor

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}")

        conn, addr = servidor.accept()
        print(f"Conexión establecida con {addr}")

        # Recibir nombre del archivo
        filename = conn.recv(1024).decode()
        print(f"Recibiendo archivo: {filename}")

        # Recibir contenido del archivo
        with open(filename, 'wb') as f:
            while True:
                datos = conn.recv(1024)
                if not datos:
                    break
                f.write(datos)
        print(f"Archivo {filename} recibido con éxito.")

if __name__ == "__main__":
    iniciar_servidor()
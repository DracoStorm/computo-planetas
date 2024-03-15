import socket
import os

def send_file(file_path, server_address):
    # Obtener el nombre y tamaño del archivo
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Crear un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        client_socket.connect(server_address)

        # Enviar el nombre del archivo y su tamaño al servidor
        file_info = f"{file_name}@{file_size}@"
        client_socket.sendall(file_info.encode('utf-8'))

        # Abrir y enviar el contenido del archivo
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

        print(f"Archivo '{file_name}' enviado con éxito al servidor.")

    except Exception as e:
        print(f"Error durante la transferencia del archivo: {e}")

    finally:
        # Cerrar la conexión
        client_socket.close()

# Dirección IP y puerto del servidor
server_address = ('172.26.166.136', 12345)  # Cambiar a la dirección IP real del servidor

# Ruta del archivo que deseas enviar
file_path = 'network/Pruebas.txt'  # Cambiar a la ruta real del archivo

# Llamar a la función para enviar el archivo
send_file(file_path, server_address)
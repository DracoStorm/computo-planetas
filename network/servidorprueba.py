import socket
import threading
import constants as const
import os

# Diccionario de direcciones IP permitidas
allowed_ips = {
    '172.26.167.179',  # Ejemplo: localhost
    # Agrega más direcciones IP permitidas según sea necesario
    '172.31.6.164',
    '172.31.12.11',
    '192.168.56.1'
}

# Lock para coordinar el acceso a la sección crítica
file_lock = threading.Lock()


def file_transfer(client_socket, initial_data):
    try:
        file_info = initial_data[len(const.FILE_IDENTIFIER):].decode('utf-8', errors='replace').split('@')
        print("File information received:", file_info)

        file_name = file_info[0]
        file_size = int(file_info[1])

        print(f"Receiving file: {file_name}, size: {file_size} bytes")

        with open(file_name, 'wb') as file:
            received_data = 0
            while received_data < file_size:
                file_data = client_socket.recv(1024)
                file.write(file_data)
                received_data += len(file_data)

        print("File received successfully.")
    except Exception as e:
        print(f"Error during file transfer: {e}")


def recive_message(client_socket, initial_data):
    try:
        message = initial_data[len(const.MSG_IDENTIFIER):].decode(
            'utf-8', errors='replace')
        print("Message received:", message)
    except Exception as e:
        print(f"Error during message transfer: {e}")


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                
                break  # No more data, close the connection

            if data.startswith(const.FILE_IDENTIFIER):
                print("Message")
                file_transfer(client_socket, data)

            elif data.startswith(const.MSG_IDENTIFIER):
                recive_message(client_socket, data)
            else:
                print("Unknown data type.")

    except Exception as e:
        print(f"Error during data transfer: {e}")

    finally:
        # Close the client connection
        client_socket.close()


# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Cambiar a la dirección IP real del servidor
server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)
server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes

print('Esperando conexiones...')

try:
    while True:
        # Aceptar una conexión
        client_socket, client_address = server_socket.accept()
        print('Conexión aceptada de', client_address)

        # Verificar la dirección IP del cliente
        if client_address[0] not in allowed_ips:
            print(f"Intento de conexión desde una dirección IP no permitida: {
                  client_address[0]}")
            break

        # Crear un hilo para manejar la conexión del cliente
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_handler.start()

except KeyboardInterrupt:
    print("Servidor cerrado manualmente.")

finally:
    # Cerrar el socket del servidor
    server_socket.close()

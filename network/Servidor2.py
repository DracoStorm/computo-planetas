import socket
import threading
import os

def handle_client(client_socket):
    try:
        # Recibir el nombre del archivo y su tamaño
        file_info = client_socket.recv(1024).decode('utf-8', errors='replace').split('@')
        print("Información del archivo recibida:", file_info)


       # print(file_info[1]) #tamano en bytes

        file_name = file_info[0]
        file_size = int(file_info[1])   # esta linea tiene problemas

        print(f"Recibiendo archivo: {file_name}, tamaño: {file_size} bytes")

        # Abrir un archivo para escribir los datos recibidos
        with open(file_name, 'wb') as file:
            # Recibir y escribir los datos en el archivo
            received_data = 0
            while received_data < file_size:
                data = client_socket.recv(1024)
                file.write(data)
                received_data += len(data)

        print("Archivo recibido con éxito.")

    except Exception as e:
        print(f"Error durante la transferencia del archivo: {e}")

    finally:
        # Cerrar la conexión del cliente
        client_socket.close()

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 12345)  # Cambiar a la dirección IP real del servidor
server_socket.bind(server_address)
server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes

print('Esperando conexiones...')

try:
    while True:
        # Aceptar una conexión
        client_socket, client_address = server_socket.accept()
        print('Conexión aceptada de', client_address)

        # Crear un hilo para manejar la conexión del cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

except KeyboardInterrupt:
    print("Servidor cerrado manualmente.")

finally:
    # Cerrar el socket del servidor
    server_socket.close()
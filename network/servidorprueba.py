import socket
import threading
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

def handle_client(client_socket, client_address):
    try:
        # Adquirir el bloqueo antes de enviar archivos
        file_lock.acquire()

        # Recibir el nombre del archivo y su tamaño
        file_info = client_socket.recv(1024).decode('utf-8', errors='replace').split('@')
        print("Información del archivo recibida:", file_info)

        file_name = file_info[0]
        file_size = int(file_info[1])

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
        # Liberar el bloqueo para permitir que otro cliente envíe archivos
        file_lock.release()
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
        
        # Verificar la dirección IP del cliente
        if client_address[0] not in allowed_ips:
            print(f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
            break
        
        # Crear un hilo para manejar la conexión del cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

except KeyboardInterrupt:
    print("Servidor cerrado manualmente.")

finally:
    # Cerrar el socket del servidor
    server_socket.close()

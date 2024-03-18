import socket
import threading
import exchange as net
import constants as const

if __name__ == '__main__':
    # Crear un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Cambiar a la dirección IP real del servidor
    server_address = ('192.168.100.21', 22333)
    server_socket.bind(server_address)
    server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes

    print('Esperando conexiones...')

    try:
        while True:
            # Aceptar una conexión
            client_socket, client_address = server_socket.accept()
            print('Conexión aceptada de', client_address)

            # Verificar la dirección IP del cliente
            if client_address[0] not in const.IPS:
                print(
                    f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
                break

            # Crear un hilo para manejar la conexión del cliente
            client_handler = threading.Thread(
                target=net.handle_client, args=(client_socket,))
            client_handler.start()

    except KeyboardInterrupt:
        print("Servidor cerrado manualmente.")

    finally:
        # Cerrar el socket del servidor
        server_socket.close()
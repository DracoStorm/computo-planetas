import socket
import constants as const
import os


def send_file(file_path, server_address):
    # Obtener el nombre y tamaño del archivo
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    try:

        # Send file information
        file_info = f"{file_name}@{file_size}@"
        client_socket.sendall(const.FILE_IDENTIFIER +
                              file_info.encode('utf-8'))

        # Send the file data
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

    except Exception as e:
        print(f"Error during file transfer: {e}")


def send_message(server_address):

    try:

        # Solicitar al usuario que ingrese el mensaje
        message = input("Ingrese el mensaje que desea enviar al servidor: ")

        # Enviar el mensaje al servidor
        client_socket.sendall(const.MSG_IDENTIFIER + message.encode('utf-8'))

        print("Mensaje enviado con éxito al servidor.")

    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")


if __name__ == "__main__":
    # Dirección IP y puerto del servidor
    # Cambiar a la dirección IP real del servidor
    server_address = ('192.168.56.1', 12345)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Conectar al servidor
    client_socket.connect(server_address)
    while True:
        # Opción para enviar mensaje o archivo
        option = input(
            "Seleccione una opción (1 para enviar mensaje, 2 para enviar archivo, q para salir): ")

        if option == '1':
            send_message(server_address)
        elif option == '2':
            # Ruta del archivo que deseas enviar
            file_path = input("Ingrese la ruta del archivo que desea enviar: ")
            send_file(file_path, server_address)
        elif option.lower() == 'q':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

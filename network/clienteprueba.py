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
        file_info = f"{file_name}@{file_size}"
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

def send_message(server_address):
    # Crear un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor
        client_socket.connect(server_address)

        # Solicitar al usuario que ingrese el mensaje
        message = input("Ingrese el mensaje que desea enviar al servidor: ")

        # Enviar el mensaje al servidor
        client_socket.sendall(message.encode('utf-8'))

        print("Mensaje enviado con éxito al servidor.")

    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")

    finally:
        # Cerrar la conexión
        client_socket.close()

def main():
    # Dirección IP y puerto del servidor
    server_address = ('192.168.56.1', 12345)  # Cambiar a la dirección IP real del servidor

    while True:
        # Opción para enviar mensaje o archivo
        option = input("Seleccione una opción (1 para enviar mensaje, 2 para enviar archivo, q para salir): ")

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

if __name__ == "__main__":
    main()
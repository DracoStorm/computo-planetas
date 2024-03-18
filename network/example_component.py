import socket
import constants as const
import exchange as net


def main() -> None:
    # Dirección IP y puerto del servidor
    # Cambiar a la dirección IP real del servidor
    server_address = (const.SERVER_IP, const.SERVER_PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Conectar al servidor
    client_socket.connect(server_address)
    while True:
        # Opción para enviar mensaje o archivo
        option = input(
            "Seleccione una opción (1 para enviar mensaje, 2 para enviar archivo, q para salir): ")

        if option == '1':
            net.send_message(client_socket)
        elif option == '2':
            # Ruta del archivo que deseas enviar
            file_path = input("Ingrese la ruta del archivo que desea enviar: ")
            net.send_file(client_socket, file_path)
        elif option.lower() == 'q':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

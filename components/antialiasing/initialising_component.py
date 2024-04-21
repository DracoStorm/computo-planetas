import socket
from PIL import Image, ImageFilter
import os
from .. import constants as const
import network.functions as net


def antialiasing(file: str) -> Image:
    # Abrir la imagen original
    image = Image.open(file)

    # Aplicar el filtro gaussiano
    alias_image = image.filter(ImageFilter.GaussianBlur(radius=2))

    return alias_image


def main() -> None:
    # Dirección IP y puerto del servidor
    # Cambiar a la dirección IP real del servidor
    server_address = (const.SERVER_IP, const.SERVER_PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Conectar al servidor
    client_socket.connect(server_address)
    while True:
        # Opción para enviar mensaje, archivo o salir
        option = input(
            "Seleccione una opción (1 para enviar mensaje, 2 para enviar archivo, q para salir): ")

        if option == '1':
            net.send_message(client_socket)
        elif option == '2':
            # Ruta del archivo que deseas enviar
            file_path = input("Ingrese la ruta del archivo que desea enviar: ")
            if os.path.isfile(file_path):
                # Aplicar antialiasing si el archivo es una imagen
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    image_with_antialiasing = antialiasing(file_path)
                    image_with_antialiasing.save(file_path)  # Sobrescribe la imagen original con la imagen antialiasing
                net.send_file(client_socket, file_path)
            else:
                print("La ruta no corresponde a un archivo válido.")
        elif option.lower() == 'q':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if _name_ == "_main_":
    main()
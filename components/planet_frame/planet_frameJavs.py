import cv2
import os
import socket
from network.constants import *
from network import functions as net
from network.exceptions import BadNetType

def define_folder_path(folder_path):
    """
    Definir la ruta de la carpeta donde se encuentran los archivos de imagen.
    
    Args:
        folder_path (str): Ruta de la carpeta.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_file_list(folder_path):
    """
    Obtener la lista de archivos en la carpeta especificada.
    
    Args:
        folder_path (str): Ruta de la carpeta.
    
    Returns:
        list: Lista de nombres de archivos en la carpeta.
    """
    return os.listdir(folder_path)

def process_images(folder_path):
    """
    Procesar imágenes en la carpeta especificada.
    
    Args:
        folder_path (str): Ruta de la carpeta.
    """
    file_list = get_file_list(folder_path)
    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Comprobar si es una imagen
            if is_image(file_path):
                # Crear una carpeta con el nombre del archivo
                folder_name = os.path.splitext(filename)[0]
                folder_path_new = os.path.join(folder_path, folder_name)
                define_folder_path(folder_path_new)
                
                # Abrir la imagen
                image = cv2.imread(file_path)
                
                # Aplicar filtro gaussiano
                processed_image = cv2.GaussianBlur(image, (5, 5), 0)
                
                # Guardar la imagen procesada con un nuevo nombre
                new_filename = os.path.splitext(filename)[0] + "_processed.jpg"
                new_file_path = os.path.join(folder_path_new, new_filename)
                cv2.imwrite(new_file_path, processed_image)
                
                # Cierra los archivos del tipo de imagen y sale del bucle
                break
        else:
            # No es un archivo, continuar con el siguiente
            continue

def is_image(file_path):
    """
    Comprueba si el archivo en la ruta especificada es una imagen.
    
    Args:
        file_path (str): Ruta del archivo.
    
    Returns:
        bool: True si es una imagen, False en caso contrario.
    """
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in valid_extensions

def connect_to_server(server_ip, server_port):
    """
    Conectar al servidor utilizando un socket.
    
    Args:
        server_ip (str): Dirección IP del servidor.
        server_port (int): Puerto del servidor.
    
    Returns:
        socket.socket: Objeto de socket cliente.
    """
    server_address = (server_ip, server_port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    print(f'Connected to server hosted at {server_ip} using port {server_port}')
    return client_socket

def main():
    server_ip = '127.0.0.1'  # Ejemplo: Cambia esto con la IP correcta
    server_port = 12345       # Ejemplo: Cambia esto con el puerto correcto
    
    # Conectar al servidor
    client_socket = connect_to_server(server_ip, server_port)

    # Procesar imágenes en la carpeta especificada
    folder_path = "components/gen_frame/planet_frame/gifs"
    define_folder_path(folder_path)
    process_images(folder_path)
    
    # Una vez que se procesan las imágenes, enviar algún tipo de información al servidor
    message = "Información que deseas enviar al servidor"
    net.send_message(client_socket, message)

if __name__ == "__main__":
    main()

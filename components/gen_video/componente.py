import cv2
import os
import socket
from network import functions as net
from network.constants import *
from network.exceptions import *


def send_video_to_server(video_path, SERVER_IP, SERVER_PORT):
    try:
        # Conexión al servidor
        server_address = (SERVER_IP, SERVER_PORT)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        print(f'Connected to server at {SERVER_IP} using port {SERVER_PORT}')

        # Enviar el video al servidor
        with open(video_path, 'rb') as file:
            filename = os.path.basename(video_path)
            net.send_file(client_socket, filename, file)
            print(f'Sending {filename} to server...')

        # Esperar la respuesta del servidor
        try:
            net.send_ok(client_socket)
            status = net.receive_status(client_socket)
            print(f'Status: {status.decode()}')
            if status == SHUTDOWN_IDENTIFIER:
                print("Server sent shutdown signal.")
        except (ComponentError, BadNetType) as e:
            print("Error receiving status from server:", e)
    except Exception as e:
        print("An error occurred during video transmission:", e)
    finally:
        client_socket.close()


if __name__ == "__main__":
    video_path = 'components/gen_video/VideoCambiado.mp4'
    SERVER_IP = '172.26.164.153'
    SERVER_PORT = 22333
    send_video_to_server(video_path, SERVER_IP, SERVER_PORT)

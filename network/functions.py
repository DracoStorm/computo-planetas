import os
from socket import socket
from constants import *


def recive_file(client_socket: socket, initial_data: bytes) -> None:
    try:
        file_info = initial_data[len(FILE_IDENTIFIER):].decode(
            'utf-8', errors='replace').split('@')
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


def recive_file(client_socket: socket, initial_data: bytes) -> tuple[str, int, bytes]:
    try:
        file_info: str = initial_data[len(FILE_IDENTIFIER):].decode(
            'utf-8', errors='replace').split('@')

        # Initialize an empty bytearray to store the file data
        file_data: bytearray = bytearray()

        while True:
            data_chunk: bytes = client_socket.recv(1024)
            if not data_chunk:
                break  # No more data, end the loop
            file_data.extend(data_chunk)
    except Exception as e:
        print(f"Error during file transfer: {e}")
    else:
        # return the file name, file size, file in bytes
        return file_info[0], int(file_info[1]), bytes(file_data)


def recive_message(initial_data: bytes) -> str:
    try:
        message = str(initial_data[len(MSG_IDENTIFIER):].decode(
            'utf-8', errors='replace'))
    except Exception as e:
        print(f"Error during message transfer: {e}")
    else:
        return message


def send_file(client_socket, file_path):
    # Obtener el nombre y tamaño del archivo
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    try:

        # Send file information
        file_info = f"{file_name}@{file_size}@"
        client_socket.sendall(FILE_IDENTIFIER +
                              file_info.encode('utf-8'))

        # Send the file data
        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

    except Exception as e:
        print(f"Error during file transfer: {e}")


def send_message(client_socket: socket, message: str) -> None:
    try:
        # Enviar el mensaje al servidor
        client_socket.sendall(MSG_IDENTIFIER + message.encode('utf-8'))
    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")


def send_error(client_socket: socket, error: str) -> None:
    try:
        # Enviar el mensaje al servidor
        client_socket.sendall(ERR_IDENTIFIER + error.encode('utf-8'))
    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")


def send_shutdown(client_socket: socket) -> None:
    try:
        # Enviar el mensaje al servidor
        client_socket.sendall(SHUTDOWN_IDENTIFIER)
    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break  # No more data, close the connection

            if data.startswith(FILE_IDENTIFIER):
                print("Message")
                recive_file(client_socket, data)

            elif data.startswith(MSG_IDENTIFIER):
                recive_message(data)
            else:
                print("Unknown data type.")

    except Exception as e:
        print(f"Error during data transfer: {e}")

    finally:
        # Close the client connection
        client_socket.close()

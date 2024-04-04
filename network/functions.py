import os
from socket import socket
from constants import *


def receive_file(client_socket: socket, initial_data: bytes) -> None:
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
        print(f"File size: {os.path.getsize(file_name)} bytes")
    except Exception as e:
        print(f"Error during file transfer: {e}")


def receive_file_info(client_socket: socket, initial_data: bytes) -> tuple[str, int, bytes]:
    try:
        file_info = initial_data[len(FILE_IDENTIFIER):].decode(
            'utf-8', errors='replace').split('@')
        file_name = file_info[0]
        file_size = int(file_info[1])

        file_data = bytearray()
        while True:
            data_chunk = client_socket.recv(1024)
            if not data_chunk:
                break
            file_data.extend(data_chunk)
    except Exception as e:
        print(f"Error during file transfer: {e}")
    else:
        return file_name, file_size, bytes(file_data)


def receive_message(initial_data: bytes) -> str:
    try:
        message = str(initial_data[len(MSG_IDENTIFIER):].decode(
            'utf-8', errors='replace'))
        print(f"Message received. Size: {len(message.encode('utf-8'))} bytes")
    except Exception as e:
        print(f"Error during message transfer: {e}")
    else:
        return message


def send_file(client_socket: socket, file_path: str) -> None:
    try:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        file_info = f"{file_name}@{file_size}@"
        client_socket.sendall(FILE_IDENTIFIER + file_info.encode('utf-8'))

        with open(file_path, 'rb') as file:
            data = file.read(1024)
            while data:
                client_socket.sendall(data)
                data = file.read(1024)

        print(f"File sent. Size: {file_size} bytes")
    except Exception as e:
        print(f"Error during file transfer: {e}")


def send_message(client_socket: socket, message: str) -> None:
    try:
        client_socket.sendall(MSG_IDENTIFIER + message.encode('utf-8'))
        print(f"Message sent. Size: {len(message.encode('utf-8'))} bytes")
    except Exception as e:
        print(f"Error during message transfer: {e}")


def send_error(client_socket: socket, error: str) -> None:
    try:
        client_socket.sendall(ERR_IDENTIFIER + error.encode('utf-8'))
    except Exception as e:
        print(f"Error during error transfer: {e}")


def send_shutdown(client_socket: socket) -> None:
    try:
        client_socket.sendall(SHUTDOWN_IDENTIFIER)
    except Exception as e:
        print(f"Error during shutdown transfer: {e}")


def handle_client(client_socket: socket) -> None:
    try:
        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            if data.startswith(FILE_IDENTIFIER):
                print("File")
                receive_file(client_socket, data)
            elif data.startswith(MSG_IDENTIFIER):
                print("Message")
                receive_message(data)
            else:
                print("Unknown data type.")
    except Exception as e:
        print(f"Error during data transfer: {e}")
    finally:
        client_socket.close()

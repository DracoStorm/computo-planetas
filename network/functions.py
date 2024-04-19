import os
from socket import socket
from .constants import *
from .exceptions import *


def receive_file(client_socket: socket) -> tuple[str, bytes]:
    data = client_socket.recv(1024)
    print(data)
    if (data == ERR_IDENTIFIER):
        raise ComponentError
    if (data == SHUTDOWN_IDENTIFIER):
        raise UnexpectedShutdown
    if (data.startswith(MSG_IDENTIFIER)):
        raise BadNetType

    file_info = data[len(FILE_IDENTIFIER):].decode(errors='replace').split('@')
    file_name = file_info[0]
    file_size = int(file_info[1])

    file_data = bytearray()
    while True:
        if len(file_data) == file_size:
            break
        data_chunk = client_socket.recv(1024)
        file_data.extend(data_chunk)
    
    file_data = bytes(file_data)
    return file_name, file_data


def receive_message(client_socket: socket) -> str:
    msg = client_socket.recv(1024)

    if (msg == ERR_IDENTIFIER):
        raise ComponentError
    if (msg == SHUTDOWN_IDENTIFIER):
        raise UnexpectedShutdown
    if (msg.startswith(FILE_IDENTIFIER)):
        raise BadNetType

    msg = str(msg[len(MSG_IDENTIFIER):].decode(errors='replace'))
    return msg


def recieve_status(client_socket: socket) -> bytes:
    status = client_socket.recv(1024)

    if (status == ERR_IDENTIFIER):
        raise ComponentError
    if (status.startswith(FILE_IDENTIFIER) or status.startswith(MSG_IDENTIFIER)):
        raise BadNetType

    return status


def send_file(client_socket: socket, file_name: str, file: bytes) -> None:
    client_socket.sendall(FILE_IDENTIFIER+file_name.encode()+len(file))
    client_socket.sendall(file)


def send_message(client_socket: socket, message: str) -> None:
    client_socket.sendall(MSG_IDENTIFIER + message.encode())


def send_error(client_socket: socket) -> None:
    client_socket.sendall(ERR_IDENTIFIER)


def send_shutdown(client_socket: socket) -> None:
    client_socket.sendall(SHUTDOWN_IDENTIFIER)


def send_ok(client_socket: socket) -> None:
    client_socket.sendall(OK_IDENTIFIER)


def handle_client(client_socket: socket) -> None:
    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        if data.startswith(FILE_IDENTIFIER):
            print("File")
            receive_file(client_socket)
        elif data.startswith(MSG_IDENTIFIER):
            print("Message")
            receive_message(data)
        else:
            print("Unknown data type.")

    client_socket.close()

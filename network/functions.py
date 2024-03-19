import os
import constants as const


def recive_file(client_socket, initial_data):
    try:
        file_info = initial_data[len(const.FILE_IDENTIFIER):].decode(
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


def recive_message(initial_data):
    try:
        message = initial_data[len(const.MSG_IDENTIFIER):].decode(
            'utf-8', errors='replace')
        print("Message received:", message)
    except Exception as e:
        print(f"Error during message transfer: {e}")


def send_file(client_socket, file_path):
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


def send_message(client_socket):

    try:
        # Solicitar al usuario que ingrese el mensaje
        message = input("Ingrese el mensaje que desea enviar al servidor: ")

        # Enviar el mensaje al servidor
        client_socket.sendall(const.MSG_IDENTIFIER + message.encode('utf-8'))

        print("Mensaje enviado con éxito al servidor.")

    except Exception as e:
        print(f"Error durante el envío del mensaje: {e}")

def handle_client(client_socket, client_address):
    try:
        # Recibir el nombre del archivo y su tamaño
        file_info = client_socket.recv(1024).decode(
            'utf-8', errors='replace').split('@')
        print("Información del archivo recibida:", file_info)

        file_name = file_info[0]
        file_size = int(file_info[1])

        print(f"Recibiendo archivo: {file_name}, tamaño: {file_size} bytes")

        # Abrir un archivo para escribir los datos recibidos
        with open(file_name, 'wb') as file:
            # Recibir y escribir los datos en el archivo
            received_data = 0
            while received_data < file_size:
                data = client_socket.recv(1024)
                file.write(data)
                received_data += len(data)

        print("Archivo recibido con éxito.")

    except Exception as e:
        print(f"Error durante la transferencia del archivo: {e}")

    finally:
        # Cerrar la conexión del cliente
        client_socket.close()

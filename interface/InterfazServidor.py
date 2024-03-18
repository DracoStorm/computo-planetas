import socket
import threading
import tkinter as tk

# Lista de direcciones IP permitidas inicialmente vacía
allowed_ips = []

def handle_client(client_socket, client_address):
    try:
        # Recibir el nombre del archivo y su tamaño
        file_info = client_socket.recv(1024).decode('utf-8', errors='replace').split('@')
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

def add_ip():
    ip_address = ip_entry.get()
    if ip_address:
        allowed_ips.append(ip_address)
        ip_listbox.insert(tk.END, ip_address)
        ip_entry.delete(0, tk.END)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print('Esperando conexiones...')

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print('Conexión aceptada de', client_address)

            if client_address[0] not in allowed_ips:
                print(f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
                client_socket.close()
                continue

            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()

    except KeyboardInterrupt:
        print("Servidor cerrado manualmente.")

    finally:
        server_socket.close()

# Crear la ventana principal
window = tk.Tk()
window.title("Configuración de IP permitidas")

# Etiqueta y campo de entrada para la dirección IP
ip_label = tk.Label(window, text="Ingresar dirección IP:")
ip_label.pack()
ip_entry = tk.Entry(window)
ip_entry.pack()

# Botón para agregar la dirección IP a la lista
add_button = tk.Button(window, text="Agregar IP", command=add_ip)
add_button.pack()

# Lista de direcciones IP permitidas
ip_listbox = tk.Listbox(window)
ip_listbox.pack()

# Botón para iniciar el servidor
start_button = tk.Button(window, text="Iniciar servidor", command=start_server)
start_button.pack()

# Iniciar el bucle de la GUI
window.mainloop()
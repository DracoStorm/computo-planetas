import socket
import threading

def receive_messages_from_server(sock):
    while True:
        message = sock.recv(1024).decode()
        if not message:
            break
        print("\nMensaje recibido del servidor:", message)

def send_message_to_server(sock):
    while True:
        message = input("\nIngrese el mensaje que desea enviar al servidor: ")
        sock.send(message.encode())

# Dirección IP y puerto del servidor
server_ip = '127.0.0.1'
server_port = 443

# Creamos el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al servidor
client_socket.connect(('172.26.160.60', 443))
print("\nConexión establecida con el servidor.")

# Hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_messages_from_server, args=(client_socket,))
receive_thread.start()

# Hilo para enviar mensajes al servidor
send_thread = threading.Thread(target=send_message_to_server, args=(client_socket,))
send_thread.start()
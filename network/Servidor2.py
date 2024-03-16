import socket
import threading
import componentes_ips
import comp_threads.compute as tc
import comp_threads.frames as tf
import comp_threads.gen_frame as tgf


# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Cambiar a la dirección IP real del servidor
server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)
server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes

print('Esperando conexiones...')

try:
    while True:
        # Aceptar una conexión
        client_socket, client_address = server_socket.accept()
        print('Conexión aceptada de', client_address)

        # Verificar la dirección IP del cliente
        if client_address[0] not in componentes_ips.IPS:
            print(
                f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
            break

        if client_address[0] == componentes_ips.IPS[0]:
            client_handler = threading.Thread(
                target=tc.handle_client, args=(client_socket, client_address))
            client_handler.start()

        if client_address[0] == componentes_ips.IPS[1]:
            client_handler = threading.Thread(
                target=tf.handle_client, args=(client_socket, client_address))
            client_handler.start()

        if client_address[0] == componentes_ips.IPS[2]:
            client_handler = threading.Thread(
                target=tgf.handle_client, args=(client_socket, client_address))
            client_handler.start()

except KeyboardInterrupt:
    print("Servidor cerrado manualmente.")

finally:
    # Cerrar el socket del servidor
    server_socket.close()

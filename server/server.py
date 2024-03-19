import socket
import threading
import network.constants as const
import comp_threads.compute as compute_thread
import comp_threads.frames as frames_thread
import comp_threads.gen_frame as genframe_thread


def main() -> None:
    # Crear un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Cambiar a la dirección IP real del servidor
    server_address = (const.SERVER_IP, const.SERVER_PORT)
    server_socket.bind(server_address)
    server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes

    print('Esperando conexiones...')

    try:
        while True:
            # Aceptar una conexión
            client_socket, client_address = server_socket.accept()
            print('Conexión aceptada de', client_address)

            # Verificar la dirección IP del cliente
            if client_address[0] not in const.IPS:
                print(
                    f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
                break

            if client_address[0] == const.IPS[0]:
                comp_compute_traj = threading.Thread(
                    target=compute_thread.handle_client, name='component compute trajectory', args=(client_socket,))
                comp_compute_traj.start()
            if client_address[0] == const.IPS[0]:
                comp_compute_traj = threading.Thread(
                    target=frames_thread.handle_client, name='component frames', args=(client_socket,))
                comp_compute_traj.start()
            if client_address[0] == const.IPS[0]:
                comp_compute_traj = threading.Thread(
                    target=genframe_thread.handle_client, name='component generate frame', args=(client_socket,))
                comp_compute_traj.start()

    except KeyboardInterrupt:
        print("Servidor cerrado manualmente.")

    finally:
        # Cerrar el socket del servidor
        server_socket.close()


if __name__ == '__main__':
    main()

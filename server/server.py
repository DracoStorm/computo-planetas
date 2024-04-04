import socket
import threading
from network.constants import *
from comp_threads import compute_traj as compute_thread
from comp_threads import frames as frames_thread


def main() -> None:
    # Crear un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Cambiar a la dirección IP real del servidor
    server_address = (SERVER_IP, SERVER_PORT)
    server_socket.bind(server_address)
    server_socket.listen(5)  # Permitir hasta 5 conexiones pendientes
    barrier = threading.Barrier(2)
    coords: str=''
    lock = threading.Lock()
    print('Esperando conexiones...')

    try:
        while True:
            # Aceptar una conexión
            client_socket, client_address = server_socket.accept()
            print('Conexión aceptada de', client_address)

            # Verificar la dirección IP del cliente
            if client_address[0] not in IPS:
                print(
                    f"Intento de conexión desde una dirección IP no permitida: {client_address[0]}")
                break

            if client_address[0] == IPS[0]:
                comp_compute_traj = threading.Thread(
                    target=compute_thread.main, name='component compute trajectory', args=(client_socket, barrier, coords, lock))
                comp_compute_traj.start()
            if client_address[0] == IPS[1]:
                comp_compute_traj = threading.Thread(
                    target=frames_thread.handle_client, name='component frames', args=(client_socket,))
                comp_compute_traj.start()
            # if client_address[0] == const.IPS[0]:
            #     comp_compute_traj = threading.Thread(
            #         target=genframe_thread.handle_client, name='component generate frame', args=(client_socket,))
            #     comp_compute_traj.start()

    except KeyboardInterrupt:
        print("Servidor cerrado manualmente.")

    finally:
        # Cerrar el socket del servidor
        server_socket.close()


if __name__ == '__main__':
    main()

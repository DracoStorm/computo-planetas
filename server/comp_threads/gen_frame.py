import socket
from threading import Barrier, Lock
from network.constants import *
from network.exceptions import *
import network.functions as net
from PIL import Image


def main(client_socket: socket.socket, barrier: Barrier, coords: str, lock: Lock, iterations: int) -> None:

    coordinates: str
    for _ in range(iterations):
        imagen_enviada = Image.open(r'components/gen_frame/fondo.jpg')
        try:
            net.send_file(client_socket, "fondo.jpg", imagen_enviada.tobytes())

        except ComponentError:
            print('Error en el componente')
            # Actualizar la interfaz de usuario
            client_socket.close()
            barrier.abort()
        except BadNetType:
            # Actualizar la interfaz de usuario
            net.send_shutdown(client_socket)
            client_socket.close()
            barrier.abort()
        except Exception as e:
            # Actualizar la interfaz de usuario
            net.send_shutdown(client_socket)
            client_socket.close()
            print(f"Error durante la transferencia de datos: {e}")
            raise
        else:
            if net.receive_status(client_socket) == OK_IDENTIFIER:
                print(f'Paso: {_} imagen enviada con éxito')
            else:
                raise ComponentError

        try:
            # Recibir coordenadas del componente compute_traj
            coordinates = net.receive_message(client_socket)
            coords = coordinates
            print(f'Coordenadas recibidas: {coords}')
        except Exception as e:
            net.send_shutdown(client_socket)
            client_socket.close()
            print(f"Error al recibir coordenadas: {e}")
            raise

        if _ + 1 == iterations:
            break
        net.send_ok(client_socket)

    net.send_shutdown(client_socket)
    client_socket.close()
    print('Componente: Generate_frames :: finalizado con éxito')


if __name__ == "__main__":
    main()

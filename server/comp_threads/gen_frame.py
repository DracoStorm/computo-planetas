import socket
from threading import Barrier, Lock
from network.constants import *
from network.exceptions import *
import network.functions as net
from PIL import Image


def main(client_socket: socket.socket, barrier: Barrier, coords: str, lock: Lock, iterations: int) -> None:

    coordinates: str
    for _ in range(iterations):
        imagen_enviada = Image.open(r'components\gen_frame\fondo.jpg')
        try:
            coordinates = net.send_file(
                client_socket, "components/gen_frame/fondo.jpg", imagen_enviada.tobytes())
            print(coordinates)

        except ComponentError:
            print('ComponentError')
            # actualizar UI
            client_socket.close()
            barrier.abort()
        except BadNetType:
            # actualizar UI
            net.send_shutdown(client_socket)
            client_socket.close()
            barrier.abort()
        except Exception as e:
            # actualizar ui
            net.send_shutdown(client_socket)
            client_socket.close()
            print(f"Error during data transfer: {e}")
            raise
        else:
            print(f'Step: {_} current {coordinates=}')
            print("no recibi el mensaje")
            recivir_msg = net.receive_message(client_socket)
            print("recibi msg")

        # barrier.wait()

        # coords = coordinates
        # barrier.wait()
        print(recivir_msg)
        print("recibi mensaje")
        if _ + 1 == iterations:
            break
        net.send_ok(client_socket)

    net.send_shutdown(client_socket)
    client_socket.close()
    print('Component: Compute_trajectory :: finalized succesfully')


if __name__ == "__main__":
    main()

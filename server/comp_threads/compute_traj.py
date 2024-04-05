import socket
from threading import Barrier, Lock
from network.constants import *
import network.functions as net


def main(client_socket: socket.socket, barrier: Barrier, coords: str, lock: Lock) -> None:

    coordinates: str
    while True:
        try:

            coordinates = net.receive_message(client_socket)

        except 'Component Error' as e:
            # actualizar UI
            net.send_shutdown()
            client_socket.close()
            barrier.abort()
        except 'Incorrect Data Type' as e:
            # actualizar UI
            net.send_shutdown()
            client_socket.close()
            barrier.abort()
        except 'Unknown Data Type' as e:
            # actualizar UI
            net.send_shutdown()
            client_socket.close()
            barrier.abort()
        except Exception as e:
            # end UI
            net.send_shutdown()
            client_socket.close()
            print(f"Error during data transfer: {e}")
            raise
        else:
            print(coordinates)
            # barrier.wait()

        coords = coordinates
        net.send_ok(client_socket)


if __name__ == "__main__":
    main()

import socket
from threading import Barrier, Lock
from network.constants import *
import network.functions as net


def main(client_socket: socket.socket, barrier: Barrier, coords: str, lock: Lock) -> None:

    coordinates: str
    while True:
        try:
            while True:
                data: bytes = client_socket.recv(1024)
                if not data:
                    break
                elif data.startswith(ERR_IDENTIFIER):
                    raise 'Component Error'
                elif data.startswith(FILE_IDENTIFIER):
                    raise 'Incorrect Data Type'
                elif data.startswith(MSG_IDENTIFIER):
                    coordinates = net.recive_message(data)
                else:
                    raise 'Unknown Data Type'
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
            barrier.wait()

        if (lock.acquire(coords)):
            coords = coordinates
            lock.release()

        else:
            net.send_shutdown()
            raise 'Can\'t adquire the lock'
        barrier.wait()


if __name__ == "__main__":
    main()

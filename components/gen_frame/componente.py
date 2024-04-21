from ast import While
import numpy
import socket
from network import functions as net
from network.constants import *
from network.exceptions import *


def main():
    server_address = (SERVER_IP, SERVER_PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    print(f'Conected to server hosted in {SERVER_IP} using {SERVER_PORT} port')

    # Obtiene las condiciones iniciales
    # X, m1, m2 = astro_init.init()

    while True:

        try:
            # print ('Funciona')
            name, imagen = net.receive_file(client_socket)
            print(name)
        except ComponentError:
            # actualizar UI
            client_socket.close()
        except BadNetType:
            # actualizar UI
            net.send_error(client_socket)
            client_socket.close()
        except Exception as e:
            # actualizar gui
            net.send_error(client_socket)
            client_socket.close()
            raise
        else:
            try:
                net.send_ok(client_socket)
            except Exception as e:
                # actualizar gui
                net.send_error(client_socket)
                client_socket.close()
                raise
        try:
            status = net.recieve_status(client_socket)
            # print(status)
        except Exception as e:
            # actualizar gui
            net.send_error(client_socket)
            client_socket.close()
            raise
        print(f'Status: {status.decode()}')

        if (status == SHUTDOWN_IDENTIFIER):
            # actualizar UI
            client_socket.close()
            break
        elif (status != OK_IDENTIFIER):
            # actualizar UI
            raise BadNetType


if __name__ == "__main__":
    main()

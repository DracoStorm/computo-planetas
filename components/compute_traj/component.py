from ast import While
import numpy
import socket
from network.exceptions import BadNetType
import plot_animation as pl
from astro_physics import orbital_trajectory
from astro_physics import astro_init
from network.constants import *
from network import functions as net


def main():
    server_address = (SERVER_IP, SERVER_PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    print(f'Conected to server hosted in {SERVER_IP} using {SERVER_PORT} port')

    # Obtiene las condiciones iniciales
    X, m1, m2 = astro_init.init()

    while True:
        X = orbital_trajectory.calculate(X, m1, m2, h=5)
        p1: tuple[float, float] = (X[0], X[1])
        p2: tuple[float, float] = (X[2], X[3])

        print(str(p1) + ',' + str(p2))

        try:
            net.send_message(client_socket, str(p1)+','+str(p2))
        except Exception as e:
            # actualizar gui
            net.send_error()
            client_socket.close()
            raise

        try:
            status = net.recieve_status(client_socket)
        except Exception as e:
            # actualizar gui
            net.send_error()
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

import numpy
import socket
import plot_animation as pl
from astro_physics import orbital_trajectory
from astro_physics import astro_init
from network.constants import *
from network import functions as net

class UnknowType(Exception):
    "Raised when the input value is unkown"
    pass

def main():
    server_address = (SERVER_IP, SERVER_PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Conectar al servidor
    client_socket.connect(server_address)
    print(f'conected to server in {server_address}')
    # Obtiene las condiciones iniciales
    X, m1, m2 = astro_init.init()
    # Calcula la trayectoria con las condiciones iniciales
    # h es el valor del intervalo de tiempo, valores bajos son precisos pero muy costos
    # N es el total de pasos que se dan, determina la duración de la simulación
    N: int = 10
    for _ in range(N):
        X = orbital_trajectory.calculate(X, m1, m2, h=5)
        p1: tuple[float, float] = (X[0], X[1])
        p2: tuple[float, float] = (X[2], X[3])
        print(str(p1)+','+str(p2))
        try:
            net.send_message(client_socket, str(p1)+','+str(p2))
        except Exception as e:
            net.send_error()
            client_socket.close()
            break
        msg = net.receive_message(client_socket)
        print(f'msg: {msg}')
        if (msg == SHUTDOWN_IDENTIFIER):
            # actualizar UI
            socket.close()
            break
        elif (msg == OK_IDENTIFIER):
            print(f'paso {_}')
            continue
        else:
            #actualizar ui
            raise UnknowType

if __name__ == "__main__":
    main()
# Cliente
import os
import socket


def iniciar_cliente():
    # El cliente se conecta al servidor a través de un socket
    socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketCliente.connect(('172.26.166.146', 12345))
    while True:
        mensaje = input(
            "Escriba un mensaje o el nombre y ruta de un archivo para enviar: ")
        if not mensaje:
            break
        if mensaje.startswith("ARCHIVO:"):
            # Enviando un archivo al servidor
            partes = mensaje.split(":")
            rutaEnvio = partes[1]
            rutaDestino = partes[2]
            enviarArchivo(socketCliente, rutaEnvio, rutaDestino)
        else:
            # Enviando texto plano al servidor
            # Invocación a procedimiento remoto, el cliente envía datos al servidor para que los procese
            socketCliente.sendall(mensaje.encode('utf-8'))
            data = socketCliente.recv(1024)
            print(f"Recibido del servidor: {data.decode('utf-8')}")
    socketCliente.close()


def enviarArchivo(socketCliente, rutaEnvio, rutaDestino):
    socketCliente.sendall(f"ARCHIVO:{rutaEnvio}:{rutaDestino}".encode('utf-8'))
    with open(rutaEnvio, "rb") as f:
        while True:
            datosArchivo = f.read(1024)
            if not datosArchivo:
                break
            socketCliente.sendall(datosArchivo)
    socketCliente.sendall(b"FIN_ARCHIVO")


iniciar_cliente()

# Servidor
import os
import socket
import threading

# El servidor escucha en un socket para aceptar conexiones de clientes
def iniciarServidor():
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Dominio IPv4 y TCP
    direccionServer = ('localhost', 12345)
    socketServer.bind(direccionServer)
    socketServer.listen()
    print(f"Servidor listo en escucha en {direccionServer[0]}:{direccionServer[1]} (TCP)")
    while True:
        conexion, direccion = socketServer.accept()
        
        #Creación de hilo referenciado a hiloCliente
        hilo = threading.Thread(target=hiloCliente, args=(conexion, direccion))
        hilo.start()

def hiloCliente(conexion, direccion):
    print(f"Conexión desde {direccion}")
    # Llamada a procedimiento remoto, el servidor recibe datos del cliente y los procesa
    #Si se recibe texto
    while True:
        texto = conexion.recv(1024)
        if not texto:
            break
        mensaje = texto.decode('utf-8')
    #Si se recibe un archivo
        if mensaje.startswith("ARCHIVO:"):
            partes = mensaje.split(":")
            rutaEnvio = partes[1]
            rutaDestino = partes[2]
            print(f"Recibiendo archivo {rutaEnvio} de {direccion}")
            with open(rutaDestino, "wb") as f:
                while True:
                    datosArchivo = conexion.recv(1024)
                    if datosArchivo == b"FIN_ARCHIVO":
                        break
                    f.write(datosArchivo)
            tamanoArchivo = os.path.getsize(rutaDestino)
            print(f"Archivo {rutaEnvio} recibido de {direccion} y guardado en {rutaDestino} ({tamanoArchivo} bytes)")
        else:
            print(f"Recibido de {direccion}: {mensaje}")
            conexion.sendall(texto)
    conexion.close()

iniciarServidor()
#CODIGO DE SERVIDOR 

import socket

def recibir_imagen(server_socket):
    conn, addr = server_socket.accept()
    print(f"Conexión aceptada de {addr}")
    
    # Recibir los bytes de la imagen
    buffer = bytearray()
    while True:
        packet = conn.recv(4096)
        if not packet:
            break
        buffer.extend(packet)
    
    # Guardar los bytes recibidos como una imagen
    with open("imagen_recibida.png", "wb") as f:
        f.write(buffer)
    
    print("Imagen recibida y guardada como 'imagen_recibida.png'")
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Servidor escuchando en el puerto 12345")
    
    try:
        while True:
            recibir_imagen(server_socket)
    except KeyboardInterrupt:
        print("Servidor cerrado manualmente.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

import socket
from PIL import Image
from io import BytesIO

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
    
    # Convertir los bytes recibidos en una imagen PIL
    imagen_recibida = Image.open(BytesIO(buffer))
    
    # Guardar la imagen recibida como un archivo PNG
    imagen_recibida.save("imagen_recibida.png")
    print("Imagen recibida y guardada como 'imagen_recibida.png'")
    
    # Mostrar la imagen recibida
    imagen_recibida.show()
    
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

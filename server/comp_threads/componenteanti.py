#componente prueba 1 de antialising cliente 
import socket
from threading import Barrier, Lock
from network.constants import *
from network.exceptions import *
import network.functions as net
from PIL import Image
from io import BytesIO


def cargar_imagen(ruta):
    # Carga una imagen desde la ruta especificada
    imagen = Image.open(ruta)
    return imagen


def convertir_imagen_a_bytes(imagen):
    # Convierte la imagen en bytes para enviarla a través del socket
    buffer = BytesIO()
    imagen.save(buffer, format="PNG")  # Guardar como PNG en lugar de JPEG
    imagen_bytes = buffer.getvalue()
    return imagen_bytes


def main(client_socket: socket.socket, barrier: Barrier, coords: str, lock: Lock, iterations: int):
    # Configuración del servidor
    
    # Ruta de la imagen que deseas enviar al servidor
    ruta_imagen = "C:/Users/alfre/OneDrive/Imágenes/Saved Pictures/logobuap.png"
    
    # Cargar la imagen
    imagen_original = cargar_imagen(ruta_imagen)
    
    # Convertir la imagen a bytes
    imagen_bytes = convertir_imagen_a_bytes(imagen_original)
    
    
    
    try:
        
        # Enviar la imagen al servidor
        net.send_file(client_socket,"fondo",imagen_bytes)
        print("Imagen enviada al servidor")
        
        # Recibir la imagen procesada del servidor
        imagen_procesada_bytes = cliente_socket.recv(4096)
        
        # Convertir los bytes recibidos en una imagen PIL
        imagen_procesada = Image.open(BytesIO(imagen_procesada_bytes))
        
        # Mostrar la imagen procesada
        imagen_procesada.show()
        print("Imagen procesada recibida del servidor")
        
    finally:
        # Cerrar el socket del cliente
        cliente_socket.close()


if __name__ == "__main__":
    main()

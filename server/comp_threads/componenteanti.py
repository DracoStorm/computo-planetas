#componente prueba 1 de antialising cliente 
import socket
from PIL import Image
from io import BytesIO


def cargar_imagen(ruta):
    # Carga una imagen desde la ruta especificada
    imagen = Image.open(ruta)
    return imagen


def convertir_imagen_a_bytes(imagen):
    # Convierte la imagen en bytes para enviarla a través del socket
    buffer = BytesIO()
    imagen.save(buffer, format="JPEG")
    imagen_bytes = buffer.getvalue()
    return imagen_bytes


def main():
    # Configuración del servidor
    host = '127.0.0.1'
    puerto = 12345
    
    # Ruta de la imagen que deseas enviar al servidor
    ruta_imagen = "mi_imagen.jpg"
    
    # Cargar la imagen
    imagen_original = cargar_imagen(ruta_imagen)
    
    # Convertir la imagen a bytes
    imagen_bytes = convertir_imagen_a_bytes(imagen_original)
    
    # Crear el socket del cliente
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor
        cliente_socket.connect((host, puerto))
        
        # Enviar la imagen al servidor
        cliente_socket.send(imagen_bytes)
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

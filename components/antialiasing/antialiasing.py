#servidor de antialising 
import socket
from PIL import Image, ImageFilter
from io import BytesIO


def cargar_imagen_desde_bytes(data_bytes):
    # Convierte los bytes recibidos en una imagen PIL
    imagen = Image.open(BytesIO(data_bytes))
    return imagen


def aplicar_antialiasing(imagen, radio=2):
    # Aplica antialiasing a la imagen utilizando un filtro gaussiano
    imagen_suavizada = imagen.filter(ImageFilter.GaussianBlur(radius=radio))
    return imagen_suavizada


def procesar_imagen(data_bytes):
    # Carga la imagen desde los bytes recibidos
    imagen_original = cargar_imagen_desde_bytes(data_bytes)
    
    # Aplica el efecto antialiasing a la imagen
    imagen_suavizada = aplicar_antialiasing(imagen_original)
    
    # Convierte la imagen suavizada a bytes
    buffer = BytesIO()
    imagen_suavizada.save(buffer, format="JPEG")
    imagen_suavizada_bytes = buffer.getvalue()
    
    return imagen_suavizada_bytes


def main():
    # Configuración del servidor
    host = '127.0.0.1'
    puerto = 12345
    
    # Crear el socket del servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(1)
    
    print("Servidor escuchando en el puerto", puerto)
    
    while True:
        # Aceptar conexiones entrantes
        cliente_socket, direccion = servidor_socket.accept()
        print("Conexión establecida desde", direccion)
        
        # Recibir datos del cliente (imagen en bytes)
        data_bytes = cliente_socket.recv(4096)
        print("Imagen recibida desde el cliente")
        
        # Procesar la imagen
        imagen_procesada_bytes = procesar_imagen(data_bytes)
        
        # Enviar la imagen procesada de vuelta al cliente
        cliente_socket.send(imagen_procesada_bytes)
        print("Imagen procesada enviada al cliente")
        
        # Cerrar la conexión con el cliente
        cliente_socket.close()


if __name__ == "__main__":
    main()

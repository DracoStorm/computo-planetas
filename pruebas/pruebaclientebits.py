import socket
from PIL import Image
from io import BytesIO

def cargar_imagen(ruta):
    """Carga una imagen desde la ruta especificada"""
    imagen = Image.open(ruta)
    return imagen

def aplicar_antialiasing(imagen):
    """Aplica un efecto de antialiasing a la imagen"""
    # Redimensionar la imagen a un tamaño más grande y luego reducirla para suavizar los bordes
    imagen_grande = imagen.resize((imagen.width * 2, imagen.height * 2), Image.LANCZOS)
    imagen_antialias = imagen_grande.resize((imagen.width, imagen.height), Image.LANCZOS)
    return imagen_antialias

def convertir_imagen_a_bytes(imagen):
    """Convierte la imagen en bytes para enviarla a través del socket"""
    buffer = BytesIO()
    imagen.save(buffer, format="PNG")  # Guardar como PNG en lugar de JPEG
    imagen_bytes = buffer.getvalue()
    return imagen_bytes

def enviar_imagen(client_socket, imagen_bytes):
    client_socket.sendall(imagen_bytes)
    print("Imagen enviada al servidor")

def main():
    # Ruta de la imagen que deseas procesar
    ruta_imagen = "C:/Users/alfre/OneDrive/Escritorio/LOBOS PUEBLA/_8913d348-0dca-473d-9b92-a2e68011c6e0.jpg"
    
    # Cargar la imagen
    imagen_original = cargar_imagen(ruta_imagen)
    
    # Aplicar el efecto de antialiasing
    imagen_procesada = aplicar_antialiasing(imagen_original)
    
    # Convertir la imagen procesada a bytes
    imagen_bytes = convertir_imagen_a_bytes(imagen_procesada)
    
    # Conectar al servidor y enviar la imagen
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    enviar_imagen(client_socket, imagen_bytes)
    client_socket.close()

if __name__ == "__main__":
    main()

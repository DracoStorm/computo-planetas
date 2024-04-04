import cv2
from gen_frame import generar_imagenes_superpuestas

def generar_video_salida(nombre_video_salida, imagenes_superpuestas, fps=5):
    # Primero, establece las dimensiones del video según las dimensiones de la primera imagen
    alto, ancho, _ = imagenes_superpuestas[0].shape
    dimensiones_video = (ancho, alto)

    # Define el codec de video
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    video_salida = cv2.VideoWriter(nombre_video_salida, codec, fps, dimensiones_video)

    # Escribe cada imagen del array al video
    for imagen in imagenes_superpuestas:
        # Convierte la imagen de formato BGR a formato RGB
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # Escribe la imagen en el video
        video_salida.write(imagen_rgb)

    # Cierra el objeto VideoWriter
    video_salida.release()

    print("Video generado exitosamente:", nombre_video_salida)

# Llama a la función para generar las imágenes superpuestas
imagenes_superpuestas = generar_imagenes_superpuestas()

# Llama a la función para generar el video de salida
generar_video_salida("video_salida.mp4", imagenes_superpuestas)
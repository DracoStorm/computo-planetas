import cv2
from PIL import Image
import numpy as np
#from frames import gen_frame  # Importa la función desde el módulo

def generar_imagenes_superpuestas(num_imagenes=5000):

    imagen_principal = Image.open(r"components\gen_frame\Fondo.jpeg")

    imagenes_superpuestas = []

    # Itera sobre un rango de num_imagenes
    for i in range(num_imagenes):
        # Abre la imagen del frame actual
        ruta_frame = fr"animation\frames\marte\frame_{i % 10}.png"
        imagen_superpuesta = Image.open(ruta_frame)

        res_img = gen_frame(imagen_principal, imagen_superpuesta)
        # Convierte la imagen resultante a una matriz numpy y agrega a la lista
        imagenes_superpuestas.append(np.array(res_img))

        # Cierra la imagen del frame actual
        imagen_superpuesta.close()

    imagen_principal.close()

    return imagenes_superpuestas

def generar_video_salida(nombre_video_salida, imagenes_superpuestas, fps=5):
    if not imagenes_superpuestas:
        print("No se generaron imágenes superpuestas.")
        return

    # Primero, establece las dimensiones del video según las dimensiones de la primera imagen
    alto, ancho, _ = imagenes_superpuestas[0].shape
    dimensiones_video = (ancho, alto)

    # Define el codec de video y crea un objeto VideoWriter
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

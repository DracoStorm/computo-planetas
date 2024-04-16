import numpy as np
import cv2
from PIL import Image

def gen_frame(background: Image.Image, planet_1: Image.Image) -> Image.Image:
    # Obtiene las dimensiones de la imagen de fondo
    sx, sy = background.size

    rx = 1
    ry = 3
    fx = sy / rx
    fy = sy / ry

    cx = 0.5
    cy = 0.5
    px = cx * fx
    px = int(np.round(px))
    py = cy * fy
    py = int(np.round(py))
    # Superpone la imagen sobre la imagen principal
    imagen_resultante = background.copy()
    imagen_resultante.paste(planet_1, (px, py), planet_1)

    return imagen_resultante  # Devuelve la imagen resultante

def generar_imagenes_superpuestas_y_video(nombre_video_salida="video2.mp4", fps=5, num_imagenes=5000):
    # Carga la imagen de fondo (reemplaza "ruta/de/tu/imagen.jpg" por la ruta de tu imagen de fondo)
    background_path = r"components/gen_frame/Fondo.jpeg"
    background = Image.open(background_path)

    imagenes_superpuestas = []

    # Itera sobre un rango de num_imagenes
    for i in range(num_imagenes):
        # Abre la imagen del frame actual
        ruta_frame = r"animation\frames\marte\frame_"+str(i % 10)+r".png"
        imagen_superpuesta = Image.open(ruta_frame)

        background = gen_frame(background, imagen_superpuesta)

        # Convierte la imagen resultante a una matriz numpy y agrega a la lista
        imagenes_superpuestas.append(np.array(background))

        # Cierra la imagen del frame actual
        imagen_superpuesta.close()

    background.close()

    # Llama a la función para generar el video de salida
    if imagenes_superpuestas:
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
    else:
        print("No se generaron imágenes superpuestas.")

# Llama a la función para generar imágenes superpuestas y el video de salida
generar_imagenes_superpuestas_y_video()

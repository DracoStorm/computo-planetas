import cv2
import numpy as np
from gen_frame import imagenes_superpuestas 

# Supongamos que tienes un array numpy llamado imagenes_superpuestas
# donde cada elemento es una imagen superpuesta

# Primero, establece las dimensiones del video según las dimensiones de la primera imagen
alto, ancho, _ = imagenes_superpuestas[0].shape
dimensiones_video = (ancho, alto)

# Especifica el nombre del archivo de video de salida
nombre_video_salida = "video_salida.mp4"

# Define el codec de video y crea un objeto VideoWriter
codec = cv2.VideoWriter_fourcc(*"mp4v")
fps = 5  # Reducir la cantidad de cuadros por segundo
video_salida = cv2.VideoWriter(nombre_video_salida, codec, fps, dimensiones_video)

# Escribe cada imagen del array al video
for imagen in imagenes_superpuestas:
    # Convierte la imagen de formato BGR a formato RGB (OpenCV usa BGR por defecto)
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    # Escribe la imagen en el video
    video_salida.write(imagen_rgb)

# Cierra el objeto VideoWriter
video_salida.release()

print("Video generado exitosamente:", nombre_video_salida)

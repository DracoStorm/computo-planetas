import os
import cv2
import numpy as np
from PIL import Image, ImageSequence

# Ruta del archivo de video anterior
previous_video_path = 'animation/Video/video_comprimido.mp4'

# Eliminar el archivo de video anterior si existe
if os.path.exists(previous_video_path):
    os.remove(previous_video_path)

# Abrir el archivo GIF y obtener sus cuadros
gif_path = 'animacion.gif'
frames = []
with Image.open(gif_path) as img:
    frames = [np.array(frame.convert('RGB')) for frame in ImageSequence.Iterator(img)]

# Especificar el formato de salida y el códec de compresión para formato .mp4
output_path = 'animation/Video/video_comprimido.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Utilizamos el códec MP4V
fps = 1  # Reducimos la tasa de frames para hacer el video más lento

# Crear el objeto VideoWriter
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (frames[0].shape[1], frames[0].shape[0]))

# Escribir cada frame en el archivo de video
for frame in frames:
    video_writer.write(frame)

# Liberar recursos
video_writer.release()
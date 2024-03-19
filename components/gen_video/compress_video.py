import os
import cv2

# Carpeta que contiene las imágenes
folder_path = 'animation/frames/marte/'

# Especificar el formato de salida y el códec de compresión para formato .mp4
output_path = 'animation/Video/video_comprimido.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Utilizamos el códec MP4V
fps = 1  # Reducimos la tasa de frames para hacer el video más lento

# Obtener la lista de archivos en la carpeta
image_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])

# Leer la primera imagen para obtener las dimensiones
img = cv2.imread(image_files[0])
height, width, _ = img.shape

# Crear el objeto VideoWriter
video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Escribir cada imagen en el archivo de video
for image_file in image_files:
    img = cv2.imread(image_file)
    video_writer.write(img)

# Liberar recursos
video_writer.release()
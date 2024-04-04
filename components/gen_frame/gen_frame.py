import numpy as np
from PIL import Image

sx = 473 
sy = 316
rx = 1
ry = 3
fx = sy / rx
fy = sy / ry

cx = 0.5
cy = 0.5
px = cx * fx
px = int(np.round(px))  # Convertir a entero
py = cy * fy
py = int(np.round(py))  # Convertir a entero

a = np.zeros((sx, sy))

# Abre la imagen principal
imagen_principal = Image.open(r"components\gen_frame\Fondo.jpeg")

# Lista para almacenar las imágenes superpuestas
imagenes_superpuestas = []

# Itera sobre un rango de 5000
for i in range(5000):
    # Abre la imagen del frame actual
    ruta_frame = fr"animation\frames\marte\frame_{i % 10}.png"  # Usa el módulo para repetir las imágenes del 0 al 9
    imagen_superpuesta = Image.open(ruta_frame)

    # Superpone la imagen sobre la imagen principal
    imagen_resultante = imagen_principal.copy()
    imagen_resultante.paste(imagen_superpuesta, (px, py), imagen_superpuesta)
    
    # Convierte la imagen resultante a una matriz numpy y agrega a la lista
    imagenes_superpuestas.append(np.array(imagen_resultante))

    # Cierra la imagen del frame actual
    imagen_superpuesta.close()

imagen_principal.close()

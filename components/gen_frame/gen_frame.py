import numpy as np
from PIL import Image

def generar_imagenes_superpuestas(num_imagenes=5000):
    sx = 473 
    sy = 316
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

    a = np.zeros((sx, sy))

    imagen_principal = Image.open(r"components\gen_frame\Fondo.jpeg")

    imagenes_superpuestas = []

    # Itera sobre un rango de num_imagenes
    for i in range(num_imagenes):
        # Abre la imagen del frame actual
        ruta_frame = fr"animation\frames\marte\frame_{i % 10}.png"
        imagen_superpuesta = Image.open(ruta_frame)

        # Superpone la imagen sobre la imagen principal
        imagen_resultante = imagen_principal.copy()
        imagen_resultante.paste(imagen_superpuesta, (px, py), imagen_superpuesta)
        
        # Convierte la imagen resultante a una matriz numpy y agrega a la lista
        imagenes_superpuestas.append(np.array(imagen_resultante))

        # Cierra la imagen del frame actual
        imagen_superpuesta.close()

    imagen_principal.close()

    return imagenes_superpuestas
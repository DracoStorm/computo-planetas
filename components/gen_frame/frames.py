import numpy as np
from PIL import Image


def gen_frame(background: Image.Image, planet_1: Image.Image) -> Image.Image:
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
    # Superpone la imagen sobre la imagen principal
    imagen_resultante = background.copy()
    imagen_resultante.paste(planet_1, (px, py), planet_1)
    
    return imagen_resultante  # Devuelve la imagen resultante


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
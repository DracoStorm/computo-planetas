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
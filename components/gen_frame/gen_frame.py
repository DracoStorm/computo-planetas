import numpy as np
from PIL import Image

sx = 630 
sy = 473
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

# Itera sobre los frames del 0 al 9
for i in range(10):
    # Abre la imagen del frame actual
    ruta_frame = fr"animation\frames\marte\frame_{i}.png"
    imagen_superpuesta = Image.open(ruta_frame)

    # Superpone la imagen sobre la imagen principal
    imagen_resultante = imagen_principal.copy()
    imagen_resultante.paste(imagen_superpuesta, (px, py), imagen_superpuesta)
    
    # Guarda la imagen superpuesta en un archivo
    nombre_archivo = f"imagen_superpuesta_{i}.png"
    imagen_resultante.save(nombre_archivo)

    # Cierra la imagen del frame actual
    imagen_superpuesta.close()

# Cierra la imagen principal
imagen_principal.close()
import numpy as np
from PIL import Image
import imageio

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
imagen_principal = Image.open(r"simulation\astro_physics\fondo.jpg")

# Lista para almacenar los frames superpuestos
frames_superpuestos = []

# Itera sobre los frames del 0 al 9
for i in range(10):
    # Abre la imagen del frame actual
    ruta_frame = fr"animation\frames\marte\frame_{i}.png"
    imagen_superpuesta = Image.open(ruta_frame)

    # Superpone la imagen sobre la imagen principal
    imagen_resultante = imagen_principal.copy()
    imagen_resultante.paste(imagen_superpuesta, (px, py), imagen_superpuesta)
    
    # Agrega la imagen superpuesta a la lista de frames
    frames_superpuestos.append(np.array(imagen_resultante))

    # Cierra la imagen del frame actual
    imagen_superpuesta.close()

# Guarda los frames superpuestos como un GIF animado
imageio.mimsave("animacion.gif", frames_superpuestos, duration=1)  # Duración de 1 segundo entre cada frame

# Cierra la imagen principal
imagen_principal.close()
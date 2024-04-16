import numpy as np
import cv2
from PIL import Image

def gen_frame(background: Image.Image, planet_1: Image.Image) -> Image.Image:
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

    imagen_resultante = background.copy()
    imagen_resultante.paste(planet_1, (px, py), planet_1)

    return imagen_resultante

def generar_imagenes_superpuestas(background_path: str, num_imagenes: int) -> list:
    background = Image.open(background_path)
    imagenes_superpuestas = []

    for i in range(num_imagenes):
        ruta_frame = r"animation\frames\marte\frame_"+str(i % 10)+r".png"
        imagen_superpuesta = Image.open(ruta_frame)

        background = gen_frame(background, imagen_superpuesta)
        imagenes_superpuestas.append(np.array(background))

        imagen_superpuesta.close()

    background.close()

    return imagenes_superpuestas

def generar_video(imagenes_superpuestas: list, nombre_video_salida: str, fps: int):
    if imagenes_superpuestas:
        alto, ancho, _ = imagenes_superpuestas[0].shape
        dimensiones_video = (ancho, alto)

        codec = cv2.VideoWriter_fourcc(*"mp4v")
        video_salida = cv2.VideoWriter(nombre_video_salida, codec, fps, dimensiones_video)

        for imagen in imagenes_superpuestas:
            imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            video_salida.write(imagen_rgb)

        video_salida.release()

        print("Video generado exitosamente:", nombre_video_salida)
    else:
        print("No se generaron imágenes superpuestas.")

# Uso de las funciones separadas
def main():
    background_path = r"components/gen_frame/Fondo.jpeg"
    nombre_video_salida = "video2.mp4"
    fps = 5
    num_imagenes = 5000

    imagenes_superpuestas = generar_imagenes_superpuestas(background_path, num_imagenes)
    generar_video(imagenes_superpuestas, nombre_video_salida, fps)

if __name__ == "__main__":
    main()
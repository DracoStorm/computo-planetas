import os
from PIL import Image, ImageDraw, ImageSequence

# Ruta de la carpeta gif y fotogramas desde la raiz
RUTA_GIF = r"animation/gifs/"
RUTA_FOTOGRAMAS = r"animation/fotogramas/"
RUTA_FOTOGRAMAS_RECORTADOS = r"animation/fotogramasrecortados/"


def recortar_en_elipse(imagen, carpeta_destino, nombre_archivo):
    # Coordenadas del elipse (ajústalas según tus necesidades)
    #elipse_coords = (16, 4, 235, 220)  # (x0, y0, x1, y1) Mercurio
    elipse_coords = (200, 29, 510, 337)  # (x0, y0, x1, y1) Marte
    # Crear una máscara de elipse
    mascara = Image.new('L', imagen.size, 0)
    draw = ImageDraw.Draw(mascara)
    draw.ellipse(elipse_coords, fill=255)

    # Aplicar la máscara al recortar la imagen
    imagen_recortada = Image.new('RGBA', imagen.size, (0, 0, 0, 0))
    imagen_recortada.paste(imagen, mask=mascara)

    # Crear la carpeta de destino para el GIF recortado si no existe
    os.makedirs(carpeta_destino, exist_ok=True)

    # Guardar la imagen recortada en la carpeta de destino
    nombre_archivo_recortado = os.path.join(carpeta_destino, f"recortada_{nombre_archivo}")
    imagen_recortada.save(nombre_archivo_recortado, 'PNG')

    print(f"Imagen recortada guardada en la carpeta '{carpeta_destino}' como '{nombre_archivo_recortado}'.")


# Carpeta donde se encuentran las imágenes originales (fotogramas desmontados)
carpeta_origen = os.path.join(RUTA_FOTOGRAMAS, "marte")

# Carpeta donde se guardarán las imágenes recortadas
carpeta_destino = os.path.join(RUTA_FOTOGRAMAS_RECORTADOS, "marte")

# Recortar todas las imágenes desmontadas en la carpeta de origen y guardarlas en la carpeta de destino
archivos_imagen = os.listdir(carpeta_origen)
for archivo_imagen in archivos_imagen:
    ruta_imagen = os.path.join(carpeta_origen, archivo_imagen)
    imagen_original = Image.open(ruta_imagen).convert('RGBA')

    # Recortar en elipse y guardar en la carpeta de destino
    recortar_en_elipse(imagen_original, carpeta_destino, archivo_imagen)

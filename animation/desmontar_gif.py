import os
from PIL import Image, ImageSequence


# Ruta de la carpeta gif y fotogramas desde la raiz
RUTA_GIF = r"animation/gifs/"
RUTA_FOTOGRAMAS = r"animation/fotogramas/"


def desmontar_gif(archivo_gif):
    """
        Desmonta el gif en cada frame que lo contiene y lo deposita en la carpta RUTA_FOTOGRAMAS.

            Parameters
            ----------
                arhivo_gif : string
                    Nombre de un archivo dentro de RUTA_GIF.

            Exceptions
            ----------
                Si la ruta del archivo o destino no es encontrada.
    """

    # Verfifica si el directorio "fotogramas" existe, si no lo crea.
    if (not os.path.isdir(RUTA_FOTOGRAMAS)):
        os.mkdir(RUTA_FOTOGRAMAS)

    # Verfifica si el directorio "animation/fotogramas/archivo_gif" existe, si no lo crea.
    # De esta manera existe una carpeta por cada gif.
    RUTA_FOTOGRAMAS_GIF = RUTA_FOTOGRAMAS + archivo_gif + r"/"
    if (not os.path.isdir(RUTA_FOTOGRAMAS_GIF)):
        os.mkdir(RUTA_FOTOGRAMAS_GIF)

    gif = Image.open(RUTA_GIF + archivo_gif + ".gif")

    try:
        # Extrae todos los fotogramas del GIF
        fotogramas = [f.convert("RGBA") for f in ImageSequence.Iterator(gif)]

        # Guarda cada fotograma como una imagen separada
        for i, fotograma in enumerate(fotogramas):
            archivo_png = RUTA_FOTOGRAMAS_GIF + f"fotograma_{i}.png"
            fotograma.save(archivo_png, "PNG")

        print(
            f"Se han desmontado correctamente {len(fotogramas)} fotogramas del gif {archivo_gif} en la carpeta {RUTA_FOTOGRAMAS_GIF}.")
    except Exception as e:
        print(f"Error al desmontar el GIF: {e}")


# Desmontar el GIF
desmontar_gif("marte")

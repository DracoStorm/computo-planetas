import os
from PIL import Image, ImageSequence


# Ruta de la carpeta gif y fotogramas desde la raiz
PATH_GIF = r"animation/gifs/"
PATH_FRAME = r"animation/frames/"


def desmontar_gif(file):
    """
        Desmonta el gif en cada frame que lo contiene y lo deposita en la carpta PATH_FRAMES.

            Parameters
            ----------
                file : string
                    Nombre de un archivo .gif dentro de PATH_GIF.

            Exceptions
            ----------
                Si el archivo no existe.
    """

    # Verfifica si el directorio "./animation/frames/" existe, si no lo crea.
    if (not os.path.isdir(PATH_FRAME)):
        os.mkdir(PATH_FRAME)

    # Verfifica si el directorio "./animation/frames/file/" existe, si no lo crea.
    # De esta manera existe una carpeta por cada gif.
    PATH_FRAME_GIF = PATH_FRAME + file + r"/"
    if (not os.path.isdir(PATH_FRAME_GIF)):
        os.mkdir(PATH_FRAME_GIF)

    gif = Image.open(PATH_GIF + file + ".gif")

    try:
        # Extrae todos los frames del file
        frames = [f.convert("RGBA") for f in ImageSequence.Iterator(gif)]

        # Guarda cada frame como una imagen separada
        for i, frame in enumerate(frames):
            name_frame = PATH_FRAME_GIF + f"frame_{i}.png"
            frame.save(name_frame, "PNG")

        print(
            f"Se han desmontado correctamente {len(frames)} frames del gif {file} en la carpeta {PATH_FRAME_GIF}.")
    except Exception as e:
        print(f"Error al desmontar el GIF: {e}")


# Desmontar el GIF
desmontar_gif("marte")

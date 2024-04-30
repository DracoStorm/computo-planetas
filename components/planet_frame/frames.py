import os
from PIL import Image, ImageSequence, ImageDraw


# Ruta de la carpeta gif y fotogramas desde la raiz
PATH_GIF = r"planet_frame\\gifs"
PATH_FRAMES = r"planet_frame\\gifs\\frames"


def unmount_gif(file: str) -> str:
    """
        Desmonta el gif en cada frame que lo contiene y lo deposita en la carpta RUTA_FRAMES.

            Parameters
            ----------
                file: str
                    Nombre de un file dentro de RUTA_GIF.

            Exceptions
            ----------
                Si la ruta del file o destino no es encontrada.
    """

    # Verfifica si el directorio "frames" existe, si no lo crea.
    if (not os.path.isdir(PATH_FRAMES)):
        os.mkdir(PATH_FRAMES)

    # Verfifica si el directorio "animation/frames/file_gif" existe, si no lo crea.
    # De esta manera existe una carpeta por cada gif.
    PATH_FRAMES_FILE = PATH_FRAMES + file + r"/"
    if (not os.path.isdir(PATH_FRAMES_FILE)):
        os.mkdir(PATH_FRAMES_FILE)

    gif = Image.open(PATH_GIF + file + ".gif")

    try:
        # Extrae todos los frames del GIF
        frames = [f.convert("RGBA") for f in ImageSequence.Iterator(gif)]

        # Guarda cada frame como una frame separada
        for i, frame in enumerate(frames):
            file_png = PATH_FRAMES_FILE + f"frame_{i}.png"
            frame.save(file_png, "PNG")

    except Exception as e:
        print(f"Error al desmontar el GIF: {e}")

    return PATH_FRAMES_FILE


def re_scale(file: str, new_size: tuple[int, int]) -> Image: # type: ignore
    # Iterar sobre cada file en la carpeta
    # Abrir la frame
    frame = Image.open(PATH_FRAMES+file)

    # Rescalar la frame
    return frame.resize(new_size) # type: ignore


def cut_elipse(file: Image) -> Image: # type: ignore
    file.convert('RGBA')
    # Coordenadas del elipse (ajústalas según tus necesidades)
    # elipse_coords = (16, 4, 235, 220)  # (x0, y0, x1, y1) Mercurio
    elipse_coords = (200, 29, 510, 337)  # (x0, y0, x1, y1) Marte
    # Crear una máscara de elipse
    mask = Image.new('L', file.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(elipse_coords, fill=255)

    # Aplicar la máscara al recortar la frame
    frame_cut = Image.new('RGBA', file.size, (0, 0, 0, 0))
    frame_cut.paste(file, mask=mask)

    return frame_cut

    # # Recortar todas las imágenes desmontadas en la carpeta de origen y guardarlas en la carpeta de destino
    # files_frame = os.listdir(carpeta_origen)
    # for file_frame in files_frame:
    #     ruta_frame = os.path.join(carpeta_origen, file_frame)
    #     frame_original = Image.open(ruta_frame).convert('RGBA')
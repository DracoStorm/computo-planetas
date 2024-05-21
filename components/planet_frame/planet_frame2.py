import os
from PIL import Image, ImageSequence, ImageDraw

# Ruta de la carpeta gif y fotogramas desde la raiz
PATH_GIFS = r"planet_frame/gifs/"
PATH_FRAMES = r"planet_frame/gifs/frames/"


def unmount_gif(file):
    """
    Desmonta el GIF en cada frame que lo contiene y lo deposita en la carpeta PATH_FRAMES.

    Parameters:
        file (str): Nombre del archivo GIF dentro de PATH_GIFS.

    Returns:
        str: Ruta de la carpeta donde se guardan los frames desmontados del GIF.
    """
    # Verifica si el directorio "frames" existe, si no lo crea.
    if not os.path.isdir(PATH_FRAMES):
        os.mkdir(PATH_FRAMES)

    # Verifica si el directorio "frames/file_gif" existe, si no lo crea.
    # De esta manera existe una carpeta por cada GIF.
    path_frames_file = os.path.join(PATH_FRAMES, file)
    if not os.path.isdir(path_frames_file):
        os.mkdir(path_frames_file)

    gif = Image.open(os.path.join(PATH_GIFS, file))

    try:
        # Extrae todos los frames del GIF
        frames = [f.convert("RGBA") for f in ImageSequence.Iterator(gif)]

        # Guarda cada frame como un archivo separado
        for i, frame in enumerate(frames):
            frame_path = os.path.join(path_frames_file, f"frame_{i}.png")
            frame.save(frame_path, "PNG")

    except Exception as e:
        print(f"Error al desmontar el GIF '{file}': {e}")

    return path_frames_file


def re_scale(file, new_size):
    """
    Rescala una imagen al nuevo tamaño especificado.

    Parameters:
        file (str): Ruta de la imagen a rescalar.
        new_size (tuple): Nuevo tamaño de la imagen (ancho, alto).

    Returns:
        Image: Imagen rescalada.
    """
    # Abrir la imagen
    image = Image.open(file)

    # Rescalar la imagen
    return image.resize(new_size)


def cut_elipse(image):
    """
    Recorta una imagen en forma de elipse.

    Parameters:
        image (Image): Imagen a recortar.

    Returns:
        Image: Imagen recortada en forma de elipse.
    """
    image.convert('RGBA')
    # Coordenadas del elipse (ajústalas según tus necesidades)
    # elipse_coords = (16, 4, 235, 220)  # (x0, y0, x1, y1) Mercurio
    elipse_coords = (200, 29, 510, 337)  # (x0, y0, x1, y1) Marte
    # Crear una máscara de elipse
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse(elipse_coords, fill=255)

    # Aplicar la máscara al recortar la imagen
    image_cut = Image.new('RGBA', image.size, (0, 0, 0, 0))
    image_cut.paste(image, mask=mask)

    return image_cut


def process_gif(gif_file):
    """
    Procesa un archivo GIF dado, desmontándolo en frames,
    redimensionando cada frame y recortando la elipse.

    Parameters:
        gif_file (str): Nombre del archivo GIF a procesar.
    """
    # Desmontar el GIF en frames
    frames_directory = unmount_gif(gif_file)

    # Directorio donde se guardarán los frames procesados
    processed_frames_directory = os.path.join(frames_directory, "processed")
    if not os.path.isdir(processed_frames_directory):
        os.mkdir(processed_frames_directory)

    # Iterar sobre cada frame desmontado
    frames = os.listdir(frames_directory)
    for frame_file in frames:
        # Redimensionar la frame
        frame_path = os.path.join(frames_directory, frame_file)
        frame_rescaled = re_scale(frame_path, (300, 300))

        # Recortar la elipse
        frame_cut = cut_elipse(frame_rescaled)

        # Guardar la frame procesada
        processed_frame_path = os.path.join(processed_frames_directory, frame_file)
        frame_cut.save(processed_frame_path)

    print(f"Procesamiento de GIF '{gif_file}' completado.")


# Procesar todos los archivos GIF en el directorio de GIFs
if __name__ == "__main__":
    gif_files = os.listdir(PATH_GIFS)
    for gif_file in gif_files:
        process_gif(gif_file)

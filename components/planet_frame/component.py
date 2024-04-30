from frames import unmount_gif, re_scale, cut_elipse
import os

# Directorio donde se encuentran los archivos GIF
PATH_GIFS = r"planet_frame/gifs/marte.gif"

def process_gif(gif_file: str):
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
        frame = re_scale(frame_path, (300, 300))
        
        # Recortar la elipse
        frame_cut = cut_elipse(frame)
        
        # Guardar la frame procesada
        processed_frame_path = os.path.join(processed_frames_directory, frame_file)
        frame_cut.save(processed_frame_path)

# Procesar todos los archivos GIF en el directorio de GIFs
gif_files = os.listdir(PATH_GIFS)
for gif_file in gif_files:
    process_gif(gif_file)

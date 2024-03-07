from PIL import Image, ImageFilter
import os

# Ruta de la carpeta que contiene las imágenes
carpeta = r'\frames\marte'

# Obtener la lista de archivos en la carpeta
archivos_en_carpeta = os.listdir(carpeta)

# Iterar sobre cada archivo en la carpeta

for archivo in archivos_en_carpeta:
    # Comprobar si el archivo es una imagen (puedes agregar más extensiones según sea necesario)
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # Crear la ruta completa del archivo
        ruta_completa = os.path.join(carpeta, archivo)
        
        # Abrir la imagen original
        imagen_original = Image.open(ruta_completa)
        
        # Aplicar el filtro gaussiano
        imagen_procesada = imagen_original.filter(ImageFilter.GaussianBlur(radius=2))  # Puedes ajustar el radio según tus necesidades
        
        # Guardar la imagen procesada en la misma carpeta con un nuevo nombre
        nombre_archivo_procesado = 'gaussiano_' + archivo
        ruta_guardado = os.path.join(carpeta, nombre_archivo_procesado)
        imagen_procesada.save(ruta_guardado)
        
        # Cerrar los objetos de la clase Image
        imagen_original.close()
        imagen_procesada.close()

print("Proceso completado.")
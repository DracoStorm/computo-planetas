from PIL import Image
import os

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = r"animation\frames\marte"

# Definir el nuevo tamaño (en píxeles)
nuevo_tamaño = (50, 50)  # Cambia estos valores según tus necesidades

# Iterar sobre cada archivo en la carpeta
for archivo in os.listdir(carpeta_imagenes):
    if archivo.endswith(".png"):  # Solo procesar archivos PNG
        # Ruta completa de la imagen
        ruta_imagen = os.path.join(carpeta_imagenes, archivo)

        # Abrir la imagen
        imagen = Image.open(ruta_imagen)

        # Rescalar la imagen
        imagen_rescalada = imagen.resize(nuevo_tamaño)

        # Ruta para guardar la imagen rescalada (sobrescribe la imagen original)
        ruta_guardar = ruta_imagen

        # Guardar la imagen rescalada (sobrescribe la imagen original)
        imagen_rescalada.save(ruta_guardar)

        print("Imagen rescalada guardada exitosamente en:", ruta_guardar)
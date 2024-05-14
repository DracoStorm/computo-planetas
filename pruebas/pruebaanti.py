from PIL import Image

def cargar_imagen(ruta):
    """Carga una imagen desde la ruta especificada"""
    imagen = Image.open(ruta)
    return imagen

def aplicar_antialiasing(imagen):
    """Aplica un efecto de antialiasing a la imagen"""
    # Redimensionar la imagen a un tamaño más grande y luego reducirla para suavizar los bordes
    imagen_grande = imagen.resize((imagen.width * 2, imagen.height * 2), Image.LANCZOS)
    imagen_antialias = imagen_grande.resize((imagen.width, imagen.height), Image.LANCZOS)
    return imagen_antialias

def main():
    # Ruta de la imagen que deseas procesar
    ruta_imagen = r"C:\Users\alfre\OneDrive\Escritorio\imagenes\la_nasa_difunde_imagenes_en_360_grados_de_marte_2.jpg"
    
    # Cargar la imagen
    imagen_original = cargar_imagen(ruta_imagen)
    
    # Aplicar el efecto de antialiasing
    imagen_procesada = aplicar_antialiasing(imagen_original)
    
    # Guardar las imágenes con nombres específicos
    original_path = "original.png"
    processed_path = "aplicada_con_efecto.png"
    imagen_original.save(original_path)
    imagen_procesada.save(processed_path)
    
    # Mostrar las imágenes guardadas con los nombres de archivo en la consola
    print(f"Mostrando la imagen original: {original_path}")
    imagen_original.show()
    
    print(f"Mostrando la imagen con antialiasing: {processed_path}")
    imagen_procesada.show()

if __name__ == "__main__":
    main()

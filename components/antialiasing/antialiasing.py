from PIL import Image, ImageFilter


def cargar_imagen(ruta: str) -> Image:
    """
    Carga una imagen desde la ruta especificada.

    Args:
    - ruta (str): Ruta de la imagen a cargar.

    Returns:
    - Image: Objeto de imagen PIL.
    """
    imagen = Image.open(ruta)
    return imagen


def aplicar_antialiasing(imagen: Image, radio: int = 2) -> Image:
    """
    Aplica antialiasing a la imagen utilizando un filtro gaussiano.

    Args:
    - imagen (Image): Objeto de imagen PIL.
    - radio (int): Radio del filtro gaussiano. Valor por defecto: 2.

    Returns:
    - Image: Imagen suavizada.
    """
    imagen_suavizada = imagen.filter(ImageFilter.GaussianBlur(radius=radio))
    return imagen_suavizada


def guardar_imagen(imagen: Image, nombre: str):
    """
    Guarda la imagen en disco con el nombre especificado.

    Args:
    - imagen (Image): Objeto de imagen PIL.
    - nombre (str): Nombre de archivo para guardar la imagen.
    """
    imagen.save(nombre)
    print(f"Imagen guardada como {nombre}")


def main():
    # Ruta de la imagen que deseas suavizar
    # Cambia esto a la ruta de tu imagen
    ruta_imagen = "components/antialiasing/zelda.jpg"

    # Cargar la imagen
    imagen_original = cargar_imagen(ruta_imagen)

    # Aplicar antialiasing a la imagen
    imagen_suavizada = aplicar_antialiasing(imagen_original)

    # Guardar la imagen suavizada
    nombre_imagen_suavizada = "mi_imagen_suavizada.jpg"
    guardar_imagen(imagen_suavizada, nombre_imagen_suavizada)


if __name__ == "__main__":
    main()

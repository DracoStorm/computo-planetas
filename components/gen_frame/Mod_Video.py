from frames import generar_imagenes_superpuestas
from video import generar_video_salida

def main():
    imagenes_superpuestas = generar_imagenes_superpuestas()
    generar_video_salida("video_salida.mp4", imagenes_superpuestas)

if __name__ == "__main__":
    main()
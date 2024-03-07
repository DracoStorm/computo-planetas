import cv2

# Ruta del video original y nombre del video comprimido
video_original = 'animation/Video/video_comprimido.mp4'
video_comprimido = 'animation/Video/VideoCambiado.mp4'

# Abre el video original
cap = cv2.VideoCapture(video_original)

# Obtiene las propiedades del video original
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define el codec y crea el objeto VideoWriter
codec = cv2.VideoWriter_fourcc(*'avc1')

# Define el tamaño de los frames para el video comprimido
new_width = int(width)
new_height = int(height)

# Crea el objeto VideoWriter para el video comprimido
out = cv2.VideoWriter(video_comprimido, codec, fps, (new_width, new_height))

# Lee los frames del video original y escribe los frames en el video comprimido
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

# Libera los recursos
cap.release()
out.release()
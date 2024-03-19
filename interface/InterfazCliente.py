import tkinter as tk
from tkinter import filedialog
from server.Cliente3 import send_file

archivos_enviados = []  # Lista para almacenar los nombres de los archivos enviados


def enviar_archivo_interfaz():
    global archivos_enviados
    # Obtener la ruta del archivo seleccionado por el usuario
    file_path = filedialog.askopenfilename()

    # Añadir el nombre del archivo a la lista de archivos enviados
    archivos_enviados.append(file_path.split('/')[-1])

    # Dirección IP y puerto del servidor
    # Cambiar a la dirección IP real del servidor
    server_address = ('192.168.1.107', 12345)

    # Crear la ventana secundaria para mostrar el progreso de la transferencia
    progreso_window = tk.Toplevel(root)
    progreso_window.title("Progreso de Transferencia")
    progreso_window.geometry("600x200")
    progreso_window.configure(background='#31363F')

    # Etiqueta para mostrar el progreso y el nombre del archivo enviado
    progreso_label = tk.Label(
        progreso_window, background='#31363F', fg='white', font=('Arial', 20))
    progreso_label.pack(pady=20)

    # Llamar a la función para enviar el archivo
    send_file(file_path, server_address)

    # Mostrar mensaje al finalizar la transferencia
    progreso_label.config(
        text=f"Archivo enviado con éxito al servidor:\n{archivos_enviados[-1]}")

    # Mostrar todos los archivos enviados durante la conexión
    archivos_label.config(text="Archivos enviados:\n" + "\n".join(
        [f"{i + 1}. {archivo}" for i, archivo in enumerate(archivos_enviados)]))

    # Esperar a que se cierre la ventana secundaria antes de continuar
    progreso_window.wait_window()


# Crear la ventana principal
root = tk.Tk()
root.title("Enviar Archivo")
root.geometry("1000x800")
root.configure(background='#31363F')

# Etiqueta para mostrar instrucciones, centrada y con letra blanca
label = tk.Label(root, text="Seleccione el archivo que desea enviar:",
                 background='#31363F', fg='white', font=('Arial', 24))
label.pack(pady=20)

# Botón para abrir el explorador de archivos, centrado y con letra blanca
browse_button = tk.Button(root, text="Examinar Archivo", background='#31363F',
                          command=enviar_archivo_interfaz, fg='white', font=('Arial', 16))
browse_button.pack(pady=20)

# Etiqueta para mostrar el historial de archivos enviados
archivos_label = tk.Label(root, background='#31363F',
                          fg='white', font=('Arial', 16))
archivos_label.pack(pady=10)
archivos_label.config(text="Archivos enviados:\n")

# Ejecutar la aplicación
root.mainloop()
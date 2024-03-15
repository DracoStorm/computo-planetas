import tkinter as tk
from tkinter import filedialog
from network.Cliente3 import send_file

def enviar_archivo_interfaz():
    # Obtener la ruta del archivo seleccionado por el usuario
    file_path = filedialog.askopenfilename()

    # Dirección IP y puerto del servidor
    server_address = ('172.26.166.136', 12345)  # Cambiar a la dirección IP real del servidor

    # Crear la ventana secundaria para mostrar el progreso de la transferencia
    progreso_window = tk.Toplevel(root)
    progreso_window.title("Progreso de Transferencia")
    progreso_window.geometry("600x200")
    progreso_window.configure(background='#31363F')

    # Etiqueta para mostrar el progreso, centrada y con letra blanca
    progreso_label = tk.Label(progreso_window, background='#31363F',text="Enviando archivo...", fg='white', font=('Arial', 20))
    progreso_label.pack(pady=20)

    # Llamar a la función para enviar el archivo
    send_file(file_path, server_address)

    # Mostrar mensaje al finalizar la transferencia
    progreso_label.config(text="Archivo enviado con éxito al servidor.")

    # Esperar a que se cierre la ventana secundaria antes de continuar
    progreso_window.wait_window()

# Crear la ventana principal
root = tk.Tk()
root.title("Enviar Archivo")
root.geometry("1000x800")
root.configure(background='#31363F')
root.configure(bg='#31363F')

# Etiqueta para mostrar instrucciones, centrada y con letra blanca
label = tk.Label(root, text="Seleccione el archivo que desea enviar:", background='#31363F', fg='white', font=('Arial', 24))
label.pack(pady=20)

# Botón para abrir el explorador de archivos, centrado y con letra blanca
browse_button = tk.Button(root, text="Examinar Archivo", background='#31363F',command=enviar_archivo_interfaz, fg='white', font=('Arial', 16))
browse_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
import tkinter as tk
from tkinter import filedialog
from Cliente3 import send_file

def enviar_archivo_interfaz():
    # Obtener la ruta del archivo seleccionado por el usuario
    file_path = filedialog.askopenfilename()

    # Dirección IP y puerto del servidor
    server_address = ('172.26.166.136', 12345)  # Cambiar a la dirección IP real del servidor

    # Crear la ventana secundaria para mostrar el progreso de la transferencia
    progreso_window = tk.Toplevel(root)
    progreso_window.title("Progreso de Transferencia")
    progreso_window.geometry("400x200")
    progreso_window.configure(background='#31363F')

    # Etiqueta para mostrar el progreso
    progreso_label = tk.Label(progreso_window, text="Enviando archivo...")
    progreso_label.pack()

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

# Etiqueta para mostrar instrucciones
label = tk.Label(root, text="Seleccione el archivo que desea enviar:")
label.pack()

# Botón para abrir el explorador de archivos
browse_button = tk.Button(root, text="Examinar Archivo", command=enviar_archivo_interfaz)
browse_button.pack()

# Ejecutar la aplicación
root.mainloop()
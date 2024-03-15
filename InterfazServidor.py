import tkinter as tk
from tkinter import filedialog
import socket
import os

def browse_file():
    filename = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, filename)

def start_transfer():
    file_path = entry_path.get()
    if not file_path:
        status_label.config(text="Selecciona un archivo primero.", fg="red")
        return

    server_address = ('0.0.0.0', 12345)  # Cambiar a la dirección IP real del servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
        client_ip = client_socket.getsockname()[0]
        if client_ip not in allowed_ips:
            status_label.config(text="No estás autorizado para conectar.", fg="red")
            return

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        client_socket.send(f"{file_name}@{file_size}".encode('utf-8'))

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

        status_label.config(text="Archivo enviado con éxito.", fg="green")

    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

    finally:
        client_socket.close()

# Interfaz gráfica
root = tk.Tk()
root.title("Transferencia de Archivos")

label_path = tk.Label(root, text="Ruta del archivo:")
label_path.pack()

entry_path = tk.Entry(root, width=50)
entry_path.pack()

btn_browse = tk.Button(root, text="Seleccionar archivo", command=browse_file)
btn_browse.pack()

btn_send = tk.Button(root, text="Enviar archivo", command=start_transfer)
btn_send.pack()

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
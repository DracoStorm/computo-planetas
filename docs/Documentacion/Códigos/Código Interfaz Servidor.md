# Código Interfaz Servidor

En este código creamos un servidor que conecta con clientes para transferir archivos. Todo se hace mediante una interfaz gráfica. Se genera una lista de IP's autorizadas para enlazarse.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Proporciona acceso a la comunicación en red.
*   [threading](../librerias/Librería_Thread.md), Permite que un programa ejecute múltiples operaciones simultáneamente en el mismo espacio de proceso.
*   [tkinter](../librerias/Librería_Tkinter.md), Es una librería que proporciona clases que permiten la creación de una interfaz gráfica de usuario.



## Funciones
1.  Función `handle client`:

    Maneja la transferencia de archivos. Registra nombres y tamaños. Guarda los archivos. Maneja excepciones. Cierra la conexión terminada la transferencia.

2.  Función `add_ip`:

    Aquí se añaden las IP's que ingresen los usuarios y las agrega a la lista de IP's autorizadas. Actualiza la lista mostrada en la interfaz.

3.  Función `start_server`:

    Configura el servidor, lo inicializa. Verifica si las conexiones que se solicitan están permitidas. Puede cerrar el servidor manualmente.



### *Código*
[*InterfazServidor.py*](../../../interface/InterfazServidor.py)
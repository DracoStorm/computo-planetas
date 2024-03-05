# Conexión Cliente-Servidor

Este programa implementa una conexión cliente-servidor donde el cliente puede enviar mensajes de texto o archivos al servidor.

## Archivo Python

### `cliente.py`

Este archivo contiene el código del cliente que se conecta al servidor y puede enviar mensajes de texto o archivos.

#### Función `iniciar_cliente()`

Esta función inicia el cliente y establece la conexión con el servidor a través de un socket TCP. Permite al usuario enviar mensajes de texto o archivos al servidor.

- **Procedimiento**:
  - El cliente se conecta al servidor utilizando un socket TCP.
  - Mientras el usuario ingrese mensajes:
    - Si el mensaje comienza con "ARCHIVO:", se interpreta como el nombre y la ruta de un archivo a enviar al servidor.
      - Se divide el mensaje para extraer la ruta del archivo y su destino en el servidor.
      - Se llama a la función `enviarArchivo()` para enviar el archivo al servidor.
    - Si el mensaje no comienza con "ARCHIVO:", se envía como texto plano al servidor.
      - Se codifica el mensaje en UTF-8 y se envía al servidor.
      - Se espera la respuesta del servidor y se imprime en la consola.
  - La conexión se cierra cuando el usuario no ingresa ningún mensaje.

#### Función `enviarArchivo(socketCliente, rutaEnvio, rutaDestino)`

Esta función envía un archivo al servidor.

- **Parámetros**:
  - `socketCliente`: Socket TCP para la conexión con el servidor.
  - `rutaEnvio`: Ruta del archivo a enviar desde el cliente.
  - `rutaDestino`: Ruta de destino en el servidor donde se guardará el archivo.
- **Procedimiento**:
  - Se envía un mensaje al servidor indicando que se enviará un archivo, junto con la ruta de origen y destino.
  - Se abre el archivo en modo lectura binaria y se envían los datos al servidor en bloques de 1024 bytes.
  - Se envía un mensaje de finalización al servidor para indicar que se ha enviado todo el archivo.

## Detalles de Funcionamiento

El cliente establece una conexión con el servidor a través de un socket TCP y envía mensajes de texto o archivos. Cuando se envía un archivo, el cliente indica al servidor que recibirá un archivo, luego transfiere el archivo en bloques de datos al servidor. Después de enviar cada archivo, el cliente cierra la conexión.

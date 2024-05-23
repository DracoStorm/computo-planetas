# Librería io

<p align="center">
  <img src="io.jpg">
</p>

Este módulo proporciona las funciones principales de Python para manejar varios tipos de entrada/salida. Hay tres tipos principales de E/S: texto, binaria y sin formato.

## Lo más importante

1.  io.open():

    Abre un archivo para leer o escribir, en forma string (predeterminada) o binaria.

2.  io.BytesIO:


    Una clase para manejar datos binarios en memoria como si fueran un archivo.

3.  io.StringIO:

    Similar a BytesIO, pero para datos de texto. Permite trabajar con cadenas de texto en memoria como si fueran archivos.

4.  io.FileIO:

    Una clase para leer y escribir archivos en disco. Se utiliza para operaciones de E/S de bajo nivel con archivos.

5.  io.write():

    Escribe en el archivo el valor de cada argumento. Los argumentos deben ser cadenas o números.

6.  io.input(), io.output:

    Establecen el tipo de archivo de entrada y salida predeterminado.

<br>
<br>
<br>

### Todo el contenido

io.BlockingIOError <br>
io.BufferedIOBase <br>
io.BufferedRandom <br>
io.BufferedReader <br>
io.BufferedRWPair <br>
io.BufferedWriter <br>
io.BytesIO <br>
io.DEFAULT_BUFFER_SIZE <br>
io.FileIO <br>
io.IOBase <br>
io.IOError <br>
io.IOBase.__enter__ <br>
io.IOBase.__exit__ <br>
io.IOBase.close <br>
io.IOBase.closed <br>
io.IOBase.detach <br>
io.IOBase.fileno <br>
io.IOBase.flush <br>
io.IOBase.isatty <br>
io.IOBase.read <br>
io.IOBase.readable <br>
io.IOBase.readline <br>
io.IOBase.readlines <br>
io.IOBase.seek <br>
io.IOBase.seekable <br>
io.IOBase.tell <br>
io.IOBase.truncate <br>
io.IOBase.writable <br>
io.IOBase.write <br>
io.IOBase.writelines <br>
io.IncrementalNewlineDecoder <br>
io.RawIOBase <br>
io.RawIOBase.read <br>
io.RawIOBase.readall <br>
io.RawIOBase.readinto <br>
io.RawIOBase.readinto1 <br>
io.RawIOBase.readline <br>
io.RawIOBase.seek <br>
io.RawIOBase.tell <br>
io.RawIOBase.truncate <br>
io.RawIOBase.write <br>
io.StringIO <br>
io.TextIOBase <br>
io.TextIOBase.detach <br>
io.TextIOBase.encoding <br>
io.TextIOBase.errors <br>
io.TextIOBase.newlines <br>
io.TextIOBase.read <br>
io.TextIOBase.readline <br>
io.TextIOBase.seek <br>
io.TextIOBase.tell <br>
io.TextIOWrapper <br>
io.UnsupportedOperation <br>
io.open <br>
io.TextIOWrapper.__init__ <br>
io.TextIOWrapper.__repr__ <br>
io.TextIOWrapper.buffer <br>
io.TextIOWrapper.close <br>
io.TextIOWrapper.closed <br>
io.TextIOWrapper.detach <br>
io.TextIOWrapper.encoding <br>
io.TextIOWrapper.errors <br>
io.TextIOWrapper.fileno <br>
io.TextIOWrapper.flush <br>
io.TextIOWrapper.isatty <br>
io.TextIOWrapper.line_buffering <br>
io.TextIOWrapper.mode <br>
io.TextIOWrapper.name <br>
io.TextIOWrapper.newlines <br>
io.TextIOWrapper.read <br>
io.TextIOWrapper.readable <br>
io.TextIOWrapper.readline <br>
io.TextIOWrapper.readlines <br>
io.TextIOWrapper.seek <br>
io.TextIOWrapper.seekable <br>
io.TextIOWrapper.tell <br>
io.TextIOWrapper.truncate <br>
io.TextIOWrapper.writable <br>
io.TextIOWrapper.write <br>
io.TextIOWrapper.write_through <br>
io.BufferedReader.__init__ <br>
io.BufferedReader.__enter__ <br>
io.BufferedReader.__exit__ <br>
io.BufferedReader.__repr__ <br>
io.BufferedReader.close <br>
io.BufferedReader.closed <br>
io.BufferedReader.detach <br>
io.BufferedReader.fileno <br>
io.BufferedReader.flush <br>
io.BufferedReader.isatty <br>
io.BufferedReader.peek <br>
io.BufferedReader.read <br>
io.BufferedReader.read1 <br>
io.BufferedReader.readable <br>
io.BufferedReader.readline <br>
io.BufferedReader.readlines <br>
io.BufferedReader.seek <br>
io.BufferedReader.seekable <br>
io.BufferedReader.tell <br>
io.BufferedReader.truncate <br>
io.BufferedReader.writable <br>
io.BufferedReader.write <br>
io.BufferedWriter.__init__ <br>
io.BufferedWriter.__enter__ <br>
io.BufferedWriter.__exit__ <br>
io.BufferedWriter.__repr__ <br>
io.BufferedWriter.close <br>
io.BufferedWriter.closed <br>
io.BufferedWriter.detach <br>
io.BufferedWriter.fileno <br>
io.BufferedWriter.flush <br>
io.BufferedWriter.isatty <br>
io.BufferedWriter.read <br>
io.BufferedWriter.read1 <br>
io.BufferedWriter.readable <br>
io.BufferedWriter.readline <br>
io.BufferedWriter.readlines <br>
io.BufferedWriter.seek <br>
io.BufferedWriter.seekable <br>
io.BufferedWriter.tell <br>
io.BufferedWriter.truncate <br>
io.BufferedWriter.writable <br>
io.BufferedWriter.write <br>
io.BufferedRandom.__init__ <br>
io.BufferedRandom.__enter__ <br>
io.BufferedRandom.__exit__ <br>
io.BufferedRandom.__repr__ <br>
io.BufferedRandom.close <br>
io.BufferedRandom.closed <br>
io.BufferedRandom.detach <br>
io.BufferedRandom.fileno <br>
io.BufferedRandom.flush <br>
io.BufferedRandom.isatty <br>
io.BufferedRandom.peek <br>
io.BufferedRandom.read <br>
io.BufferedRandom.read1 <br>
io.BufferedRandom.readable <br>
io.BufferedRandom.readline <br>
io.BufferedRandom.readlines <br>
io.BufferedRandom.seek <br>
io.BufferedRandom.seekable <br>
io.BufferedRandom.tell <br>
io.BufferedRandom.truncate <br>
io.BufferedRandom.writable <br>
io.BufferedRandom.write <br>
io.BufferedIOBase.__enter__ <br>
io.BufferedIOBase.__exit__ <br>
io.BufferedIOBase.close <br>
io.BufferedIOBase.closed <br>
io.BufferedIOBase.detach <br>
io.BufferedIOBase.fileno <br>
io.BufferedIOBase.flush <br>
io.BufferedIOBase.isatty <br>
io.BufferedIOBase.peek <br>
io.BufferedIOBase.read <br>
io.BufferedIOBase.read1 <br>
io.BufferedIOBase.readable <br>
io.BufferedIOBase.readline <br>
io.BufferedIOBase.readlines <br>
io.BufferedIOBase.seek <br>
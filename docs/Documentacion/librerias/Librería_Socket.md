# Librería Socket

<p align="center">
  <img src="socket.png">
</p>

Los sockets son una estructura que permite la conexión entre dos aplicaciones, procesos o equipos, estableciendo una relación cliente/servidor, que permite el intercambio de datos, incluso entre programas colocados en ordenadores diferentes. <br>
Este módulo lo utilizamos para conectar distintas computadoras y compartir archivos.

## Lo más importante

1.  socket.socket()

    Crea un objeto socket.

2.  socket.connect():

    Conecta el socket a una dirección remota (IP y el número de puerto). Lo vuelve un cliente.

3.  socket.listen():

    Permite que el socket acepte conexiones. Lo vuelve un servidor.

4.  socket.accept():

    Acepta una conexión entrante. Devuelve un nuevo socket conectado y la dirección del cliente.

5.  socket.send():

    Envía datos a través del socket. Los datos deben ser de tipo bytes.

<br>
<br>
<br>

### Todo el contenido

socket() <br>
socketpair() <br>
fromfd() <br>
send_fds() <br>
recv_fds()  <br>
fromshare() <br>
gethostname() <br>
gethostbyname() <br>
gethostbyaddr() <br>
getservbyname() <br>
getprotobyname() <br>
ntohs(), ntohl() <br>
htons(), htonl() <br>
inet_aton() <br>
inet_ntoa() <br>
socket.getdefaulttimeout() <br>
socket.setdefaulttimeout() <br>
create_connection() <br>













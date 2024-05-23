# Código "Server"

Este es un servidor que acepta conexiones de clientes en dos direcciones IP diferentes. Dependiendo de la dirección del cliente, se ejecutan diferentes componentes. Acepta hasta 5 conexiones.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Actúa como un enlace de comunicación entre un servidor y un cliente.
*   [threading](../librerias/Librería_Thread.md), Permite que un programa ejecute múltiples operaciones simultáneamente en el mismo espacio de proceso.
*   [network](../../../network/exceptions.py) y [comp_threads](../../../components/gen_frame/), Nuestros módulos personalizados con componentes que necesitamos.



## Funciones

1. Función `main`:

    Inicializa el servidor. Prepara un lista de espera de máximo 5 conexiones. Inicia un bucle en el que en cada iteración, acepta y verifica las conexiones. <br>
    El componente compute_traj se ejecuta cuando el cliente se conecta desde la dirección IP_COMPUTE_TRJ. <br>
    El componente gen_frame se ejecuta cuando el cliente se conecta desde la dirección IP_GEN_FRAME. <br>
    Ambos componentes se ejecutan en subprocesos separados para manejar conexiones de forma simultánea. El servidor está configurado para utilizar una barrera que se activa después de cierto número de iteraciones.



### *Código*

[*server.py*](../../../server/server.py)
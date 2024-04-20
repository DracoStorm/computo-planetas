# Identificadores de tipo de envio de red
FILE_IDENTIFIER = b'FILE'
MSG_IDENTIFIER = b'MSG'
ERR_IDENTIFIER = b'ERR'
SHUTDOWN_IDENTIFIER = b'STDN'
OK_IDENTIFIER = b'OK'

# Lista de ips según los componentes
IP_COMPUTE_TRJ = '192.168.100.61'
IP_PLANET_FRAME = '0.0.0.0'
IP_GEN_FRAME = '192.168.100.72'
IP_ANTIALIASING = '0.0.0.0'
IP_GEN_VIDEO = '0.0.0.0'

IPS = [
    IP_COMPUTE_TRJ,
    IP_PLANET_FRAME,
    IP_GEN_FRAME,
    IP_ANTIALIASING,
    IP_GEN_VIDEO
]

# Definir el servidor y el puerto
SERVER_IP = '192.168.100.21'
SERVER_PORT = 22333

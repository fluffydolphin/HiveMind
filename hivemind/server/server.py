import socket
from threading import Thread
import random
import argparse
import sys


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument(
    "-p", "--port", default=5000, help="Port of the Server", type=int
)


args = parser.parse_args()
host =  "0.0.0.0"


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)


client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, args.port))
s.listen(5)
print(f"[*] Listening as {host}:{args.port}")
separator_token = "<SEP>"

name = "server"


def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())
            

c = socket.socket()
print(f"[*] Connecting to {host}:{args.port}...")
c.connect((host, args.port))
print("[+] Connected.")
        

def listen_for_messages():
    while True:
        message = c.recv(1024).decode()
        print("\n" + message)


l = Thread(target=listen_for_messages)
l.daemon = True
l.start()
    

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.") 
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()


for cs in client_sockets:
    cs.close()

s.close()


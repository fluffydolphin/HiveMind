import socket
from threading import Thread
import random


HOST = "0.0.0.0"
PORT = 420
SERVER_HOST = "192.168.3.49"
SERVER_PORT = 420


client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print(f"[*] Listening as {HOST}:{PORT}")


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
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
c.connect((SERVER_HOST, SERVER_PORT))
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


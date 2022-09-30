import socket
import logging
from threading import Thread
from webbrowser import get
import random
from datetime import datetime
from colorama import Fore, init, Back
import json

# server's IP address
HOST = "0.0.0.0"
PORT = 420 # port we want to use
SERVER_HOST = "192.168.3.10"
SERVER_PORT = 420 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((HOST, PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {HOST}:{PORT}")

name = "fluffydolphin"

def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP> 
            # token with ": " for nice printing
            msg = msg.replace(separator_token, ": ")
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())
            
# initialize TCP socket
c = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
c.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
        
def listen_for_messages():
    while True:
        message = c.recv(1024).decode()
        print("\n" + message)


# make a thread that listens for messages to this client & print them
l = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
l.daemon = True
# start the thread
l.start()
    

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.") 
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()


